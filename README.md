# AI Text Summarizer

A Python-based text summarization app using Hugging Face transformers with a clean object-oriented design.  
Supports multiple models - BART, T5, and Pegasus - with options for single-model summarization or side-by-side comparison in an interactive Gradio web UI.

> **Note:** This project is part of my personal journey to learn AI and understand how transformer models work in practice.  
> It helps me experiment hands-on with different models and learn best practices in building AI applications.

## Features

- Summarize text using popular transformer models (BART, T5, Pegasus)
- Preloads models for fast switching between them
- Two UI modes:  
  - **Single model summarization** with customizable length parameters  
  - **Side-by-side comparison** showing outputs from all three models  
- Built with modular, reusable, and extensible OOP code  
- Easy to run locally with minimal setup


## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/akankshaty/ai-text-summarizer.git
   cd ai-text-summarizer

2. (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
   
4. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
Run the app
```bash
python app.py
```

This launches a Gradio web interface (usually at http://127.0.0.1:7860) where you can:

- Enter text to summarize
- Choose a single model or compare all three side-by-side
- Adjust summary length parameters (max and min length)


## Project Structure

```
text_summarizer/
├── app.py           # Gradio UI code with tabs for single & multi-model
├── summarizer.py    # TextSummarizer class loading and managing models
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## How It Works

- The `TextSummarizer` class preloads the three transformer models on initialization.
- Summarization calls are routed through this class for easy model switching and reuse.
- The Gradio UI provides two tabs for single-model summarization and multi-model output comparison.

## Learn More

- Models used:
  - [BART](https://huggingface.co/facebook/bart-large-cnn)
  - [T5](https://huggingface.co/t5-small)
  - [Pegasus](https://huggingface.co/google/pegasus-xsum)
- Transformer concepts: [Jay Alammar's Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- Hugging Face course: https://huggingface.co/course/chapter1

## Contributing

Feel free to open issues or submit pull requests!  
Suggestions to add features like PDF summarization, token count display, or export options are welcome.

## License

[MIT License](LICENSE)


