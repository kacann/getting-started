# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Get Started with pyATS'
copyright = '2019, Cisco Systems Inc.'
author = 'Cisco Systems Inc.'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel', 'sphinxcontrib.spelling',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for PDF output -------------------------------------------------
#
pdf_documents = [('index')]



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/theme.css',
    'css/custom.css',
]
html_js_files = [
    'js/custom.js',
]
html_theme_path = ["_themes", ]
html_show_sourcelink = False
html_copy_source = False
rst_prolog = """
.. |pyATS| replace:: pyATS
.. |pyATSbold| replace:: **pyATS**
.. |library| replace:: pyATS Library
.. |librarybold| replace:: **pyATS Library**
.. |geniecmd| replace:: genie
.. |genieprfx| replace:: genie
.. |getstartedguide| replace:: *Get Started with pyATS Guide*
.. |windows_reg| unicode:: Windows U+00AE
.. |ubuntu_reg| unicode:: Ubuntu U+00AE
.. |linux_reg| unicode:: Linux U+00AE
.. |mac_reg| unicode:: Mac U+00AE
.. |docker_reg| unicode:: Docker U+00AE
.. |github_reg| unicode:: GitHub U+00AE
.. |python_reg| unicode:: Python U+00AE
.. |parser_site| replace:: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers
.. |br| raw:: html
  <br />
.. |line6| raw:: html
  <p style="border:1px solid #e1e4e5;"><code style="border:none; color:#e74c3c;">print('Slot 1 serial number:' </br>&nbsp;+ p1['name']['Slot 1']['serial_number'])</code></p>
.. raw:: html
    <style>
    .question {background-color: yellow; font-weight:bold; padding: .25em;}
    .monospace {font-family: monospace; color: #404040; font-size: 14px;}
    .border {border: 1px #404040;}
    </style>
.. role:: question
.. role:: monospace
.. role::  border
"""
