def check_positive(a,b,c):
    positive_count = sum(1 for num in [a,b,c] if num > 0)
    return positive_count == 2

print (check_positive(1,0,2))