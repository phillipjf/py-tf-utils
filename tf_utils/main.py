import sys

from tf_utils import unused_variables
from tf_utils import gen_docs
from tf_utils import utils


def help(command=None):
    default = (
        "Usage: tf-utils command [path]\n" +
        "\tcommand: unused | docs\n" +
        "\tpath: A path to the module root to analyze. " +
        "Default: current directory."
    )
    unused = (
        "Usage: tf-utils docs [path]\n" +
        "\tpath: A path to the module root to analyze. " +
        "Default: current directory."
    )
    docs = (
        "Usage: tf-utils unused [path]\n" +
        "\tpath: A path to the module root to analyze. " +
        "Default: current directory."
    )
    help_docs = {
        "default": default,
        "unused": unused,
        "docs": docs,
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

    if 'help' in root:
        return help(command)

    if command == 'unused':
        return unused_variables.find_unused_variables_in_tree(root)
    elif command == 'docs':
        modules = utils.find_tf_modules(root)
        module_items = gen_docs.get_all_vars_and_outs(modules)
        rows = gen_docs.format_for_table(module_items)
        return gen_docs.generate_docs(rows)
    else:
        return help()
