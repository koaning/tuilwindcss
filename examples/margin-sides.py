from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical


class PaddingDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Vertical(
            Static("mt-2", classes="mt-2 bg-gray-200 border-round-gray-600 text-gray-800"),
            Static("mb-2", classes="mb-2 bg-gray-300 border-round-gray-600 text-gray-800"),
            Static("ml-2", classes="ml-2 bg-gray-200 border-round-gray-600 text-gray-800"),
            Static("mr-2", classes="mr-2 bg-gray-300 border-round-gray-600 text-gray-800"),
            Static("mx-2", classes="mx-2 bg-gray-200 border-round-gray-600 text-gray-800"),
            Static("my-2", classes="my-2 bg-gray-300 border-round-gray-600 text-gray-800"),
            classes="bg-gray-400"
        )

if __name__ == "__main__":
    app = PaddingDemo()
    app.run()