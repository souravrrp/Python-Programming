#Longest Palindrome

strng="WOW"

ret = []
longest = N
found = False

if not strng:
    return ['']

for l in range(N, 0, -1):
    found = False
    for s in range(N-l+1):
        if is_palindrome(s, s+l-1):
            found = True
            ret.append(strng[s:s+l])
    if found:
        break
print(ret)