import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================\n")

print("1) ✊  Rock")
print("2) ✋  Paper")
print("3) ✌️  Scissors")
print("4) 🦎  Lizard")
print("5) 🖖  Spock")

player = int(input("Pick a number (1-5): "))
computer = random.randint(1, 5)

choices = {
    1: "✊ Rock",
    2: "✋ Paper",
    3: "✌️ Scissors",
    4: "🦎 Lizard",
    5: "🖖 Spock"
}

print(f"\nYou chose: {choices[player]}")
print(f"CPU chose: {choices[computer]}")

winning_combos = {
    1: [3, 4],
    2: [1, 5],
    3: [2, 4],
    4: [2, 5],
    5: [1, 3]
}

if player == computer:
    print("It's a tie!")
elif computer in winning_combos[player]:
    print("The player won!")
else:
    print("The computer won!")
