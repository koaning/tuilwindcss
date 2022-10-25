import pathlib
import srsly

COLORS = srsly.read_json("data/colors.json")
FRACTIONS = srsly.read_json("data/fractions.json")
BORDER_STYLES = srsly.read_json("data/border_styles.json")

style_css = ""
style_min_css = ""

def write(text):
    global style_css
    global style_min_css
    style_css += text
    style_min_css += text.replace(" ", "").replace("\n", "")


# Add text/background colors 
for k, v in COLORS.items():
    write(f".text-{k} {{\n    color: {v};\n}}\n")
    write(f".bg-{k} {{\n    background: {v};\n}}\n")
    for border in BORDER_STYLES:
        write(f".border-{border}-{k} {{\n    border: {border} {v};\n}}\n")
        write(f".border-left-{border}-{k} {{\n    border-left: {border} {v};\n}}\n")
        write(f".border-right-{border}-{k} {{\n    border-right: {border} {v};\n}}\n")
        write(f".border-top-{border}-{k} {{\n    border-top: {border} {v};\n}}\n")
        write(f".border-bottom-{border}-{k} {{\n    border-bottom: {border} {v};\n}}\n")


for direction in "left|start|center|right|end|justify".split("|"):
    write(f".text-{direction} {{\n    text-align: {direction};\n}}\n")

for pix in range(0, 26):
    # Cases like p-8, m-2
    write(f".m-{pix} {{\n    margin: {pix};\n}}\n")
    write(f".p-{pix} {{\n    padding: {pix};\n}}\n")
    # Cases like px-2, my-1
    write(f".mx-{pix} {{\n    margin-left: {pix};\n    margin-right: {pix};\n}}\n")
    write(f".my-{pix} {{\n    margin-top: {pix};\n    margin-bottom: {pix};\n}}\n")
    write(f".px-{pix} {{\n    padding-left: {pix};\n    padding-right: {pix};\n}}\n")
    write(f".py-{pix} {{\n    padding-top: {pix};\n    padding-bottom: {pix};\n}}\n")
    # Cases like pt-1, mb-1, pl-3, mr-2
    write(f".mt-{pix} {{\n    margin-top: {pix};}}\n")
    write(f".mb-{pix} {{\n    margin-bottom: {pix};}}\n")
    write(f".ml-{pix} {{\n    margin-left: {pix};}}\n")
    write(f".mr-{pix} {{\n    margin-right: {pix};}}\n")
    write(f".pt-{pix} {{\n    padding-top: {pix};}}\n")
    write(f".pb-{pix} {{\n    padding-bottom: {pix};}}\n")
    write(f".pl-{pix} {{\n    padding-left: {pix};}}\n")
    write(f".pr-{pix} {{\n    padding-right: {pix};}}\n")
    # Cases like h-3, w-2
    write(f".h-{pix} {{\n    height: {pix};}}\n")
    write(f".w-{pix} {{\n    width: {pix};}}\n")

# Cases like w-auto, h-auto
write(f".w-auto {{\n    width: auto;}}\n")
write(f".h-auto {{\n    height: auto;}}\n")

# # Cases like w-1/2, h-2/3
# for frac, val in FRACTIONS.items():
#     write(f".h-\{frac} {{\n    width: {val};\n}}\n")
#     write(f".w-\{frac} {{\n    width: {val};\n}}\n")
write(f".w-full {{\n    width: 100%;}}\n")
write(f".h-full {{\n    height: 100%;}}\n")

# Cases like dock-left, dock-bottom
for direction in "top|right|bottom|left".split("|"):
    write(f".dock-{direction} {{\n    dock: {direction};\n}}\n")

# Cases like w-auto, h-auto
for vis in "visible|hidden".split("|"):
    write(f".{vis} {{\n    visibility: {vis};\n}}\n")

# Cases like `bold`
for font in ["bold", "italic", "reverse", "underline", "strike"]:
    write(f".{font} {{\n    text-style: {font};\n}}\n")

pathlib.Path("style.css").write_text(style_css)
pathlib.Path("docs/examples/tutorial/tuilwind.css").write_text(style_css)
pathlib.Path("style.min.css").write_text(style_min_css)
