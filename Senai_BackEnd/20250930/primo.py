def is_prime(num):
    count = 1
    criterio = 0
    
    while num > count:
        
        if num % count == 0:
            criterio += 1
        count += 1
    
    if criterio >= 2:
        return False
    else:
        return True
    

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()