#D&D 5e Handbook LLM Assistant

This project is a local language model-powered assistant that can answer questions about the Dungeons & Dragons 5e Player's Handbook, running entirely on your machine using LlamaIndex, llama-cpp-python, and local embeddings from HuggingFace.

## Features :

    - Ask questions like "What are available classes?" or "How does spellcasting work?"

    - Uses Mistral 7B Instruct as a local LLM 
    (Can be changed for any other open source llm that is GGUF format compatible with l)

    - Embeddings via sentence-transformers/all-mpnet-base-v2

    - Local PDF ingestion using LlamaIndex and llama-index-readers-file

    - No OpenAI or API keys required — everything runs locally

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/dnd-llm-assistant.git
cd dnd-llm-assistant
```

### 2. Create environment

- With Conda:

```bash
conda env create -f environment.yml
conda activate llama_env
```

- Or with pip:

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage :

### 1. Place the D&D PDF in the following directory (or change the path in main.py):

- `data/ (D&D 5e - Players Handbook.pdf)

### 2. Place your .gguf quantized model here (or set a model URL)

- `models/`

### 3. Run the assistant:

```bash
python main.py
```

You’ll be prompted to enter questions like:

- What are available classes?
- What is the difference between a wizard and a sorcerer?

## Model Info

- LLM: Mistral 7B Instruct GGUF Q4_K_M
- Embedding model: sentence-transformers/all-mpnet-base-v2

## Notes

- Edit `.env.example` with appropriate values and rename to `.env` if needed.
- CUDA is assumed for performance. Make sure your system is GPU-ready.

## Project Structure

├── Data/
│   └── D&D 5e - Players Handbook.pdf
├── main.py
├── requirements.txt
├── environment.yml
└── README.md

## Credits
LlamaIndex
llama-cpp-python
TheBloke on HuggingFace
Sentence Transformers
Wizards of the Coast
D&D Beyond
