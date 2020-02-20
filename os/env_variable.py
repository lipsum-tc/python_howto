
import os

"""
get:
os.environ["KEY"]
os.environ.get("key", "default_value")

set:
os.environ["KEY"] = value

delete:
del os.environ["KEY"]

iterate:
for key, value in os.environ.items():
    ...
"""

def dump_env_variables():
    for key, value in os.environ.items():
        print(key, "=", value)


if __name__ == "__main__":
    dump_env_variables()

