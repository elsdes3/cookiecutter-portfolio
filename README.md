# Minimal Datascience Project Template

![CI](https://github.com/elsdes3/cookiecutter-portfolio/workflows/CI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/mit)
![OpenSource](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![prs-welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)

## [Table of Contents](#table-of-contents)
1. [About](#about)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Notes](#notes)

## [About](#about)
Create a minimal folder structure for a datascience project.

## [Requirements](#requirements)
1. Install the Python packages
   - `cookiecutter`
   - `tox`

   using
   ```bash
   pip install cookiecutter tox
   ```
2. Install `Make` ([link](https://www.gnu.org/software/make/))

## [Usage](#usage)
1. Clone this repo
   ```bash
   cd Downloads
   git clone https://github.com/elsdes3/cookiecutter-portfolio.git
   ```
2. Set your prefered values for **all** variables in
   - `cookiecutter-portfolio/cookiecutter-project/config.yaml`

   Note that every variable present in `cookiecutter.json` must also be present in `config.yaml`.
3. Change into the project directory
   ```bash
   cd cookiecutter-portfolio
   ```
4. Create the templated project, run code formatting checks and run the starter notebook (`0_get_data.ipynb`) programmatically using
   ```bash
   make build
   ```

## [Notes](#notes)
1. This template a customized version of the `cookiecutter-datascience` template ([v2](https://github.com/drivendata/cookiecutter-data-science/tree/v2)).
2. The Python library `tox` is used for managing Python virtual environments. See these links ([1](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/), [2](https://towardsdatascience.com/exclusive-how-to-deploy-your-first-machine-learning-models-bf0a2109e522)) for details about how `tox` can be used to do this for a machine learning project.
