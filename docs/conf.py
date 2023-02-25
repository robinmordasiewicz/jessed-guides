# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Project information

project = 'Terraform Essentials'
copyright = '2022, Jesse Driskill'
author = 'Jesse Driskill'

release = '0.1'
version = '0.1.0'

html_permalinks = False
html_show_sphinx = False
html_show_sourcelink = False
nitpicky = True

# -- General configuration
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinxcontrib.console'
]

copybutton_prompt_text = "$ "
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True

todo_include_todos = True

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': False,
    'style_external_links': True,
    'titles_only': True
}

html_context = {
    "display_github": True,
    "github_user": "robinmordasiewicz",
    "github_repo": "jessed-guides",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Inlude links on every page
CURDIR = os.path.abspath(os.path.dirname(__file__))
rst_epilog = open(os.path.join(CURDIR, 'rst_epilog.inc'),'r').read()

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
