from textual.app import App, ComposeResult
from textual.widgets import Static


class BorderDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("first",  classes="p-2 text-center text-gray-800 bg-gray-100 border-solid-gray-900")
        yield Static("second", classes="p-2 text-center text-gray-800 bg-gray-200 border-round-gray-900")
        yield Static("third",  classes="p-2 text-center text-gray-800 bg-gray-400 border-double-gray-900")

if __name__ == "__main__":
    app = BorderDemo()
    app.run()