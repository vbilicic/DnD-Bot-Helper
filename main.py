import os
from dotenv import load_dotenv
load_dotenv()

import logging
import sys

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt as default_messages_to_prompt,
    completion_to_prompt as default_completion_to_prompt,
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding

# Logging setup
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load environment
model_path = os.getenv("MODEL_PATH", "./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")
data_path = os.getenv("DATA_DIR", "./data")

# Load documents
documents = SimpleDirectoryReader(data_path).load_data()

# Setup LLM
llm = LlamaCPP(
    model_path=model_path,
    temperature=0.1,
    max_new_tokens=256,
    context_window=3900,
    model_kwargs={"n_gpu_layers": -1},
    messages_to_prompt=default_messages_to_prompt,
    completion_to_prompt=default_completion_to_prompt,
    verbose=True,
)

# Embedding model
embed_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
embed_model = LangchainEmbedding(embed_model)

Settings.llm = llm
Settings.embed_model = embed_model

# Build index and query engine
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

print(" Welcome to the D&D 5e LLM Assistant! Ask me anything about the handbook.\n")

while True:
    try:
        query = input(" What would you like to ask? ")
        if query.lower() in ("exit", "quit"):
            print(" Goodbye!")
            break
        response = query_engine.query(query)
        print(f"\n {response}\n")
    except KeyboardInterrupt:
        print("\n Exiting...")
        break
