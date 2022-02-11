import os

from tf_utils import utils

ITEM_MAP = {"locals": "local", "variables": "var"}


def get_items_in_file(path, item_type):
    tf_definitions = utils.load_terraform(path)
    try:
        if item_type == "variables":
            variables = [str(list(v.keys())[0]) for v in tf_definitions.get("variable", [])]
            return set(variables)
        elif item_type == "locals":
            _locals = tf_definitions.get("locals", [])
            if _locals:
                _locals = _locals[0].keys()
            return set(_locals)
        else:
            raise NotImplementedError(f"{item_type} not supported")
    except KeyError:
        return set()
    except AttributeError:
        return set()


def find_unused_variables_in_tree(root):
    modules = utils.module_file_list(root)
    for mod_root, files in modules.items():
        for item_type, label in ITEM_MAP.items():
            items = {}
            for f in files:
                file_path = os.path.join(mod_root, f)
                print(f"Checking file {file_path}...")
                for item_name in get_items_in_file(file_path, item_type):
                    items[item_name] = f

            for f in files:
                tf_src = open(os.path.join(mod_root, f)).read()
                for varname in list(items):
                    if f"{ITEM_MAP[item_type]}.{varname}" in tf_src:
                        del items[varname]
            if items:
                print(f"Unused {item_type} in {mod_root}:")
                for varname, filename in items.items():
                    filepath = os.path.join(mod_root, filename)
                    print(f"* {filepath} ~> {label}.{varname}")
                print("")
