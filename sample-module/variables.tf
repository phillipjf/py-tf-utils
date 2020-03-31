variable unquoted {}

variable string_3 {
  default = ""
}

variable string_2 {
  description = "It's string number two."
  type        = string
}

// It's string number one.
variable string_1 {
  default = "bar"
}

variable map_3 {
  default = {}
}

variable map_of_strings {
  description = "It's a map of strings."
  type        = map(string)
}

variable map_of_any {
  description = "It's a map of any."
  type        = map(any)
}

// It's map number one.
variable map_1 {
  default = {
    a = 1
    b = 2
    c = 3
  }

  type = map(string)
}

variable list_3 {
  default = []
}

variable list_2 {
  description = "It's list number two."
  type        = list(string)
}

// It's list number one.
variable list_1 {
  default = ["a", "b", "c"]
  type    = list(string)
}

// A variable with pipe in the description
variable input_with_pipe {
  description = "It includes v1 | v2 | v3"
  default     = "v1"
}
