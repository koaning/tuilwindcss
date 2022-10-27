---
hide:
  - navigation
---   
# tuilwindcss

You can find a list of tuilwindcss demos below

## Tailwind Compatible Classes 

### Background Color

```python title="Background Color Demo"
--8<-- "docs/examples/bg.py"
```

```{.textual path="docs/examples/bg.py"}
```

### Padding

#### Simple Padding

```python title="Padding Demo"
--8<-- "docs/examples/padding.py"
```

```{.textual path="docs/examples/padding.py"}
```

#### Padding Direction

You can also be specific in the direction of the padding. So you can specify: 

- `pt-1` to add 1 padding to the **top**
- `pb-1` to add 1 padding to the **bottom**
- `pl-1` to add 1 padding to the **left**
- `pr-1` to add 1 padding to the **right**
- `px-1` to add 1 padding to **horizontally**
- `py-1` to add 1 padding to **vertically**

```python title="Padding Direction Demo"
--8<-- "docs/examples/padding-sides.py"
```

```{.textual path="docs/examples/padding-sides.py"}
```

### Margin

#### Simple Margin


```python title="Padding Demo"
--8<-- "docs/examples/margin.py"
```

```{.textual path="docs/examples/margin.py"}
```

#### Margin Direction

You can also be specific in the direction of the padding. So you can specify: 

- `mt-1` to add 1 padding to the **top**
- `mb-1` to add 1 padding to the **bottom**
- `ml-1` to add 1 padding to the **left**
- `mr-1` to add 1 padding to the **right**
- `mx-1` to add 1 padding to **horizontally**
- `my-1` to add 1 padding to **vertically**

```python title="Padding Direction Demo"
--8<-- "docs/examples/margin-sides.py"
```

```{.textual path="docs/examples/margin-sides.py"}
```


### Text 

#### Text Color

```python title="Text Color Demo"
--8<-- "docs/examples/text-color.py"
```

```{.textual path="docs/examples/text-color.py"}
```

#### Text Style

```python title="Text Style Demo"
--8<-- "docs/examples/text-style.py"
```

```{.textual path="docs/examples/text-style.py"}
```

#### Text Alignment

```python title="Text Alignment Demo"
--8<-- "docs/examples/text-alignment.py"
```

```{.textual path="docs/examples/text-alignment.py"}
```

## Tailwind Inconsistent Classes

### Border

Borders in CSS allow you to define the border-width seperately from the border-color. Textual doesn't do this, which is why the class names are much longer.

### Base Border

```python title="Border Demo"
--8<-- "docs/examples/border-base.py"
```

```{.textual path="docs/examples/border-base.py"}
```

### Border Direction

You can also be specific in the direction of the border. So you can specify: 

- `border-t-1-<COLOR>` to add a border to the **top**
- `border-b-1-<COLOR>` to add a border to the **bottom**
- `border-l-1-<COLOR>` to add a border to the **left**
- `border-r-1-<COLOR>` to add a border to the **right**
- `border-x-1-<COLOR>` to add a border to **horizontally**
- `border-y-1-<COLOR>` to add a border to **vertically**


```python title="Border Demo"
--8<-- "docs/examples/border-sides.py"
```

```{.textual path="docs/examples/border-sides.py"}
```

## Textual Specific Classes

We try to mimic tailwindcss as much as possible. But there are a few places where textual has it's own definitions. For these
instances we try to offer classes that follow the spirit of tailwind. 

### Dock 

### Dock Left/Right

```python title="Dock Demo"
--8<-- "docs/examples/dock-demo-1.py"
```

```{.textual path="docs/examples/dock-demo-1.py"}
```

### Dock Top/Bottom

```python title="Dock Demo"
--8<-- "docs/examples/dock-demo-2.py"
```

```{.textual path="docs/examples/dock-demo-2.py"}
```