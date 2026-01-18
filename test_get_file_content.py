from functions.get_file_content import get_file_content


def main():
    test_cases = [
        ("calculator", "lorem.txt"),
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),
    ]

    for working_dir, file_path in test_cases:
        print(f'get_file_content("{working_dir}", "{file_path}"):')
        print()
        result = get_file_content(working_dir, file_path)
        print(result)
        print()
        print(f"Result length: {len(result)} characters")
        print()
        print("-" * 50)
        print()


if __name__ == "__main__":
    main()
