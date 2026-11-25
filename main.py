#!/usr/bin/env python3
"""make.fun entry program: copy the bundled newspaper image to /output/entry.png.

Stdlib only, offline, deterministic: the output is a byte-for-byte copy of
entry.png, so repeated runs produce identical output.
"""
import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.png"


def main():
    os.umask(0o022)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dst = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
