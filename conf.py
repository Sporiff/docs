# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'helloSystem'
copyright = '2020-2021, probono'
author = 'probono'

# The full version, including alpha/beta/rc tags
release = '' # 'experimental' # We don't want this in the HTML title


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Auto-generate section labels.
    'sphinx.ext.autosectionlabel',
    'myst_parser'
]

# Enable code fences to be written with colons for extra control

myst_enable_extensions = ["colon_fence"]

master_doc = 'index'

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# specify a fallback value for local builds
# FIXME: find a way to use relative URLs instead of absolute URLs to better support URLs
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "helloSystem/docs")
GITHUB_REPO_OWNER, GITHUB_REPO_NAME = GITHUB_REPOSITORY.split("/")[0:2]

# Display "Edit on GitHub"
html_context = {
  'display_github': True,
  'github_user': GITHUB_REPO_OWNER,
  'github_repo': GITHUB_REPO_NAME,
  'github_version': 'main/',
}

html_show_copyright = False
html_show_sphinx = False
html_logo = "_static/hello_logo.png"

epub_cover = ('./_static/hello_logo.png', 'epub-cover.html')
epub_tocscope = "includehidden"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'theme_overrides.css',
]

github_doc_root = 'https://' + GITHUB_REPO_OWNER + '.github.io/' + GITHUB_REPO_NAME + '/'
