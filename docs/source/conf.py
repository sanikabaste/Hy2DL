# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hy2DL'
copyright = '2024, Sanika Baste'
author = 'Sanika Baste'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # autodocument
    'sphinx.ext.napoleon',  # google and numpy doc string support
    'sphinx.ext.mathjax',  # latex rendering of equations using MathJax
    'nbsphinx',  # for direct embedding of jupyter notebooks into sphinx docs
    'nbsphinx_link'  # to be able to include notebooks from outside of the docs folder
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints', '_build']

templates_path = ['_templates']
exclude_patterns = []

# Allows to build the docs with a minimal environment without warnings about missing packages
autodoc_mock_imports = [
    'matplotlib',
    'numba',
    'pandas',
    'ruamel',
    'scipy',
    'tqdm',
    'xarray',
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
