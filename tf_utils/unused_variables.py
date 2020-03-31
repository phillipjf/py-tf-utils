#!/usr/bin/env python

import os
import sys

import hcl2 as hcl

ITEM_MAP = {
    'locals': 'local',
    'variables': 'var'
}


def get_items_in_file(path, item_type):
    try:
        print(f"Checking file {path}...")
        with open(path) as tf:
            tf_definitions = hcl.load(tf)
    except ValueError as err:
        raise ValueError(f"Error loading Terraform from {path}: {err}")

    try:
        if item_type == 'variables':
            variables = [str(list(v.keys())[0]) for v in tf_definitions['variable']]
            return set(variables)
        elif item_type == 'locals':
            _locals = tf_definitions.get('locals', [])
            if _locals:
                _locals = _locals[0].keys()
            return set(_locals)
        else:
            raise NotImplementedError(f"{item_type} not supported")
    except KeyError:
        return set()
    except AttributeError:
        return set()


def tf_files_in_module(dirname):
    for f in os.listdir(dirname):
        if f.endswith(".tf"):
            yield f


def get_items_in_module(dirname, item_type):
    all_items = {}

    for f in tf_files_in_module(dirname):
        file_path = os.path.join(dirname, f)
        for varname in get_items_in_file(file_path, item_type):
            all_items[varname] = f
    return all_items


def find_unused_items_in_module(dirname, item_type):
    unused_items = get_items_in_module(dirname, item_type)

    for f in tf_files_in_module(dirname):
        if not unused_items:
            return {}

        tf_src = open(os.path.join(dirname, f)).read()
        for varname in list(unused_items):
            if f"{ITEM_MAP[item_type]}.{varname}" in tf_src:
                del unused_items[varname]

    return unused_items


def find_unused_variables_in_tree(root):
    for mod_root, _, filenames in os.walk(root):
        if (mod_root.startswith('./terraform.tfstate.d') or
            mod_root.startswith('./.terraform')):
            continue
        if not any(f.endswith(".tf") for f in filenames):
            continue

        for item_type, label in ITEM_MAP.items():
            unused_items = find_unused_items_in_module(mod_root, item_type)
            if unused_items:
                print(f"Unused {item_type} in {mod_root}:")
                for varname, filename in unused_items.items():
                    filepath = os.path.join(mod_root, filename)
                    print(f"* {filepath} ~> {label}.{varname}")
                print("")


if __name__ == "__main__":
    try:
        root = sys.argv[1]
    except IndexError:
        root = "."

    find_unused_variables_in_tree(root)
