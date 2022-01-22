#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests using pytest."""


# pylint: disable=too-many-arguments

import pytest

non_empty_root_dirs_list = ["data", "reports"]
non_empty_root_dirs_sub_dirs_list = [
    ["external", "interim", "processed", "raw"],
    ["figures"],
]
empty_root_dirs_list = ["executed_notebooks", "models", "references"]
root_dir_files_list = [
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
module_files_list = ["__init__.py", "utils.py"]
module_data_files_list = [
    "__init__.py",
    ".gitkeep",
    "load_data.py",
    "make_dataset.py",
    "process_data.py",
]
module_features_files_list = ["__init__.py", ".gitkeep", "build_features.py"]
module_models_files_list = [
    "__init__.py",
    ".gitkeep",
    "predict_model.py",
    "train_model.py",
]
module_visualization_files_list = ["__init__.py", ".gitkeep", "visualize.py"]


@pytest.mark.parametrize("repo_name", ["name-of-github-repository"])
@pytest.mark.parametrize("root_dir_files", [root_dir_files_list])
def test_project_generation(bake_custom_project, repo_name, root_dir_files):
    """Test generation and rendering of template."""
    result = bake_custom_project
    assert result.exit_code == 0
    assert result.exception is None
    proj_dir = result.project_path
    assert proj_dir.name == repo_name
    assert proj_dir.is_dir
    for file in root_dir_files:
        file = proj_dir.joinpath(file)
        assert file.is_file


@pytest.mark.parametrize("empty_root_dirs", [empty_root_dirs_list])
def test_empty_root_folder_generation(bake_custom_project, empty_root_dirs):
    """Test generation and rendering of non-nested subdirs in template."""
    result = bake_custom_project
    proj_dir = result.project_path
    for empty_root_dir in empty_root_dirs:
        proj_empty_root_dir = proj_dir.joinpath(empty_root_dir)
        assert proj_empty_root_dir.is_dir
        for file in [".gitkeep"]:
            file = proj_empty_root_dir.joinpath(file)
            assert file.is_file


@pytest.mark.parametrize("non_empty_root_dirs", [non_empty_root_dirs_list])
@pytest.mark.parametrize(
    "non_empty_root_dirs_sub_dirs", [non_empty_root_dirs_sub_dirs_list]
)
def test_non_empty_root_folder_generation(
    bake_custom_project, non_empty_root_dirs, non_empty_root_dirs_sub_dirs
):
    """Test generation and rendering of nested subdirs template."""
    result = bake_custom_project
    proj_dir = result.project_path
    for non_empty_root_dir, non_empty_root_dirs_sub_dir in zip(
        non_empty_root_dirs, non_empty_root_dirs_sub_dirs
    ):
        proj_non_empty_root_dir = proj_dir.joinpath(non_empty_root_dir)
        assert proj_non_empty_root_dir.is_dir
        for sub_dir in non_empty_root_dirs_sub_dir:
            sub_dir = proj_non_empty_root_dir.joinpath(sub_dir)
            assert sub_dir.is_dir
            for file in [".gitkeep"]:
                file = sub_dir.joinpath(file)
                assert file.is_file


@pytest.mark.parametrize("module_files", [module_files_list])
@pytest.mark.parametrize("module_data_files", [module_data_files_list])
@pytest.mark.parametrize("module_features_files", [module_features_files_list])
@pytest.mark.parametrize("module_models_files", [module_models_files_list])
@pytest.mark.parametrize(
    "module_visualization_files", [module_visualization_files_list]
)
def test_module_folder_generation(
    bake_custom_project,
    module_files,
    module_data_files,
    module_features_files,
    module_models_files,
    module_visualization_files,
):
    """Test generation and rendering of module contents in template."""
    result = bake_custom_project
    proj_dir = result.project_path
    module_dir = proj_dir.joinpath("name-of-python-module")
    assert module_dir.is_dir
    for file in module_files:
        file = module_dir.joinpath(file)
        assert file.is_file

    for folder, folder_files_list in zip(
        ["data", "features", "models", "visualization"],
        [
            module_data_files,
            module_features_files,
            module_models_files,
            module_visualization_files,
        ],
    ):
        module_sub_dir = module_dir.joinpath(folder)
        assert module_sub_dir.is_dir
        for file in folder_files_list:
            file = module_sub_dir.joinpath(file)
            assert file.is_file
