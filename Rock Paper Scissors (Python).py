import random
import time

def game_startup():
    time.sleep(1)
    print("ROCK!")
    time.sleep(1)
    print("PAPER!")
    time.sleep(1)
    print("SCISSORS!")
    time.sleep(1)
    print("SHOOT!")

def calc(p,c):
    if p == c:
        print("TIE")
    elif (p == "Rock" and c == "Paper") or (p == "Scissors" and c == "Rock") or (p == "Paper" and c == "Scissors"):
        print(f"{c} beats {p}: YOU LOSE")
    else:
        print(f"{p} beats {c}: YOU WIN")
    time.sleep(1)

def main():
    CPU_list = ["Rock", "Paper", "Scissors"]

    while True:
        Player = input("Pick Rock, Paper, or Scissors (type 'quit' to end): ")
        if Player == "quit":
            quit()
        if Player not in CPU_list:
            continue
        CPU = CPU_list[random.randint(0,2)]
        game_startup()
        print(f"Your move: {Player}, CPU: {CPU}")
        time.sleep(1)
        calc(Player,CPU)
        print("\n")
main()


