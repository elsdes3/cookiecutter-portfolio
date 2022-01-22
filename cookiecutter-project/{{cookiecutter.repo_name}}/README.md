# {{cookiecutter.repo_name}}

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }})
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/master/0_get_data.ipynb)
![CI](https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/actions/workflows/main.yml/badge.svg)
[![License: {{ cookiecutter.open_source_license }}](https://img.shields.io/badge/License-{{ cookiecutter.open_source_license }}-brightgreen.svg)](https://opensource.org/licenses/{{ cookiecutter.open_source_license }})
![OpenSource](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![prs-welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![pyup](https://pyup.io/repos/github/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/shield.svg)

## [Table of Contents](#table-of-contents)
1. [About](#about)
   * [Overview](#overview)
2. [Usage](#usage)
3. [Notebooks](#notebooks)
4. [Project Organization](#project-organization)

## [About](#about)

### [Overview](#overview)
An overview of the project should go here.

## [Usage](#usage)
1. Create a Python virtual environment to run Jupyter notebooks, install required Python packages and start a notebook server
   ```bash
   make build
   ```
2. Perform pre-commit code checks (before [commiting any new code to git](https://git-scm.com/docs/git-commit)) in a Python virtual environment
   ```bash
   make precommit
   ```
4. Programmatically run notebooks in a Python virtual environment using the Python libraries in `requirements.txt` and `papermill` ([link](https://papermill.readthedocs.io/en/latest/))
   ```bash
   make ci
   ```

## [Notebooks](#notebooks)
1. `01_get_data.ipynb` ([view](https://nbviewer.org/github/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/blob/main/01_get_data.ipynb))
   - retrieve the raw data
2. `02_process_data.ipynb` ([view](https://nbviewer.org/github/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/blob/main/02_process_data.ipynb))
   - process the raw data

### [Project Organization](#project-organization)

    ├── LICENSE
    ├── .gitignore                    <- files and folders to be ignored by version control system
    ├── .pre-commit-config.yaml       <- configuration file for pre-commit hooks
    ├── .github
    │   ├── workflows
    │       └── main.yml              <- configuration file for CI build on Github Actions
    ├── Makefile                      <- Makefile with commands like `make data` or `make train`
    ├── README.md                     <- The top-level README for developers using this project.
    ├── data
    │   ├── external                  <- Data from third party sources.
    │   ├── interim                   <- Intermediate data that has been transformed.
    │   ├── processed                 <- The final, canonical data sets for modeling.
    │   └── raw                       <- The original, immutable data dump.
    │
    ├── models                        <- Trained and serialized models, model predictions, or model summaries
    │
    ├── references                    <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── executed_notebooks            <- Destination for notebooks that are executed programmatically.
    │
    ├── reports                       <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                   <- Generated graphics and figures to be used in reporting
    ├── *.ipynb                       <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                    and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt              <- The requirements file for reproducing the analysis environment, e.g.
    │                                    generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                      <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                           <- Source code for use in this project.
    │   ├── __init__.py               <- Makes src a Python module
    │   │
    │   ├── data                      <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features                  <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models                    <- Scripts to train models and then use trained models to make
    │   │   │                            predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization             <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── papermill_runner.py           <- Python functions that execute notebooks.
    └── tox.ini                       <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
