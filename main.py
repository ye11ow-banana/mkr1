def get_keyword() -> str:
    return input('Keyword: ')


def get_data_from_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return file.readlines()


def main() -> None:
    pass


if __name__ == '__main__':
    main()
