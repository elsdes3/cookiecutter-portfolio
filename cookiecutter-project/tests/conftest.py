#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Define Pytest fixtures to inject into tests."""


import json

import pytest
import testing_utils.ccfebd_test_utilities as cu

# pylint: disable=too-many-locals,redefined-outer-name


@pytest.fixture
def custom_template(tmpdir):
    """Generate a template with cookiecutter, in order to run tests."""
    template = tmpdir.ensure("cookiecutter-template", dir=True)
    json_data = cu.generate_json_and_cfg_contents("cookiecutter.json")

    # ========= Populate cookiecutter.json =========
    template.join("cookiecutter.json").write(json.dumps(json_data))

    # ========= Create project folder =========
    repo_dir = template.ensure("{{cookiecutter.repo_name}}", dir=True)

    # ========= Prepare individual files in project root dir =========
    repo_dir.join("README.md").write("{{cookiecutter.repo_name}}")
    # Ensure files exist, without adding contents
    blank_files = [
        ".gitignore",
        ".pre-commit-config.yaml",
        "environment.yml",
        "LICENSE",
        "Makefile",
        "papermill_runner.py",
        "README.md",
        "requirements.txt",
        "setup.py",
        "tox.ini",
    ]
    for blank_file in blank_files:
        repo_dir.join(blank_file).ensure(file=True)
    # ========= Prepare files in the custom Python package dir =========
    module_dir = repo_dir.join("{{cookiecutter.package_name}}", dir=True)
    module_files_list = ["__init__.py", "utils.py"]
    for module_file in module_files_list:
        module_dir.join(module_file).ensure(file=True)
    # ========= Prepare files in modules (sub dirs in package dir) =========
    data_module_files_list = [
        "__init__.py",
        ".gitkeep",
        "load_data.py",
        "make_dataset.py",
        "process_data.py",
    ]
    features_module_files_list = [
        "__init__.py",
        ".gitkeep",
        "build_features.py",
    ]
    models_module_files_list = [
        "__init__.py",
        ".gitkeep",
        "predict_model.py",
        "train_model.py",
    ]
    visualization_module_files_list = [
        "__init__.py",
        ".gitkeep",
        "visualize.py",
    ]
    for folder, folder_files_list in zip(
        ["data", "features", "models", "visualization"],
        [
            data_module_files_list,
            features_module_files_list,
            models_module_files_list,
            visualization_module_files_list,
        ],
    ):
        module_sub_dir = module_dir.join(folder, dir=True)
        for module_sub_dir_file in folder_files_list:
            module_sub_dir.join(module_sub_dir_file).ensure(file=True)
    return template


@pytest.fixture
def bake_custom_project(cookies, custom_template):
    """Generate custom cookiecutter project template."""
    result = cookies.bake(template=str(custom_template))
    return result
