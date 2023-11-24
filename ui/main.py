"""Frontend for the Base64 App"""
import gradio as gr
from func import Decode, Encode

with gr.Blocks(theme=gr.themes.Base(),title="Base64") as base64:
    gr.Markdown("""
                # Base64 Encode and Decode app
                Input your data in either of the boxes and click the relavant button.
                """)
    with gr.Tab("Base64"):
        plain_text = gr.TextArea(
            lines=5,
            label="Plain Text",
            placeholder="Tanzu Rocks!!!")
        encoded_text = gr.TextArea(
            lines=5,
            label="Encoded Text",
            placeholder="VGFuenUgUm9ja3MhISE=")
    with gr.Row():
        encode_button = gr.Button("Encode")
        decode_button = gr.Button("Decode")

    encode_button.click(
        fn=Encode,
        inputs=plain_text,
        outputs=encoded_text)
    decode_button.click(
        fn=Decode,
        inputs=encoded_text,
        outputs=plain_text)


if __name__ == "__main__":
    base64.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=8080,
        show_api=False
        )
