import random

for i in range (1, 6):
    # 1부터 46까지의 숫자 중에서 중복 없이 6개를 랜덤으로 선택합니다.
    random_numbers = random.sample(range(1, 47), 6)

    # 추출된 숫자를 정렬하여 출력합니다.
    random_numbers.sort()
    print(str(i) + "번의 6개 숫자:", random_numbers)