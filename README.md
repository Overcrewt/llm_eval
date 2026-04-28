# LLM Cybersecurity Evaluator

This project contains scripts to automate the querying and evaluation of Large Language Models on a set of cybersecurity questions.

## Setup Instructions for DigitalOcean GPU Droplets

DigitalOcean GPU droplets (e.g., using NVIDIA H100 or A100) come with drivers pre-installed. However, to leverage the GPU for fast inference with `llama.cpp`, you must install `llama-cpp-python` with CUDA support enabled.

1. Create a Python virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install `llama-cpp-python` with CUDA acceleration:
```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --no-cache-dir
```

3. Install the remaining requirements:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Generating Answers (`ask_llm.py`)
Run the first script to query the model you want to test.
```bash
python ask_llm.py
```
You will be prompted to enter the Hugging Face URL for the `.gguf` file of the model you want to test (e.g., `https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf`).
The script will download it automatically and begin answering questions from `questions.json`.
The responses will be saved in `answers_llm.json`. If interrupted, simply rerun it and it will resume where it left off.

### 2. Evaluating Answers (`evaluate_llm.py`)
Run the second script to evaluate the generated answers.
```bash
python evaluate_llm.py
```
The script will:
- Automatically download an evaluator model (Meta-Llama-3-8B-Instruct.Q4_K_M.gguf).
- Ask you to enter metadata about the model you just tested (Name, Type, Params, etc.).
- Compare the answers in `answers_llm.json` against the reference answers.
- Append a detailed breakdown and Markdown table of the scores to `report.md`.
