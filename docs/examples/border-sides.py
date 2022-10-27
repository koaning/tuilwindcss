from textual.app import App, ComposeResult
from textual.widgets import Static


class BorderSidesDemo(App):
    CSS_PATH = "tuilwind.css"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Static("first",  classes="p-1 text-center bg-red-300    border-t-heavy-red-600")
        yield Static("second", classes="p-1 text-center bg-green-300  border-l-heavy-green-600")
        yield Static("third",  classes="p-1 text-center bg-blue-300   border-r-heavy-blue-600")
        yield Static("fourth", classes="p-1 text-center bg-yellow-300 border-b-heavy-yellow-600")
        yield Static("fifth",  classes="p-1 text-center bg-orange-300 border-x-heavy-orange-600")
        yield Static("sixth",  classes="p-1 text-center bg-cyan-300   border-y-heavy-cyan-600")

if __name__ == "__main__":
    app = BorderSidesDemo()
    app.run()