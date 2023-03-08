from textual.app import App, ComposeResult
from textual.widgets import Static


class DockDemo(App):
    CSS_PATH = "tuilwind.min.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("left",  classes="dock-left  h-full bg-red-600    w-15")
        yield Static("right", classes="dock-right h-full bg-yellow-600 w-20")

if __name__ == "__main__":
    app = DockDemo()
    app.run()