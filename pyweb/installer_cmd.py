#!/usr/bin/env python3

import sys

try:
    from pyweb import pyweb_add_content
except ImportError:
    import pyweb_add_content


def main():
    argv = sys.argv[1:]
    pyweb_add_content.main(argv)


if __name__ == "__main__":
    main()
