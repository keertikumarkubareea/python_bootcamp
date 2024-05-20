"""
This is a guessing game, and the goal is to guess which person is more popular than the other.
Game stops once we get it wrong.
"""
import data
import random
from replit import clear


def choose_data(all_data: list) -> tuple:
    data1 = random.choice(all_data)
    data2 = random.choice(all_data)
    while data1 == data2:
        data2 = random.choice(all_data)
    return data1, data2


def compare_followers(a: dict, b: dict) -> str:
    """Returns True if Data A is more popular (higher follower count) than Data B"""
    if a[data.FOLLOWER_COUNT] > b[data.FOLLOWER_COUNT]:
        return "a"
    else:
        return "b"


def main():
    player_lost = False
    score = 0
    while not player_lost:
        print(data.LOGO_ART)
        topic1, topic2 = choose_data(all_data=data.DATA)
        print(f"Compare A: {topic1[data.NAME]}, {topic1[data.DESCRIPTION]}, from {topic1[data.COUNTRY]}")
        print(data.VS_ART)
        print(f"Against B: {topic2[data.NAME]}, {topic2[data.DESCRIPTION]}, from {topic2[data.COUNTRY]}")
        choice = ""
        while choice != "a" and choice != "b":
            choice = input("Who has more followers? 'A' or 'B': ").lower()
        clear()
        if choice == compare_followers(a=topic1, b=topic2):
            score += 1
            print(f"You're right! Current score = {score}")
        else:
            player_lost = True
    print(f"Sorry, that's wrong! Final score = {score}")


if __name__ == "__main__":
    main()
