# Cyberdudebivash's Password Strength Checker

## Description

This is a simple GUI application built with Tkinter to check password strength, display percentage, verify against cybersecurity guidelines (e.g., NIST: 8+ chars, mixed types, not guessable), and suggest strong passwords.

**Note:** For educational purposes. Uses zxcvbn for analysis (scores 0-4, feedback). Suggestions use secure random generation.

## Requirements

- Python 3.x
- Packages: See `requirements.txt`

## Installation

1. Install dependencies: `pip install -r requirements.txt`
2. Run `python main.py`

## Usage

1. Launch the app: `python main.py`
2. Enter a password in the field.
3. Click "Check Strength" to see:
   - Strength level and percentage.
   - If it meets guidelines (Yes/No).
   - Feedback and suggestions.
4. Click "Suggest Strong Password" for a random 16-char secure password.

## Features

- **Strength Checker**: Uses zxcvbn for score, crack time estimates.
- **Percentage**: Score-based (0-100%).
- **Guidelines Check**: Length, character mix, guessability.
- **Recommendations**: Generates strong passwords on demand.

## Limitations

- Passwords are hidden in entry but processed in memory.
- No storage; pure checker.
- Expand with more guidelines (e.g., breach checks via API).

## License

MIT License 

##COPYRIGHT@CYBERDUDEBIVASH  2025