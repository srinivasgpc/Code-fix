# using a genarator


n =100
factors = [k for k in range(1,n+1) if n % k == 0]
print(factors)