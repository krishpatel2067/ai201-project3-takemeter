import gradio as gr
from model_manager import classify

demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=5, label="Post", placeholder="Enter a post to classify..."),
    outputs=[
        gr.Textbox(label="Predicted Label"),
        gr.Label(label="Confidence Scores"),
    ],
    title="TakeMeter Classifier",
    description=(
        "_Krish A. Patel_\n\n"
        "_CodePath AI201: Applications of AI Engineering Project 3 (Summer 2026)_\n\n"
        "Classifies a social media post as artistic critique, external narrative, or fandom expression."
    ),
)

if __name__ == "__main__":
    demo.launch()
