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
# Will generate docs for `sample-module` and `sub-module`
tf-utils docs sample-module

# Will ONLY generate docs for `sub-module`
tf-utils docs sample-module/sub-module/

# Will show unused variables in `sample-module` and `sub-module`
tf-utils unused sample-module

# Will ONLY show unused variables in `sub-module`
tf-utils unused sample-module/sub-module/
```

The documentation can also be redirected to a file:

```sh
tf-utils docs sample-module/sub-module/ >> TF_DOCS.md
```

## Background

- [Using terraform-docs to keep your module documentation in sync](https://www.davidbegin.com/using-terraform-docs-to-automate-keeping-your-terraform-modules-documenting/)
- [Finding unused variables in a Terraform module](https://alexwlchan.net/2019/05/finding-unused-variables-in-a-terraform-module/)