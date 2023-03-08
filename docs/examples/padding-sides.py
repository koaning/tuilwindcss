from textual.app import App, ComposeResult
from textual.widgets import Static


class PaddingDemo(App):
    CSS_PATH = "tuilwind.min.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("pt-2", classes="pt-2 bg-gray-200 border-round-gray-600 text-gray-700")
        yield Static("pb-2", classes="pb-2 bg-gray-300 border-round-gray-600 text-gray-700")
        yield Static("pl-2", classes="pl-2 bg-gray-200 border-round-gray-600 text-gray-700")
        yield Static("pr-2", classes="pr-2 bg-gray-300 border-round-gray-600 text-gray-700")
        yield Static("px-2", classes="px-2 bg-gray-200 border-round-gray-600 text-gray-700")
        yield Static("py-2", classes="py-2 bg-gray-300 border-round-gray-600 text-gray-700")

if __name__ == "__main__":
    app = PaddingDemo()
    app.run()