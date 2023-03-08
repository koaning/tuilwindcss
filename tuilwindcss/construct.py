from pathlib import Path

import srsly
from parse import compile

from tuilwindcss.constants import BORDER_STYLES, COLORS


class CSSWriter:
    """A CSS writer"""

    def __init__(self):
        self._styles = {}
        self._construct()

    def add_style(self, class_name: str, *content: str) -> None:
        """Add a css-class with contents tot the writer"""
        self._styles[class_name] = content

    def _construct(self):
        # Add text/background colors
        for k, v in COLORS.items():
            self.add_style(f".text-{k}", f"color: {v}")
            self.add_style(f".bg-{k}", f"background: {v}")
            for border in BORDER_STYLES:
                self.add_style(f".border-{border}-{k}", f"border: {border} {v}")
                self.add_style(f".border-l-{border}-{k}", f"border-left: {border} {v}")
                self.add_style(f".border-r-{border}-{k}", f"border-right: {border} {v}")
                self.add_style(f".border-t-{border}-{k}", f"border-top: {border} {v}")
                self.add_style(
                    f".border-b-{border}-{k}", f"border-bottom: {border} {v}"
                )
                self.add_style(
                    f".border-x-{border}-{k}",
                    f"border-left: {border} {v}",
                    f"border-right: {border} {v};",
                )
                self.add_style(
                    f".border-y-{border}-{k}",
                    f"border-top: {border} {v}",
                    f"border-bottom: {border} {v};",
                )

        for direction in "left|start|center|right|end|justify".split("|"):
            self.add_style(f".text-{direction}", f"text-align: {direction}")

        for pix in range(0, 26):
            # Cases like p-8, m-2
            self.add_style(f".m-{pix}", f"margin: {pix}")
            self.add_style(f".p-{pix}", f"padding: {pix}")
            # Cases like px-2, my-1
            self.add_style(f".mx-{pix}", f"margin-left: {pix}", f"margin-right: {pix}")
            self.add_style(f".my-{pix}", f"margin-top: {pix}", f"margin-bottom: {pix}")
            self.add_style(
                f".px-{pix}", f"padding-left: {pix}", f"padding-right: {pix}"
            )
            self.add_style(
                f".py-{pix}", f"padding-top: {pix}", f"padding-bottom: {pix}"
            )
            # Cases like pt-1, mb-1, pl-3, mr-2
            self.add_style(f".mt-{pix}", f"margin-top: {pix}")
            self.add_style(f".mb-{pix}", f"margin-bottom: {pix}")
            self.add_style(f".ml-{pix}", f"margin-left: {pix}")
            self.add_style(f".mr-{pix}", f"margin-right: {pix}")
            self.add_style(f".pt-{pix}", f"padding-top: {pix}")
            self.add_style(f".pb-{pix}", f"padding-bottom: {pix}")
            self.add_style(f".pl-{pix}", f"padding-left: {pix}")
            self.add_style(f".pr-{pix}", f"padding-right: {pix}")
            # Cases like h-3, w-2
            self.add_style(f".h-{pix}", f"height: {pix}")
            self.add_style(f".w-{pix}", f"width: {pix}")

        # Cases like w-auto, h-auto
        self.add_style(".w-auto", "width: auto")
        self.add_style(".h-auto", "height: auto")

        # # Cases like w-1/2, h-2/3
        # for frac, val in FRACTIONS.items():
        #     self.add_style(f".h-\{frac} {{\n    width: {val};\n}}\n")
        #     self.add_style(f".w-\{frac} {{\n    width: {val};\n}}\n")
        self.add_style(".w-full", "width: 100%")
        self.add_style(".h-full", "height: 100%")

        # Cases like dock-left, dock-bottom
        for direction in "top|right|bottom|left".split("|"):
            self.add_style(f".dock-{direction}", f"dock: {direction}")

        # Cases like w-auto, h-auto
        for vis in "visible|hidden".split("|"):
            self.add_style(f".{vis}", f"visibility: {vis}")

        # Cases like `bold`
        for font in ["bold", "italic", "reverse", "underline", "strike"]:
            self.add_style(f".{font}", f"text-style: {font}")

    def write_json(self, path: Path):
        """Write the state as a json file."""
        srsly.write_json(path, self._styles)

    def iter_styles(self, minified=True, classes=None):
        """Iterate over all the generated styles"""
        if not classes:
            classes = self._styles.keys()
        for k, v in self._styles.items():
            if k in classes:
                if minified:
                    v = ";".join(v)
                    yield f"{k}" + "{" + f"{v}" + "}"
                else:
                    if len(v) > 1:
                        v = list(v)
                        v[0] = "    " + v[0]
                    v = ";\n    ".join(v) if len(v) > 1 else f"    {v[0]};"
                    yield f"{k}" + "{\n" + f"{v}" + "\n}\n"

    def fetch_classes(self, path: Path):
        """Fetches classes from a py file."""
        text = path.read_text()

        found_classes = set()
        for query in [compile('classes="{classes}"'), compile("classes='{classes}'")]:
            for e in query.findall(text):
                for css_class in e.named["classes"].split(" "):
                    found_classes.add(f".{css_class}")
        return found_classes

    def write_css(self, path: Path, minified=False, src_file=None):
        """Write into .css file"""
        classes = set()
        if src_file:
            classes.update(self.fetch_classes(path=Path(src_file)))

        with open(path, "w") as f:
            for style in self.iter_styles(minified=minified, classes=classes):
                f.write(style)


if __name__ == "__main__":
    writer = CSSWriter()
    print(writer.fetch_classes(Path("docs/examples/bg.py")))
