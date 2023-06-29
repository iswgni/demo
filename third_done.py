numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def f(x):
    if x > 50:
         if x % 2 == 0:
            return True
         else:
            return False
    else:
        return False

out_filter = filter(f, numbers)
print(list(out_filter))