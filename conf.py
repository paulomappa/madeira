# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Estruturas de Madeira'
copyright = '2025, Prof. Paulo Mappa'
author = 'Prof. Paulo Mappa'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ["nbsphinx"]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinxdoc'
#html_theme = 'epub'
#html_theme = 'scrolls'
#html_theme = 'classic'
#html_theme = 'traditional'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
