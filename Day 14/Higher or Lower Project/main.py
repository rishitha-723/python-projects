import game_data
import art
import random
print(art.logo)
score = 0
game = False
while not game:
    a = random.choice(game_data.data)
    print(f"Compare A: {a["name"]}, {a["description"]}, {a["country"]}")
    print(art.vs)
    b = random.choice(game_data.data)
    if (a == b):
        b = random.choice(game_data.data)
    print(f"Against B: {b["name"]}, {b["description"]}, {b["country"]}")
    guess = input("Who has more followers A or B: ").lower()
    if guess == 'a' and a['follower_count'] > b['follower_count']:
        score += 1
        print("Yor're right! Current score : ", score)
    elif guess == 'b' and b['follower_count'] > a['follower_count']:
        score += 1
        print("Yor're right! Current score : ", score)
    else:
        print("\n" * 20)
        print(art.logo)
        print("Sorry, that's wrong. Final score: ",score)
        game = True



