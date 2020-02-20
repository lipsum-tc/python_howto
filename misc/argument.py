import argparse

"""
how to get command arguments

import argparse
parser = argparse.ArgumentParser()
    description = "description"

-h, --help option is defined automatically.

define argument:
parser.add_argument("name1", "name2", ....)
    type = <type>               specify argument type: e.g. int, str
    help = "help message"
    default = <default_value>   without default option, the default value is None.
    choices = [option1, option2, ...]   limit options to specified values
    action = "<action_str>"
        "store_true"
        "count"

mutually exclusive options:
group = parser.add_mutually_exclusive_group()
group.add_argument(option 1 definition)
group.add_argument(option 2 definition)
now, option1 and option2 are mutually exclusive.

get arguments:
args = parser.parse_args()
the args is Namespace object.

args.hoge   argument value
"""

def calc_expr():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type = int)
    parser.add_argument("operator", choices = ["+", "-", "/", "*", "**", "%"])
    parser.add_argument("y", type = int)
    parser.add_argument("-v", "--verbose", type = bool, default = False)

    args = parser.parse_args()
    if args.verbose:
        for key, value in vars(args).items():
            print(f"{key} = {value}")
    expr = f"{args.x} {args.operator} {args.y}"
    result = eval(expr)
    print(expr, "=", result)


if __name__ == "__main__":
    calc_expr()
