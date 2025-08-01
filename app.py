import gradio as gr
from summarizer import TextSummarizer

# Create one instance and reuse
summarizer = TextSummarizer()

def summarize_text(text, model_choice):
    return summarizer.summarize(text, model_choice)

# --- All Model Comparison ---
def summarize_all_models(text):
    results = summarizer.summarize_with_all_models(text)
    return results["BART"], results["T5"], results["Pegasus"]

with gr.Blocks(title="AI Text Summarizer") as demo:
    gr.Markdown("## ✨ AI Text Summarizer")
    with gr.Tab("Single Model"):
        with gr.Row():
            textbox = gr.Textbox(label="Enter text", lines=10)
        with gr.Row():
            model_dropdown = gr.Dropdown(choices=["BART", "T5", "Pegasus"], label="Model", value="BART")
        summarize_btn = gr.Button("Summarize")
        single_output = gr.Textbox(label="Summary")

        summarize_btn.click(
            summarize_text,
            inputs=[textbox, model_dropdown],
            outputs=single_output
        )

    with gr.Tab("Compare All Models"):
        multi_text = gr.Textbox(label="Enter text", lines=10)
        compare_btn = gr.Button("Compare")
        with gr.Row():
            bart_output = gr.Textbox(label="BART")
            t5_output = gr.Textbox(label="T5")
            pegasus_output = gr.Textbox(label="Pegasus")

        compare_btn.click(
            summarize_all_models,
            inputs=multi_text,
            outputs=[bart_output, t5_output, pegasus_output]
        )

demo.launch()