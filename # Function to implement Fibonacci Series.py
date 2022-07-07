# Function to implement Fibonacci Series
def fibMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

tempDict = {}
print(tempDict)
fibMemo(6, tempDict)

#Printing the elements of the Fibonacci Series
print("0")
print("1")
for element in tempDict.values():
    print(element)