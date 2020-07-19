# -- Project information -----------------------------------------------------

project = 'UU GRASP Computing manuals'
copyright = '2020, GRASP'
author = 'GRASP'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.githubpages',
              'sphinxemoji.sphinxemoji']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


html_theme = 'sphinx_material'

html_theme_options = {
    'nav_title': 'UU GRASP Computing manuals',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://uugrasp.github.io/UUComputingDocs/',

    # Set the color and the accent color
    'color_primary': 'yellow',
    'color_accent': 'orange',
    'html_minify': True,
    'css_minify': True,
    'master_doc': False,
    'nav_links': [],
    'heroes': {},


    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/UUGRASP/UUComputingDocs',
    'repo_name': 'UUComputingDocs',
    'repo_type': 'github',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 5,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']