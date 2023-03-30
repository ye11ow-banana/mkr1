def get_keyword() -> str:
    return input('Keyword: ')


def get_data_from_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return file.readlines()


def filter_data(data: list[str], keyword: str) -> list[str]:
    return [_ for _ in data if keyword in _]


def write_data_to_file(file_path: str, data: list[str]) -> None:
    with open(file_path, 'w') as file:
        return file.writelines(data)


def main() -> None:
    keyword = get_keyword()
    data = get_data_from_file('src/data.txt')
    filtered_data = filter_data(data, keyword)
    write_data_to_file('src/filtered.txt', filtered_data)


if __name__ == '__main__':
    main()
