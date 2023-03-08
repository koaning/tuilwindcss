from pathlib import Path

from radicli import Arg, Radicli

from .construct import CSSWriter

cli = Radicli(help="Tuiwindcss: Tailwind for Textual.")


@cli.command(
    "construct",
    path=Arg(help="path to .py file that contains textual app"),
    minified=Arg("--minified", "-m", help="minify the css file"),
    pyfile=Arg("--pyfile", "-p", help="Python file with class definitions"),
)
def construct(path: Path, minified: bool = False, pyfile: Path = None):
    CSSWriter().write_css(path=path, minified=minified, src_file=pyfile)


if __name__ == "__main__":
    cli.run()
