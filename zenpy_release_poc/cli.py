import argparse

from zenpy_release_poc import __version__


def main():
    parser = argparse.ArgumentParser(prog="zenpy-release-poc")
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args()
    print(f"zenpy-release-poc {__version__}: release automation PoC is working")


if __name__ == "__main__":
    main()
