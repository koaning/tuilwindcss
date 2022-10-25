from textual.app import App, ComposeResult
from textual.widgets import Static


class PaddingDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("pt-2", classes="pt-2 bg-blue-400")
        yield Static("pb-2", classes="pb-2 bg-blue-500")
        yield Static("pl-2", classes="pl-2 bg-blue-600")
        yield Static("pr-2", classes="pr-2 bg-blue-700")
        yield Static("px-2", classes="px-2 bg-yellow-400")
        yield Static("py-2", classes="py-2 bg-yellow-600")

if __name__ == "__main__":
    app = PaddingDemo()
    app.run()