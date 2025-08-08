# Snake_Water_Gun_Game-
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

## 🧠 Game Logic

```python
youDict = {"s":1,"w":-1,"g":0}
options = {1: "Snake", -1: "Water", 0: "Gun"}


## ▶️ Example Output

Snake - Water - Gun
Select to [snack = s] , [water = w] , [gun = g]
Enter your choice: s
You are select is : Snake
Computer select is : Water
You Win!
