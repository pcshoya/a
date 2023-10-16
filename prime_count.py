count = 0
prime = 1

for num in range(1, 101):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                prime=0
                break
            else:
                prime = 1
          
    if prime == 1 and num != 1:
        count += 1

print(count)