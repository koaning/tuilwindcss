from textual.app import App, ComposeResult
from textual.widgets import Static


class PaddingDemo(App):
    CSS_PATH = "tuilwind.min.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("p-1", classes="p-1 bg-blue-400")
        yield Static("p-2", classes="p-2 bg-blue-500")
        yield Static("p-3", classes="p-3 bg-blue-600")
        yield Static("p-4", classes="p-4 bg-blue-700")

if __name__ == "__main__":
    app = PaddingDemo()
    app.run()