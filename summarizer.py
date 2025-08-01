from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.model_map = {
            "BART": "facebook/bart-large-cnn",
            "T5": "t5-small",
            "Pegasus": "google/pegasus-xsum"
        }

        # Preload all models into memory once
        self.pipelines = {
            name: pipeline("summarization", model=model_id)
            for name, model_id in self.model_map.items()
        }

    def summarize(self, text, model_choice, max_length=130, min_length=30):
        if not text.strip():
            return "Please enter some text."

        summarizer = self.pipelines.get(model_choice)
        if not summarizer:
            return f"Model '{model_choice}' not found."

        result = summarizer(text, max_length=int(max_length), min_length=int(min_length), do_sample=False)
        return result[0]['summary_text']
