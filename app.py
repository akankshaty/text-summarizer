import gradio as gr
from summarizer import TextSummarizer

# Create one instance and reuse
summarizer = TextSummarizer()

def summarize_text(text, model_choice):
    return summarizer.summarize(text, model_choice)

gr.Interface(
    fn=summarize_text,
    inputs=[
        gr.Textbox(lines=10, label="Enter text to summarize"),
        gr.Dropdown(choices=["BART", "T5", "Pegasus"], label="Model", value="BART")
    ],
    outputs="textbox",
    title="Preloaded AI Text Summarizer"
).launch()