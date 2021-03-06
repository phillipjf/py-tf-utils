locals {
    a_string = "my_test_local"
    using_a_local = replace(local.a_string, "_", "-")
    using_a_var = format("Using var: %s", var.string_2)
}

module "foo" {
  source = "github.com/foo/bar"

  id   = "1234567890"
  name = "baz"

  zones = ["us-east-1", "us-west-1"]

  tags = {
    Name         = "baz"
    Created-By   = "first.last@email.com"
    Date-Created = "20180101"
  }
}

module "foo" {
  source = "github.com/foo/bar?refs=tag/v0.1.0"

  id   = "1234567890"
  name = "baz"

  zones = ["us-east-1", "us-west-1"]

  tags = {
    Name         = "baz"
    Created-By   = "first.last@email.com"
    Date-Created = "20180101"
  }
}
