s = "Let's take LeetCode contest"
print(s.split())
x = ' '.join([word[::-1] for word in s.split()])
print(x)
v=[i[::-1] for i in s.split()]
print(v)
s=' '.join([i[::-1] for i in s.split()])
print(s)