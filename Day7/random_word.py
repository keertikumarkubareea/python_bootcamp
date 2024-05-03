"""
Beginning of the Python Hangman project
"""
import random
import constants


def choose_random(list_of_words: list) -> str:
    return random.choice(list_of_words)


random_word = choose_random(constants.WORDS)

placeholder = []

for char in random_word:
    placeholder.append(constants.PLACEHOLDER)

placeholder_str = ' '.join(placeholder)
print(f"A random word has been chosen.")

lives_used = 0

while constants.PLACEHOLDER in placeholder and lives_used < constants.NUMBER_OF_LIVES:
    print("--------------------------------------------------")
    print(f"Take a character guess: {placeholder_str}")
    char = input().lower()
    if char in random_word:
        print(f"Character '{char}' is present in the word")
        # Replace the placeholder underscores with the character placed at the appropriate index
        for index in range(0, len(random_word)):
            if random_word[index] == char:
                placeholder[index] = char
        placeholder_str = ' '.join(placeholder)
    else:
        print(f"Character '{char}' is NOT present in the word")
        lives_used += 1
    print(f"You have {constants.NUMBER_OF_LIVES - lives_used} lives left")

print("--------------------------------------------------")

if lives_used >= constants.NUMBER_OF_LIVES:
    print("You lose. You have exhausted all your lives")
else:
    print("You won!!!!")
    print(f"You have correctly guessed: {placeholder_str}")
    print(f"You had {constants.NUMBER_OF_LIVES - lives_used} lives left! Good job!")


