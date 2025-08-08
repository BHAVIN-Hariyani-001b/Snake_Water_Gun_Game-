# 🐍 Snake-Water-Gun Game (Python)

A fun terminal-based mini-game based on the classic **Snake-Water-Gun** concept, similar to Rock-Paper-Scissors.

---

## 🕹️ Game Rules

- 🐍 Snake drinks water → **Snake wins**
- 💧 Water douses gun → **Water wins**
- 🔫 Gun kills snake → **Gun wins**

---

## 🎮 How to Play

1. Run the Python script.
2. Choose one option:
   - `s` → Snake
   - `w` → Water
   - `g` → Gun
3. The computer will randomly select one of the three options.
4. The game will determine the winner based on the rules.

---

## 🧠 Game Logic (Python snippet)

```python
youDict = {"s": 1, "w": -1, "g": 0}
options = {1: "Snake", -1: "Water", 0: "Gun"}

com = random.choice(list(options.keys()))
youStr = input("Enter your choice (s/w/g): ").lower()

if youStr not in youDict:
    print("Invalid choice!")
    exit()

you = youDict[youStr]

print(f"You selected: {options[you]}")
print(f"Computer selected: {options[com]}")

if com == you:
    print("It's a draw!")
elif (com == -1 and you == 1) or (com == 1 and you == 0) or (com == 0 and you == -1):
    print("You Win!")
else:
    print("You Lose!")

```

## ▶️ Output
```
Snake - Water - Gun
Select to [snake = s], [water = w], [gun = g]
Enter your choice: s
You selected: Snake
Computer selected: Water
You Win!
```
---

## 📁 File Structure
```
Snake_Water_Gun_Game/
├── snake-water-gun.py   # Main game logic
└── README.md            # Project documentation
```
---

### 🚀 Run the Game
```
python snake-water-gun.py