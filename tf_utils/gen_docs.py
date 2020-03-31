import os

import hcl2 as hcl
from tabulate import tabulate

variable_headers = [
    "Name",
    "Description",
    "Type",
    "Default",
    "Required",
]

output_headers = [
    "Name",
    "Description",
]


def get_all_vars_and_outs(modules):
    all_vars_and_outs = {}

    for module, files in modules.items():
        values = {'variable': [], 'output': []}
        for file in files:
            with open(os.path.join(module, file)) as f:
                parsed = hcl.loads(f.read())
            for k, v in values.items():
                # This could possibly clobber duplicate vars
                # but there shouldn't be any dupes anyways
                v.extend(parsed.get(k, []))
            all_vars_and_outs[module] = values

    return all_vars_and_outs


def format_output_for_table(values):
    rows = []
    for value in values:
        key, val = list(value.items())[0]
        row = [
            key,
            val.get('description', [''])[0]
        ]
        rows.append(row)

    return rows


def format_variable_for_table(values):
    rows = []
    for value in values:
        key, val = list(value.items())[0]
        row = [
            key,
            val.get('description', [''])[0],
            val.get('type', [''])[0],
            val.get('default', [''])[0],
            not bool(val.get('default', None))
        ]
        rows.append(row)

    return rows


def format_for_table(module_items):
    to_docs = {}
    for module, items in module_items.items():
        to_docs[module] = {}
        for _type, values in items.items():
            func = globals().get(f"format_{_type}_for_table")
            to_docs[module][_type] = func(values)
    return to_docs


def generate_docs(table_items):
    for module, items in table_items.items():
        header = module.lstrip('./')
        print(f"## {header}")
        for _type, rows in items.items():
            print(f"### {_type}")
            headers = globals().get(_type+'_headers')
            print(tabulate(rows, headers, tablefmt='pipe'))
