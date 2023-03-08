from textual.app import App, ComposeResult
from textual.widgets import Static


class BorderSidesDemo(App):
    CSS_PATH = "tuilwind.min.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("t", classes="p-1 text-center text-gray-800 bg-gray-200 border-t-heavy-gray-600")
        yield Static("l", classes="p-1 text-center text-gray-800 bg-gray-300 border-l-heavy-gray-600")
        yield Static("r", classes="p-1 text-center text-gray-800 bg-gray-200 border-r-heavy-gray-600")
        yield Static("b", classes="p-1 text-center text-gray-800 bg-gray-300 border-b-heavy-gray-600")
        yield Static("x", classes="p-1 text-center text-gray-800 bg-gray-200 border-x-heavy-gray-600")
        yield Static("y", classes="p-1 text-center text-gray-800 bg-gray-300 border-y-heavy-gray-600")

if __name__ == "__main__":
    app = BorderSidesDemo()
    app.run()