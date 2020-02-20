
import sys

"""
sys.argv: list[str]
sys.argv[0]: script path
sys.argv[1]: arg1
sys.argv[2]: arg2
...

num:
    len(sys.argv)

"""

def dump_argv():
    for i in range(len(sys.argv)):
        print(f"{i} : {sys.argv[i]}")


if __name__ == "__main__":
    dump_argv()
