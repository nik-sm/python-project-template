## Setup and usage
Requires python with venv. On Ubuntu:
```shell
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-venv python3.11-dev
```

Use `make` to create python environment, install dependencies, and install `pre-commit` hooks.

Use `make` or `make lint` to cleanup staged files before commits.

Use `git commit --no-verify` to commit without running pre-commit hooks.

Use `pre-commit autoupdate` to get the latest version of pre-commit hooks.

Use `pre-commit uninstall` to uninstall pre-commit hooks.
