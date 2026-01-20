from functions.get_files_info import get_files_info


def main():
    test_cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]

    for i, (working_dir, directory) in enumerate(test_cases, 1):
        print(f'{i}. get_files_info("{working_dir}", "{directory}"):')
        print()
        result = get_files_info(working_dir, directory)
        print(f"Result for '{directory}' directory:")
        for line in result.split("\n"):
            print(f"    {line}")
        print()


if __name__ == "__main__":
    main()
