import random

def rolling_dice(pip, repeat):
    for i in range(1, repeat+1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과 : " , n)

rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)