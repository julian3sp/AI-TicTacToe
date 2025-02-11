# AI-TicTacToe
# AI-TicTacToe

AI-TicTacToe is a Python-based implementation of the classic Tic-Tac-Toe game, featuring an AI opponent that utilizes the Minimax algorithm with Alpha-Beta Pruning for optimal decision-making.

## Features
- **Minimax Algorithm with Alpha-Beta Pruning**: Ensures optimal moves by evaluating the best possible outcomes.
- **Turn-based Play**: Allows a player to compete against the AI.
- **Win Detection**: Identifies winning states and draws.
- **Time Constraint**: Ensures AI makes decisions within a 2-second limit.

## Getting Started

### Prerequisites
Ensure you have Python installed:
```sh
python --version
```

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AI-TicTacToe.git
   ```
2. Navigate to the project directory:
   ```sh
   cd AI-TicTacToe
   ```
3. Run the script:
   ```sh
   python ai_tictactoe.py
   ```

## How to Play
1. The game starts by prompting the user to enter their player name:
   - Enter `blue` to play first as `X`.
   - Enter `orange` to let the AI play first as `X`.
2. Players take turns making moves by entering grid positions (e.g., `a1`, `b2`).
3. The AI will calculate its move and respond.
4. The game continues until there is a winner or a draw.

## Game Mechanics
- The board is represented as a dictionary with keys:
  ```python
  game = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}
  ```
- The AI uses `minimax` to determine the best move based on game states.
- The game terminates when either player wins or all cells are filled (draw).

## Example Gameplay
```
Enter player name (blue/orange): blue
a1
b2
c3
```

## Project Structure
```
AI-TicTacToe/
│── ai_tictactoe.py  # Main game script
│── README.md        # Documentation
```

## Future Improvements
- Implement a GUI for a more interactive experience.
- Add difficulty levels for varied AI strength.
- Enhance AI efficiency with additional heuristics.

## License
This project is open-source and available under the MIT License.

## Author
Your Name - [GitHub Profile](https://github.com/yourusername)

