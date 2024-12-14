import random

# Game data with names and their associated values
game_data = [
    {"name": "Neymar", "value": 1600000},
    {"name": "Lionel Messi", "value": 2100000},
    {"name": "Cristiano Ronaldo", "value": 2500000},
    {"name": "Taylor Swift", "value": 1700000},
    {"name": "Ariana Grande", "value": 1900000},
    {"name": "Selena Gomez", "value": 2000000},
]

def print_header():
    print("=" * 40)
    print("            WELCOME TO HIGHER OR LOWER")
    print("=" * 40)

def print_goodbye():
    print("=" * 40)
    print("         THANK YOU FOR PLAYING!        ")
    print("=" * 40)

def print_divider():
    print("-" * 40)

def higher_or_lower_game():
    # Shuffle the game data for randomness
    data = game_data[:]
    random.shuffle(data)
    
    player_is_alive = 1  # 1 = alive, 0 = dead
    score = 0

    print_header()

    # Game loop
    while player_is_alive and len(data) > 1:
        current = data.pop(0)
        next_item = data[0]

        print_divider()
        print(f"Current: {current['name']} ({current['value']})")
        print(f"Next: {next_item['name']}")
        guess = input("Will it be higher or lower? (h/l): ").strip().lower()

        if (guess == 'h' and next_item['value'] > current['value']) or \
           (guess == 'l' and next_item['value'] < current['value']):
            score += 1
            print("Correct! 🎉")
        else:
            player_is_alive = 0
            print("Wrong! 💀")
            print(f"The value of {next_item['name']} is {next_item['value']}.")
            break

    print_divider()
    print(f"Your score: {score}")
    print_goodbye()

# Run the game
if __name__ == "__main__":
    higher_or_lower_game()
