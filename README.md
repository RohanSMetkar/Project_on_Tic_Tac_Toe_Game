🎮 Python Tic-Tac-Toe (Milestone Project)
A clean, functional, and terminal-friendly implementation of the classic Tic-Tac-Toe game built with Python 3. This project focuses on modular programming, using functions to handle board rendering, win logic, and user input validation.

🚀 Features
Numpad Mapping: Intuitive control using the 1-9 keys (mapped like a computer's numeric keypad).

Smart Validation: Prevents players from picking occupied spaces or entering invalid characters.

Randomized Starts: The computer randomly decides which player goes first.

Cross-Platform: Works in Jupyter Notebooks, VS Code, and online terminal compilers (like Online GDB).

🛠️ How to Play
Run the script in any Python 3 environment.

Choose your marker: Player 1 picks 'X' or 'O'.

Enter positions: Use the number keys 1-9 to place your mark based on the layout below:

Plaintext
 7 | 8 | 9 
-----------
 4 | 5 | 6 
-----------
 1 | 2 | 3 
Win or Draw: The game automatically detects three-in-a-row or a full board (tie).

Replay: Choose to play another round without restarting the script.

💻 Installation & Usage
Clone the repository:

Bash
https://github.com/RohanSMetkar/Project_on_Tic_Tac_Toe_Game
Navigate to the directory:

Bash
cd tic-tac-toe-python
Run the game:

Bash
python tic_tac_toe.py
📂 Project Structure
display_board(): Renders the 3x3 grid.

player_input(): Handles 'X' or 'O' assignment.

win_check(): Contains the logic for 8 possible winning combinations.

player_choice(): Validates that the chosen move is both a number and an empty space.


📝 Notes on Compiler Compatibility
This version is optimized for Online GDB and standard terminals.

It uses print('\n' * 100) to simulate a "clear screen" effect without needing external Jupyter libraries (IPython.display).

Includes try/except blocks to handle input errors gracefully.
