#!/usr/bin/env python3
# coding : utf-8

import argparse

class Args:
    def __init__(self, prog, version = 1.0, description = "", epilog = ""):
        self.parser = argparse.ArgumentParser(
            prog = prog,
            description = description,
            epilog = epilog
            )
        self.common(version)

    def common(self, version):
        # self.parser.add_argument("--help", action = "help")
        self.parser.add_argument("--version", action = "version", version = f"%(prog)s {version}")

    def get(self):
        return self.parser.parse_args()

if __name__ == "__main__":
    args = Args("Test Program", "This program is test program")
    args.parser.add_argument("--my-arg0")
    args.parser.add_argument("--my-arg1")
    args.parser.add_argument("--my-arg2", action = "store_true")
    arg = args.get()
    print(arg.my_arg0)
    print(arg.my_arg1)
    print(arg.my_arg2)

