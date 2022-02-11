locals {
  a_string             = "my_test_local"
  unused_using_a_local = replace(local.a_string, "_", "-")
  unused_using_a_var   = format("Using var: %s", var.string_2)
}

module "foo" {
  source  = "hashicorp/foo/bar"
  version = "0.0.0"

  id   = "1234567890"
  name = "baz"

  zones = ["us-east-1", "us-west-1"]

  tags = {
    Name         = "baz"
    Created-By   = "first.last@email.com"
    Date-Created = "20180101"
  }
}

module "foo_bar" {
  source = "github.com/github/bar?ref=tag/v0.1.0"

  id   = "1234567890"
  name = "baz"

  zones = ["us-east-1", "us-west-1"]

  tags = {
    Name         = "baz"
    Created-By   = "first.last@email.com"
    Date-Created = "20180101"
  }
}

module "archive_qp" {
  source = "https://example.com/vpc-module?archive=zip"
}

module "archive_qps" {
  source = "https://example.com/vpc-module?fizz=buzz&archive=zip"
}

module "archive_zip" {
  source = "https://example.com/vpc-module.zip"
}

module "archive_tarbz2" {
  source = "https://example.com/vpc-module.tar.bz2"
}

module "archive_tbz2" {
  source = "https://example.com/vpc-module.tbz2"
}

module "archive_targz" {
  source = "https://example.com/vpc-module.tar.gz"
}

module "archive_tgz" {
  source = "https://example.com/vpc-module.tgz"
}

module "archive_tarxz" {
  source = "https://example.com/vpc-module.tar.xz"
}

module "archive_txz" {
  source = "https://example.com/vpc-module.txz"
}
