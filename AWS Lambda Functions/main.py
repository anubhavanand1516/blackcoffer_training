
import random

def random_drink():
    drinks=["coffee","tea","beer","wine","water","juice"]
    return random.choice(drinks)

if __name__=="__main__":
    print(f"you should drink some {random_drink()}")
