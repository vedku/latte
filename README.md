# latte: A developer's best friend

latte is a command-line tool designed to help Python developers analyze their code quickly and easily. It provides several useful commands for code inspection and package management.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone the repository or download the `latte_main.py` file.
3. (Optional) Create an alias for easy access:
   - Open your shell configuration file (`.zshrc` or `.bashrc`):
     ```bash
     nano ~/.zshrc  # For zsh
     # or
     nano ~/.bashrc  # For bash
     ```
   - Add this line at the end of the file:
     ```bash
     alias latte='python3 /path/to/your/latte_main.py'
     ```
   - Save the file and reload your shell configuration:
     ```bash
     source ~/.zshrc  # For zsh
     # or
     source ~/.bashrc  # For bash
     ```

## Usage

1. Open a terminal and navigate to the directory containing `latte_main.py`.
2. Run the script:
   ```bash
   python3 latte_main.py
   ```
   (Or simply type `latte` if you've set up the alias)
3. When prompted, enter the full path to the Python file you want to analyze.
4. Use the available commands to analyze your code.

## Available Commands

- `ln`: Returns the number of lines of code in the file
- `xn`: Returns the number of variables in the code
- `pi`: Installs all the packages imported in the file
- `fn`: Returns the number of functions in the file
- `help`: Displays the list of available commands
- `exit`: Exits the program

## Command Details

### ln (Line Number)
This command counts and displays the total number of lines in your Python file.

Example:
```
latte> ln
Number of lines: 50
```

### xn (Variable Count)
This command counts and displays the number of variables defined in your Python file.

Example:
```
latte> xn
Number of variables: 10
```

### pi (Package Install)
This command identifies all the packages imported in your Python file and attempts to install them using pip.

Example:
```
latte> pi
Installed 3 packages.
```

### fn (Function Count)
This command counts and displays the number of functions defined in your Python file.

Example:
```
latte> fn
Number of functions: 5
```

### help
Displays the list of available commands and their brief descriptions.

### exit
Exits the Latte tool.

## Example Session

```
Welcome to Latte!
Enter the name of the Python file you're editing: /path/to/your/script.py
Type 'help' for a list of commands.
latte> ln
Number of lines: 100
latte> xn
Number of variables: 15
latte> fn
Number of functions: 7
latte> pi
Installed 2 packages.
latte> exit
```

## Notes

- Ensure you have the necessary permissions to install packages when using the `pi` command.
- The tool currently analyzes one file at a time. To analyze a different file, you need to restart the tool.
- Make sure to provide the full path to the Python file you want to analyze when prompted.
