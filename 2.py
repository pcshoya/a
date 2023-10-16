import secrets

# 1부터 46까지의 숫자 중에서 중복 없이 6개를 랜덤으로 선택합니다.
random_numbers = secrets.randbelow(6)


# 추출된 숫자를 정렬하여 출력합니다.
random_numbers.sort()
print("암호학적으로 안전한 랜덤으로 추출된 6개의 숫자:", random_numbers)