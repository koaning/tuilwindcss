from pathlib import Path 
from radicli import Arg, Radicli
from parse import compile


cli = Radicli(help="Tuiwindcss: Tailwind for Textual.")



@cli.command(
    "reduce",
    path=Arg(help="path to .py file that contains textual app"),
)
def text(path: Path):
    text = path.read_text()

    for query in ['classes="{classes}"', "classes='{classes}'"]:
        p = compile(query)
        found_classes = set()
        for e in p.findall(text):
            for css_class in e.named['classes'].split(" "):
                found_classes.add(css_class)
    return found_classes


if __name__ == "__main__":
    cli.run()
