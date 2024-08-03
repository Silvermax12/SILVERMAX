print('Silvermax Welcomes U To Play His Game')
import random

letter_distribution = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2,
                       'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}

letter_scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
                 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

def rack_1():
    rack = []
    for _ in range(7):
        letter = random.choice(list(letter_distribution.keys()))
        rack.append(letter)
        letter_distribution[letter] -= 1
    return rack

def show_rack(rack):
    print("Your rack:")
    for i, letter in enumerate(rack):
        print(f"{i+1}: {letter} (Score: {letter_scores[letter]})")

def tiles(rack):
    indices = input("Enter the number of the tile u wanna change (use comma separate am o): ").split(',')
    new_tiles = []
    for index in indices:
        index = int(index.strip()) - 1
        if 0 <= index < len(rack):
            letter = random.choice(list(letter_distribution.keys()))
            new_tiles.append(letter)
            rack[index] = letter
        else:
            print(f"it seems u no sabi english: {index+1}")
    return new_tiles

def it_exists(word, rack):
    rack_copy = rack.copy()
    for letter in word:
        if letter in rack_copy:
            rack_copy.remove(letter)
        else:
            return False
    return True

def calculate_word_score(word):
    return sum(letter_scores[letter] for letter in word)

with open('wordlist.txt',"r") as file:
    if_it_exists = set(word.strip().upper() for word in file.readlines())

def is_valid_word(word):
    return word.upper() in if_it_exists

def playing(rack):
    word = input("Enter the word u wanna play: ").upper()
    if is_valid_word(word):
        if it_exists(word, player_rack):
            for letter in word:
                if letter in rack:
                    rack.remove(letter)
                else:
                    print("Are u dumb. Better use only letters from ur rack.")
                    return
            score = calculate_word_score(word)
            print(f"You scored {score} points for the word {word}")
            rack += rack_1()[:len(word)]
        else:
            print("Are u dumb. Better use only letters from ur rack.")
    else:
        print(f"The word '{word}' does not exist in Silvermax dictionary. Better try again.")

player_rack = rack_1()

while True:
    show_rack(player_rack)
    
    action = input("\nChoose an action (play/change(tile)/quit): ").lower()
    
    if action == 'play':
        playing(player_rack)
    elif action == 'change':
        new_tiles = tiles(player_rack)
        print(f"You changed tiles: {', '.join(new_tiles)}")
    elif action == 'quit':
        break
    else:
        print("Are u dumb. Better use only letters from ur rack.")

print("All Hail Silvermax")