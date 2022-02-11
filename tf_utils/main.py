import sys

from tf_utils import unused_variables
from tf_utils import module_versions


def help(command=None):
    path_param_help = (
        "\tpath: A path to the module root to analyze. "
        + "Default: current directory ('.')."
    )
    help_docs = {
        "default": (
            "Usage: tf-utils command [path]\n"
            + "\tcommand: unused, modules \n"
            + path_param_help
        ),
        "unused": (
            "Usage: tf-utils unused [path]\n"
            + path_param_help
        ),
        "modules": (
            "Usage: tf-utils modules [path]\n"
            + path_param_help
        ),
    }
    return help_docs.get(command, help_docs.get('default'))


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
    elif command == "modules":
        return module_versions.print_module_versions(root)
    else:
        return help()
