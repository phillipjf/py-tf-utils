# tf-docs

This project contains a bash script to generate documentation of Terraform libraries.

For an example, see the `example` directory.

## Requirements

- [Go](https://golang.org/doc/install#install)
- `terraform-config-inspect`
  - `go get github.com/hashicorp/terraform-config-inspect`
- [jq](https://stedolan.github.io/jq/download/)

## Usage

```sh
./gen-docs.sh /path/to/terraform/module
```

To test with the example:

```sh
./gen-docs.sh example/
```

## Background

- [Using terraform-docs to keep your module documentation in sync](https://www.davidbegin.com/using-terraform-docs-to-automate-keeping-your-terraform-modules-documenting/)
- [Finding unused variables in a Terraform module](https://alexwlchan.net/2019/05/finding-unused-variables-in-a-terraform-module/)