import reflex as rx

from ui.func import Decode, Encode

box_style = {
    "width":"90%",
    "height":"200px",
    "max_width":"1024px",
    "bg":"white",
    "padding":"2em",
    "border_radius":"50px",
}

button_style = {
    "color":"white",
    "bg":"black",
}

class State(rx.State):
    text: str
    result: str

    def Plain_text(self) -> str:
        self.result = Encode(self.text)

    def Encoded_text(self) -> str:
        self.result = Decode(self.text)



def index():
    return rx.vstack(
                rx.image(
                    src="base64 - header.png",
                ),
                #rx.text("Insert text : "),
                rx.text_area(
                    on_blur=State.set_text,
                    placeholder="Type your text here...",
                    style=box_style,
                ),
                rx.hstack(
                    rx.button(
                        "Encode",
                        on_click=State.Plain_text,
                        style=button_style,
                        ),
                    rx.button(
                        "Decode",
                        on_click=State.Encoded_text,
                        style=button_style,

                    ),
                ),

                rx.text_area(
                    default_value=State.result,
                    placeholder="Converted text...",
                    is_read_only=True,
                    style=box_style,
                ),


        #rx.text(State.result),
        #rx.text(State.Encoded_text),
        
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index, title="Base64")
app.compile()