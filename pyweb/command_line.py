import sys

try:
    from pyweb import pyweb
except ImportError:
    import pyweb


def main():
    argv = sys.argv[1:]
    print(argv)
    pyweb.main(argv)


if __name__ == "__main__":
    main()
