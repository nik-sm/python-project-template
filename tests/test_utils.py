import re

from src.utils import get_git_hash


def test_get_git_hash():
    git_hash = get_git_hash()
    assert re.match("git[abcdef0-9][+]?", git_hash) is not None
