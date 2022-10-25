from textual.app import App, ComposeResult
from textual.widgets import Static

text = """This text is certainly a fair bit long to proove a point. 
Oh my yes indeed, it really is a fair bit longer than many other examples!"""

class TextAlignmentDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static(text, classes="p-1 bg-green-400 text-left")
        yield Static(text, classes="p-1 bg-red-400 text-center")
        yield Static(text, classes="p-1 bg-blue-400 text-right")
        yield Static(text, classes="p-1 bg-yellow-400 text-justify")
        yield Static(text, classes="p-1 bg-lime-400 text-start")
        yield Static(text, classes="p-1 bg-cyan-400 text-end")

if __name__ == "__main__":
    app = TextAlignmentDemo()
    app.run()