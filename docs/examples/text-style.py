from textual.app import App, ComposeResult
from textual.widgets import Static


class TextStyleDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("This is some text.", classes="")
        yield Static("This is some text.", classes="bold")
        yield Static("This is some text.", classes="italic")
        yield Static("This is some text.", classes="underline")
        yield Static("This is some text.", classes="strike")
        yield Static("This is some text.", classes="reverse")
        

if __name__ == "__main__":
    app = TextStyleDemo()
    app.run()