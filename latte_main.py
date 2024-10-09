#!/usr/bin/env python3

import os
import re
import subprocess


def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())


def count_variables(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # This regex pattern matches variable assignments
        pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*='
        return len(re.findall(pattern, content))


def install_packages(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # This regex pattern matches import statements
        pattern = r'(?:from\s+(\w+)(?:\.\w+)*\s+)?import\s+(\w+|\*)'
        packages = set(match[0] or match[1] for match in re.findall(pattern, content))

    for package in packages:
        subprocess.run(['pip', 'install', package])
    print(f"Installed {len(packages)} packages.")


def count_functions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # This regex pattern matches function definitions
        pattern = r'\bdef\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\('
        return len(re.findall(pattern, content))


def print_help():
    print("Available commands:")
    print("ln - Returns the number of lines of code in the file")
    print("xn - Returns the number of variables in the code")
    print("pi - Installs all the packages in the file")
    print("fn - Returns the number of functions")
    print("help - Displays this help message")
    print("exit - Exits the program")


def main():
    print("Welcome to Latte!")
    file_name = input("Enter the full path of the Python file you're editing: ")

    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return

    print("Type 'help' for a list of commands.")

    while True:
        command = input("latte> ").strip().lower()

        if command == 'exit':
            break
        elif command == 'help':
            print_help()
        elif command == 'ln':
            print(f"Number of lines: {count_lines(file_name)}")
        elif command == 'xn':
            print(f"Number of variables: {count_variables(file_name)}")
        elif command == 'pi':
            install_packages(file_name)
        elif command == 'fn':
            print(f"Number of functions: {count_functions(file_name)}")
        else:
            print("Unknown command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
