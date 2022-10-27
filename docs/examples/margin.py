from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical

class MarginDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Vertical(
            Static("m-1 p-1", classes="m-1 p-1 bg-gray-200 border-round-gray-600 text-gray-600"),
            Static("m-2 p-1", classes="m-2 p-1 bg-gray-200 border-round-gray-600 text-gray-600"),
            Static("m-3 p-2", classes="m-3 p-2 bg-gray-200 border-round-gray-600 text-gray-600"),
            classes="bg-gray-300"
        )

if __name__ == "__main__":
    app = MarginDemo()
    app.run()