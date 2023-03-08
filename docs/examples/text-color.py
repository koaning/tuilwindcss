from textual.app import App, ComposeResult
from textual.widgets import Static


class TextColorDemo(App):
    CSS_PATH = "tuilwind.min.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("# This is the blue bit!", classes="text-center bold")
        for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            yield Static("This is some example text.", classes=f"text-blue-{i}")
        yield Static("# This is a new section!", classes="text-center bold")
        for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            yield Static("This is some example text.", classes=f"text-gray-{i}")

if __name__ == "__main__":
    app = TextColorDemo()
    app.run()