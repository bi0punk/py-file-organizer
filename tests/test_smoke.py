import os
import pytest


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md not found"


def test_gitignore_exists():
    assert os.path.isfile(".gitignore"), ".gitignore not found"


def test_pyproject_toml_exists():
    assert os.path.isfile("pyproject.toml"), "pyproject.toml not found"


def test_env_example_exists():
    assert os.path.isfile(".env.example"), ".env.example not found"
