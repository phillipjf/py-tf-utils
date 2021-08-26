// It's string number one.
variable "unused_string_1" {
  default = "bar"
}

variable "string_2" {
  description = "It's string number two."
  type        = string
}

variable "unused_string_3" {
  default = ""
}

variable "unused_map_of_strings" {
  description = "It's a map of strings."
  type        = map(string)
}

variable "unused_map_of_any" {
  description = "It's a map of any."
  type        = map(any)
}

// It's map number one.
variable "unused_map_1" {
  default = {
    a = 1
    b = 2
    c = 3
  }

  type = map(string)
}

variable "unused_map_2" {
  default = {}
}

// It's list number one.
variable "unused_list_1" {
  default = ["a", "b", "c"]
  type    = list(string)
}

variable "unused_list_2" {
  description = "It's list number two."
  type        = list(string)
}

variable "unused_list_3" {
  default = []
}

// A variable with pipe in the description
variable "unused_input_with_pipe" {
  description = "It includes v1 | v2 | v3"
  default     = "v1"
}
