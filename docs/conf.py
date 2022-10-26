import sys
import pathlib
sys.path.append(str(pathlib.Path('..').resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'jertl'
copyright = '2022, Ray Pelletier'
author = 'Ray Pelletier'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autodoc_member_order = 'bysource'

# Napoleon settings
napoleon_include_init_with_doc = True
napoleon_type_aliases = None


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "nature"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "sidebarwidth": 300
}
html_static_path = ['_static']
