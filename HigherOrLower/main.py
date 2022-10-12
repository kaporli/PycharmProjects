import random
from art import logo
from game_data import data
from art import vs

answer = random.choice(data)

def game():
    game_over = False
    score = 0
    while game_over is not True:
        print(logo)
        global answer
        A = answer
        B = random.choice(data)
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

        guess = input(f"\nWho has more Instagram followers, A or B? ").lower()

        if A['follower_count'] > B['follower_count']:
            answer = A
            wrong_answer = B
            answer_input = "a"
        else:
            answer = B
            wrong_answer = A
            answer_input = "b"

        score += 1

        if guess == answer_input:
            print(f"\nYou're right! Current score: {score}.")
            print(
                f"\n{answer['name']} has {answer['follower_count']} million followers. {wrong_answer['name']} has {wrong_answer['follower_count']} million followers.")
        else:
            print(
                f"\nGame over. {answer['name']} has {answer['follower_count']} million followers. {wrong_answer['name']} has {wrong_answer['follower_count']} million followers. Final score: {score}")
            game_over == True
            break


game()