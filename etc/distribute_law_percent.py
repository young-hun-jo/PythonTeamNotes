A, B, C = map(int, input().split())
one = (A+B) % C
two = ((A % C) + (B % C)) % C
three = (A*B) % C
four = ((A % C) * (B % C)) % C
print(one) # one, two 결과 동일
print(two)
print(three) # three, four 결과 동일
print(four)
