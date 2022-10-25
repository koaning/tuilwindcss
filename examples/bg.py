from textual.app import App, ComposeResult
from textual.widgets import Static


class BackgroundColorDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            yield Static(f"bg-blue-{i}", classes=f"bg-blue-{i}")
        for i in reversed([100, 200, 300, 400, 500, 600, 700, 800, 900]):
            yield Static(f"bg-blue-{i}", classes=f"bg-blue-{i}")
        

if __name__ == "__main__":
    app = BackgroundColorDemo()
    app.run()