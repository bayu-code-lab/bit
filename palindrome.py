def data(n):
    collection = []
    limit = (10 ** n) -1
    result = 0
    for i in range(limit,-1,-1):
        for x in range(limit,-1,-1):
            num = int(i) * int(x)
            if num < result:
                break
            if str(num) == str(num)[::-1] and num > result:
                result = num
    print(result)

n=4 #input value here
data(n) 


