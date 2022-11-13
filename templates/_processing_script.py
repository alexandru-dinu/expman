import argparse


def main() -> None:
    # use cli_args
    # use logging
    ...


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    ...
    cli_args = parser.parse_args()

    logger = ...  # setup logger

    main()
