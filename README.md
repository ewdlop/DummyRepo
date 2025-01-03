LaTeX compilers translate LaTeX source code into formatted documents (usually PDF). Main functions:

1. Text processing/formatting
2. Mathematical equation rendering
3. Bibliography management
4. Cross-referencing
5. Figure/table placement

Common LaTeX compilers:
- pdflatex: Most common, creates PDF directly
- xelatex: Better Unicode/font support
- lualatex: Modern engine with Lua scripting

For the Hamiltonian systems example, pdflatex would process:
```latex
$H: M \to \mathbb{R}$
```
into properly formatted mathematical notation in the output PDF.

Usage:
```bash
pip install pyyaml
python yaml_processor.py
```

The program reads YAML config, generates LaTeX, and compiles to PDF. Sample YAML:

```yaml
latex:
  compiler: pdflatex
  output_dir: ./build
  templates_dir: ./templates
  packages:
    - amsmath
    - amssymb

document:
  title: "Hamiltonian Systems"
  author: "Author Name"
```
