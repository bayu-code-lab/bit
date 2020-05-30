
def check(n):
    result = 0
    for i in range(len(n)):
        for x in range(len(n),-1,-1):
            if n[i] == n[x-1]:
                break

            profit = n[x-1] - n[i]

            if profit > result:
                result = profit
    if result == 0:
        print('Harga selalu turun')
    else:
        print(result)

n = [5, 6, 15, 3, 10, 22, 15] #input value here
check(n)

