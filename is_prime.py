num = int(input("숫자를 입력 해 주세요 : "))

prime = 1

for i in range(2, num):
    if num % i == 0:
        prime = 0
        break
    else :
        prime = 1

if num != 1 and prime == 1:
    print("소수입니다.")
else :
    print("소수가 아닙니다.")