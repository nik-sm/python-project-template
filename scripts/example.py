import argparse

from src.utils import entrypoint, get_git_hash

parser = argparse.ArgumentParser(description="Example CLI", allow_abbrev=False)
parser.add_argument("--arg1", action="store_true", default=False)
parser.add_argument("--arg2", type=int, default=0)
args = parser.parse_args()

print(f"Git commit hash: {get_git_hash()}")
print(f"Args: {args}")

entrypoint()
