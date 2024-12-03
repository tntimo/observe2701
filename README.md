# empty-python

## Development

### First time setup

Run
```
poetry config virtualenvs.in-project true
poetry install
```

Ensure proper environment is selected in VSCode: `.venv/bin/python`.

### Use the terminal 

Maybe run if VSCode stubborly refuses to use the proper environment: `poetry shell`

To format, run: `./fmt.sh`

To test, run: `tox`
