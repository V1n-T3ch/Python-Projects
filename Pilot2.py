import random

def aviator_crash():
    print("Welcome to Aviator Crash!")
    bet_amount = float(input("Enter your bet amount: $"))
    multiplier = 1.0
    crash_point = random.uniform(1.5, 10.0)  # Randomize the crash point
    print(f"Multiplier is increasing. Current multiplier: {multiplier:.2f}")
    print("Cash out at any time before the crash!")
    
    while True:
        choice = input("Cash out (c) or continue (enter): ").lower()
        
        if choice == 'c':
            payout = bet_amount * multiplier
            print(f"You cashed out at {multiplier:.2f}x. You won ${payout:.2f}!")
            break
        
        multiplier += 0.1  # Increment the multiplier
        print(f"Multiplier is increasing. Current multiplier: {multiplier:.2f}")
        
        if multiplier >= crash_point:
            print(f"Crash! Multiplier reached {multiplier:.2f}x. You lost ${bet_amount:.2f}.")
            break

if __name__ == "__main__":
    aviator_crash()
