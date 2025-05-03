import random 
import timer
while True: 
    start_time = time.time() 
    number = random.randint(1, 75) 
    print("Guess a number between 1 and 75") 
    guess = int(input()) 
    if guess == number: 
        print("You win!") 
    else: 
        if guess < number: 
            print("Too low!") 
        elif guess > number: 
            print("Too high!") 
        print(f"Wrong! The number was {number}") 
        print("Play again? (y/n)") 
        if input().lower() != 'y': 
            break
    print(f"Time taken: {time.time() - start_time:.2f}s")