# [Usage](#usage)

## [Table of Contents](#table-of-contents)

- [Requirements](#requirements)
- [Generate project from template](#generate-project-from-template)

## [Requirements](#requirements)

Install [Python](https://www.python.org/) ver. 3.9 or higher and install the Python libraries
- [`cookiecutter`](https://github.com/audreyr/cookiecutter)
- [`tox`](https://tox.wiki/en/latest/)

## [Generate project from template](#generate-project-from-template)

In order to create a project using this template
- [use `git` to clone](https://linux.die.net/man/1/git-clone) this project locally
  ```bash
  git clone https://github.com/elsdes3/cookiecutter-portfolio.git
  ```
- change `config.yaml` and `cookiecutter.json` as required
  - the parameters in `config.yaml` and `cookiecutter.json` must be the same but only the values from `config.yaml` will be used
- generate a templated project using
  ```bash
  cd cookiecutter-portfolio
  make build
  ```

This will auto-generate a new boilerplate project from this template by taking all default values specified in `config.yaml` and generating a template without any manual prompts and user input.
