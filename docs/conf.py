# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sequencing-docker-stacks"
copyright = "2025, Fabian Rost"
author = "Fabian Rost"

version = "latest"
release = "latest"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# The file above was generated using sphinx 8.1.3 with this command:
# sphinx-quickstart --project "docker-stacks" --author "Project Jupyter" -v "latest" -r "latest" -l en --no-sep --no-makefile --no-batchfile
# These are custom options for this project

html_theme = "sphinx_book_theme"
html_title = "Sequencing Docker Stacks documentation"
html_logo = "_static/jupyter-logo.svg"
html_theme_options = {
    "logo": {
        "text": html_title,
    },
    "navigation_with_keys": False,
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": "https://github.com/fbnrst/sequencing-docker-stacks",
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
}
html_last_updated_fmt = "%Y-%m-%d"

extensions = ["myst_parser", "sphinx_copybutton", "sphinx_last_updated_by_git"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
pygments_style = "sphinx"

# MyST configuration reference: https://myst-parser.readthedocs.io/en/latest/configuration.html
myst_heading_anchors = 3

linkcheck_ignore = [
    r".*github\.com.*#",  # javascript based anchors
    r"http://127\.0\.0\.1:.*",  # various examples
    r"https://mybinder\.org/v2/gh/.*",  # lots of 500 errors
    r"https://packages\.ubuntu\.com/search\?keywords=openjdk",  # frequent read timeouts
    r"https://anaconda\.org\/conda-forge",  # frequent read timeouts
]

linkcheck_allowed_redirects = {
    r"https://results\.pre-commit\.ci/latest/github/fbnrst/sequencing-docker-stacks/main": r"https://results\.pre-commit\.ci/run/github/.*",  # Latest main CI build
    r"https://github\.com/fbnrst/sequencing-docker-stacks/issues/new.*": r"https://github\.com/login.*",  # GitHub wants user to be logon to use this features
    r"https://github\.com/orgs/jupyter/teams/docker-image-maintainers/members": r"https://github\.com/login.*",
}
