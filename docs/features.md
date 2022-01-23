# [Template features](#template-features)

`cookiecutter-portfolio` creates a
- Python project directory with a structure chosen to support a datascience project
- starter notebooks that use the created project's directory structure to import [Python modules](https://docs.python.org/3/tutorial/modules.html)
- Continuous Integration (CI) conifgurations to execute analysis notebooks and perform code-formatting checks on the supporting Python modules, using Github Actions

It is based on [`cookiecutter-data-science`](https://github.com/drivendata/cookiecutter-data-science/blob/master/README.md#the-resulting-directory-structure), so it's output generally resembles the directory structure produced by that template, with some exceptions and additional features that try to support the [Python-based best practices](https://python.g-node.org/python-summerschool-2011/_media/materials/best_practices/haenel-best-practices-2011-09-standrews.pdf) for the [software development life cycle](https://www.devteam.space/blog/what-is-software-development-lifecycle-and-what-you-plan-for/#5).

## [Features](#features)

Below are the features offered by this template, in addition to `cookiecutter-data-science`
1. Creates a [`pre-commit` git hook](https://githooks.com/) configuration file to enforce code formatting in standalone Python modules and non-Python files, such as
   - [`black`](https://black.readthedocs.io/en/stable/)
   - [`flake8`](https://flake8.pycqa.org/en/latest/)
   - [maximum line length](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
   - [blank lines surrounding functions](https://www.python.org/dev/peps/pep-0008/#blank-lines)
   - Python module imports on separate lines ([1](https://www.python.org/dev/peps/pep-0008/#imports), [2](http://google.github.io/styleguide/pyguide.html#313-imports-formatting))
   - [use of spaces over tabs](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
   - sorting Python imports
2. Demonstrates sample analysis workflows in notebooks to show how Python functions can be abstracted in modules
3. Provide configuration files to run analysis notebooks as part of Continuous Integration (CI) system for Github-based project
   - this CI workflow will automatically run when the templated project is pushed to Github
4. Embeds badges, in `README.md`, with links to explore notebooks or projects through cloud-based computation environments
   - [Binder](https://mybinder.readthedocs.io/en/latest/index.html)
   - [Colaboratory by Google Research](https://research.google.com/colaboratory/faq.html)

   as well as creating notebook links using [NBViewer](https://nbviewer.jupyter.org/faq#what-is-nbviewerjupyterorg).
5. Provides overhead to programmatically run notebooks locally, with script to accept user input for notebooks, from Python scripts, using the Python [`papermill`](https://papermill.readthedocs.io/en/latest/) library (see [1](https://blog.goodaudience.com/inside-netflixs-notebook-driven-architecture-aedded32145e))
6. Places [`.PHONY` targets](https://ftp.gnu.org/old-gnu/Manuals/make-3.79.1/html_node/make_34.html) in `Makefile` for convenience in running
   - code-formatting checks
   - analysis notebooks (programmatically)
