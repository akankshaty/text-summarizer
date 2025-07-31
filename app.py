from transformers import pipeline
import gradio as gr

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

gr.Interface(fn=summarize_text, inputs="textbox", outputs="textbox", title="AI Text Summarizer").launch()
