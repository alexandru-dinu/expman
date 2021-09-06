def main() -> None:
    # use args
    # use logging
    ...


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    ...
    args = parser.parse_args()

    logger = setup_logging(...)

    main()
