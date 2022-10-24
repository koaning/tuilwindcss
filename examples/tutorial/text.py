from textual.app import App, ComposeResult
from textual.widgets import Static


class PaddingDemo(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("# This is the blue bit!", classes="text-center bold")
        for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            yield Static("This is some example text.", classes=f"bg-blue-400 text-blue-{i}")
        yield Static("# This is a new section!", classes="text-center bold")
        for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            yield Static("This is some example text.", classes=f"bg-white text-gray-{i}")

if __name__ == "__main__":
    app = PaddingDemo()
    app.run()