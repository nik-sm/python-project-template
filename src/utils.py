import subprocess


def get_git_hash():
    """Get short git hash, with "+" suffix if local files modified"""
    # Need to update index, otherwise can give incorrect results
    subprocess.run(["git", "update-index", "-q", "--refresh"])
    h = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip().decode("utf-8")

    # Add '+' suffix if local files are modified
    exitcode, _ = subprocess.getstatusoutput("git diff-index --quiet HEAD")
    if exitcode != 0:
        h += "+"
    return "git" + h


def entrypoint():
    print("Entrypoint")


if __name__ == "__main__":
    entrypoint()
