import yaml
import subprocess
import os
from pathlib import Path

class YAMLProcessor:
    def __init__(self, yaml_file):
        self.config = self.load_yaml(yaml_file)
        self.setup_directories()

    def load_yaml(self, file_path):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def setup_directories(self):
        dirs = [
            self.config['latex']['output_dir'],
            self.config['latex']['templates_dir']
        ]
        for d in dirs:
            Path(d).mkdir(parents=True, exist_ok=True)

    def generate_latex(self):
        template = f"""
\\documentclass{{article}}
{self.generate_packages()}

\\begin{{document}}
\\title{{{self.config['document']['title']}}}
\\author{{{self.config['document']['author']}}}
\\maketitle

\\section{{Definitions}}
A Hamiltonian system is represented by a function $H: M \\to \\mathbb{{R}}$

\\end{{document}}
"""
        with open('main.tex', 'w') as f:
            f.write(template)

    def generate_packages(self):
        return '\n'.join([f'\\usepackage{{{pkg}}}' 
                         for pkg in self.config['latex']['packages']])

    def compile_latex(self):
        cmd = [
            self.config['latex']['compiler'],
            '-output-directory',
            self.config['latex']['output_dir'],
            'main.tex'
        ]
        subprocess.run(cmd, check=True)

    def run(self):
        self.generate_latex()
        self.compile_latex()

if __name__ == '__main__':
    processor = YAMLProcessor('latex-config.yaml')
    processor.run()
