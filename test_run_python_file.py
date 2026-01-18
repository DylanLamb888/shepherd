from functions.run_python_file import run_python_file


def main():
    test_cases = [
        ("calculator", "main.py", None),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py", None),
        ("calculator", "../main.py", None),
        ("calculator", "nonexistent.py", None),
        ("calculator", "lorem.txt", None),
    ]

    for working_dir, file_path, args in test_cases:
        if args:
            print(f'run_python_file("{working_dir}", "{file_path}", {args}):')
        else:
            print(f'run_python_file("{working_dir}", "{file_path}"):')
        print()
        result = run_python_file(working_dir, file_path, args)
        print(result)
        print()
        print("-" * 50)
        print()


if __name__ == "__main__":
    main()
