import sys

from tf_utils import unused_variables


def help(command=None):
    default = (
        "Usage: tf-utils command [path]\n"
        + "\tcommand: unused \n"
        + "\tpath: A path to the module root to analyze. "
        + "Default: current directory."
    )
    unused = (
        "Usage: tf-utils unused [path]\n"
        + "\tpath: A path to the module root to analyze. "
        + "Default: current directory."
    )
    help_docs = {
        "default": default,
        "unused": unused,
    }
    return help_docs.get(command, default)


def main():
    args = sys.argv
    if len(args) < 2:
        return help()

    command = sys.argv[1]
    try:
        root = sys.argv[2]
    except IndexError:
        root = "."

    if "help" in root:
        return help(command)

    if command == "unused":
        return unused_variables.find_unused_variables_in_tree(root)
    else:
        return help()
