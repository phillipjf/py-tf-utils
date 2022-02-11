import os

import hcl2 as hcl


def load_terraform(path):
    try:
        with open(path) as tf:
            return hcl.load(tf)
    except ValueError as err:
        raise ValueError(f"Error loading Terraform from {path}: {err}")


def module_file_list(root="."):
    ignored_directories = ["/terraform.tfstate.d", "/.terraform", "/.git"]
    modules = {}
    for mod_root, _, filenames in os.walk(root):
        # Ignore select directories
        if any([v in mod_root for v in ignored_directories]):
            continue
        # Skip if there are no Terraform files in the directory
        if not any([f.endswith(".tf") for f in filenames]):
            continue

        modules[mod_root] = [f for f in filenames if f.endswith(".tf")]

    return modules
