# Python Games Collection

A collection of classic games built with Python! Perfect for learning game development, practicing Python, or just having fun.

## Available Games

| Game | Description | Run Command |
|------|-------------|-------------|
| **BlackJack** | Classic casino card game with betting | `cd BlackJack && python main.py` |
| **SnakeGame** | Control the snake, eat food, grow longer! | `cd SnakeGame && python main.py` |
| **PingPong** | Two-player ping pong with sound effects | `cd PingPong && python main.py` |
| **Breakout** | Break all the bricks with your paddle | `cd Breakout && python main.py` |
| **Pacman** | Navigate the maze, avoid ghosts | `cd Pacman && python main.py` |
| **Hangman** | Word guessing game | `cd Hangman && python main.py` |
| **TurtleCrossing** | Help the turtle cross the road | `cd TurtleCrossing && python main.py` |
| **KBC** | Quiz game inspired by Kaun Banega Crorepati | `cd KBC && python main.py` |
| **RockPaperScissor** | Classic hand game vs computer | `cd RockPaperScissor && python main.py` |

## Getting Started

### Prerequisites

- Python 3.7 or higher
- tkinter (usually comes with Python)
- turtle module (comes with Python)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnshMNSoni/python-games.git
   cd python-games
   ```

2. Run any game:
   ```bash
   cd <GameFolder>
   python main.py
   ```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new games
- Improving existing games
- Reporting bugs
- Suggesting features

## Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
python -m pytest tests/

# Run tests for a specific game
python -m pytest tests/BlackJack/
```

## 📁 Project Structure

```
python-games/
├── BlackJack/          # Card game with GUI
├── SnakeGame/          # Classic snake game
├── PingPong/           # Pong with sound
├── Breakout/           # Brick breaker
├── Pacman/             # Maze game
├── Hangman/            # Word guessing
├── TurtleCrossing/     # Road crossing game
├── KBC/                # Quiz game
├── RockPaperScissor/   # Hand game
├── tests/              # Unit tests for all games
├── CONTRIBUTING.md     # Contribution guidelines
└── README.md           # This file
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **Star this repo if you find it useful!**
