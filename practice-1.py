l = []

while True:
    num = int(input("add number or Exit?: "))
    l.append(num)
    if num == 0:
        l.sort(reverse=True)
        break
    
for num in l:
    print(num)