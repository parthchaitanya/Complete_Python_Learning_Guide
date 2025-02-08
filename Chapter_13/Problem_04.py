def divisible5(n):
    if(n%5 == 0):
        return True
    return False


a = [1, 2, 34343, 53, 62345895, 8787, 65, 754, 45, 55]
f = list(filter(divisible5, a))
print(f)