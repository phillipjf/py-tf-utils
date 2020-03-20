#!/usr/bin/env python

import os
import sys

import hcl2 as hcl

OUT_PATH=f"{root}/TF_DOCS.md"


def tf_files_in_module(dirname):
    for f in os.listdir(dirname):
        if f.endswith(".tf"):
            yield f


def get_variables(mod_path):



if __name__ == "__main__":
    try:
        root = sys.argv[1]
    except IndexError:
        root = "."

    find_unused_variables_in_tree(root)
