# 29.4 매개변수 모두 곱하기
def all_mul(*arg):
    mul = 1
    for i in arg:
        mul *= i
    return mul
print(all_mul(5,7,9,10))
