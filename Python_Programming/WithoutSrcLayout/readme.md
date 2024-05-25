`A demo project of a python project file structure without src layout`

## WithoutSrcLayout/
        |--bin/
        |--tests/
            |--test_extractor.py
            |--test_transformer.py
            |--test_loader.py
        |--docs/
        |--withoutsrclayoutV1_0_0/
            |--__init__.py
            |--extractor.py
            |--transformer.py
            |--loader.py
        |--withoutsrclayoutV3_1_3/
        |--readme.md
        |--requirements.txt
        |--setup.py

** WithoutSrcLayout/ **: The root directory of the project.

## Pytest Configuration
We can use the **toml** file to configure pytest. The file name should be **pytest.ini** or **tox.ini**. The content of the file is as follows:
```toml
[pytest]
addopts = -v
testpaths = tests
```
Anyway, we may have these commands one after another...
    - `python -m pytest tests/`
    - `pytest -s -v` or
    - `pytest`