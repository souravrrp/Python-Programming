
import collections


s = "aaabbbcc"

counts = collections.Counter(s)

freq, ans = set(), 0
print(counts.items())
for i, j in counts.items():
    while j > 0 and j in freq:
        #print(i)
        print("Value of J",j)
        j -= 1
        ans += 1
        print("Value of ans",ans)
    print(freq)
    freq.add(j)
    print(j)
    print(freq)
print(ans)

"""
cs = Counter(s).most_common()
length, sum_ = len(s), 0
for key, val in cs:
    if (val > length):
        sum_ += val - length
        val = length
        length = max(0, val - 1)
print(sum_)
"""