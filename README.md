# CSV Column Expander

This Python code expands a column in a CSV file with a range of numbers. 

## Getting Started

1. Install Python on your computer if it is not already installed.
2. Download the code file to your computer.

## Prerequisites

The code requires Python 3 and the `csv` module.

## Usage

1. Run the code by opening the terminal or command prompt and navigating to the directory where the code file is saved. Then, enter the command: `python csv_column_expander.py`.
2. Enter the name of the input file when prompted.
3. Enter the name of the output file when prompted.
4. The code will generate a new CSV file with the expanded column.

## Notes

- The code assumes that the column to be expanded is in the second position (index 1). You can change this by modifying the `COL_TO_EXPAND` variable in the code.
- The code assumes that the range of numbers is specified in the column as follows: `<text>(<lower>-<upper>)`. For example, if the column contains the text "apple(1-3)", the code will generate three rows with the values "apple1", "apple2", and "apple3".
- If the specified range is a single number (e.g., "apple(1)"), the code will generate a single row with the value "apple1".
- If the specified range contains leading zeros (e.g., "apple(001-003)"), the code will generate three rows with the values "apple001", "apple002", and "apple003".
