A = [1, 2, 3]
S = set()
S.add(2)
for x in A:
  if S.__contains__(x):
    print("Example")