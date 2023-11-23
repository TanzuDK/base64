import gradio as gr
from func import Decode, Encode

with gr.Blocks(title="Base64") as base64:
    gr.HTML=("<h1>Base64</h1>")
    gr.Markdown("Base64 Encode and Decode app")
    with gr.Tab("Base64"):
        plain_text = gr.TextArea(lines=5, label="Plain Text")
        encoded_text = gr.TextArea(lines=5, label="Encoded Text")
    with gr.Row():
        encode_button = gr.Button("Encode")
        decode_button = gr.Button("Decode")
    encode_button.click(fn=Encode, inputs=plain_text, outputs=encoded_text)
    decode_button.click(fn=Decode, inputs=encoded_text, outputs=plain_text)



if __name__ == "__main__":
    base64.launch() 