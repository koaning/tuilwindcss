import pathlib
import srsly

COLORS = srsly.read_json("data/colors.json")

for k, v in COLORS.items():
    COLORS[k] = v.replace(" ", ",")

srsly.write_json("data/colors.json", COLORS)

style_css = ""
style_min_css = ""

def write(text):
    global style_css
    global style_min_css
    style_css += text
    style_min_css += text.replace(" ", "").replace("\n", "")


# Add text/background colors 
for k, v in COLORS.items():
    write(f".text-{k} {{\n    color: {v}\n}}\n")
    write(f".bg-{k} {{\n    background: {v}\n}}\n")

pathlib.Path("style.css").write_text(style_css)
pathlib.Path("style.min.css").write_text(style_min_css)
