total = 0
counter = 1
while counter <= 10:
    grad = int(input("점수를 입력: "))
    total = grad + total
    counter = counter + 1
    
aver = total / 10
print(aver)