# Password Complexity Checker

## Overview
This is a Python-based GUI application that evaluates the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. It provides detailed feedback to help users improve their passwords. The application uses Tkinter for the graphical interface and includes a toggle to show/hide the password.

## Features
- **Password Strength Evaluation**: Assesses passwords based on:
  - Length (minimum 8 characters, stronger if >12)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- **Scoring System**: Assigns a score out of 5 (capped at 5):
  - Weak (0-2): Red
  - Moderate (3-4): Orange
  - Strong (5): Green
- **Show/Hide Password**: Toggle between masking the password with asterisks (*) and showing plain text using an eye icon.
- **Feedback**: Displays detailed suggestions for improving password strength.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Installation
1. Clone or download the repository.
2. Ensure Python 3 is installed on your system.
3. Verify Tkinter is available by running `python -m tkinter` (should open a demo window).
4. No additional dependencies are required.

## Usage
1. Save the `Password_complexity_checker.py` file.
2. Run the script:
   ```bash
   python Password_complexity_checker.py
   ```
3. In the GUI:
   - Enter a password in the input field.
   - Click the eye button (👁) to show/hide the password.
   - Click "Check Strength" to evaluate the password.
4. View the strength rating (Weak, Moderate, Strong) and feedback in the text area.

## Example
For the password `Pass123!`:
- **Output**: 
  - Password Strength: Moderate (Score: 4/5) [in orange]
  - Feedback:
    - Password length is acceptable (8-12 characters).
    - Contains uppercase letters: Good!
    - Contains lowercase letters: Good!
    - Contains numbers: Good!
    - Contains special characters: Good!

For the password `Password123!@#long`:
- **Output**: 
  - Password Strength: Strong (Score: 5/5) [in green]
  - Feedback:
    - Password length is strong (>12 characters).
    - Contains uppercase letters: Good!
    - Contains lowercase letters: Good!
    - Contains numbers: Good!
    - Contains special characters: Good!

## Files
- `Password_complexity_checker.py`: Main Python script containing the application logic and GUI.
- `README.md`: This file, providing project documentation.
- `.gitignore`: Specifies files and directories to exclude from version control.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.
