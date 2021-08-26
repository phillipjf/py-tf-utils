# py-tf-utils

This project contains a command-line tool for various Terraform utilities.

For an example, see the `sample-module` directory.

## Installation

```sh
pip install py-tf-utils
```

## Usage

To test with the sample project:

```sh
# Will show unused variables in `sample-module` and `sub-module`
tf-utils unused sample-module

# Will ONLY show unused variables in `sub-module`
tf-utils unused sample-module/sub-module/
```

## Background

- [Finding unused variables in a Terraform module](https://alexwlchan.net/2019/05/finding-unused-variables-in-a-terraform-module/)
