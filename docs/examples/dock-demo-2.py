from textual.app import App, ComposeResult
from textual.widgets import Static


class DockDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("top", classes="dock-top h-2 bg-green-600 w-full text-center")
        yield Static("bottom", classes="dock-bottom h-4 bg-blue-600 w-full text-center")

if __name__ == "__main__":
    app = DockDemo()
    app.run()