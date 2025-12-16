# Blackjack CLI (Python)

Simple command-line Blackjack game with a real 52-card deck (no replacement).

## Features
- Real 52-card deck, shuffled each game
- Ace handling (11 -> 1 when needed)
- Dealer draws until 17
- Natural blackjack detection

## Requirements
- Python 3.10+ (or your version)

## Installation
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run
```bash
python blackjack.py
```
