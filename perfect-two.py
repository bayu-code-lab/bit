def check(n):
    array = [2,7,11,15]
    cut = False
    for i in range(len(array)):
        for x in range(len(array) - i):
            if n == array[i] + array[x+i]:
                print([i,x+i])
                cut = True
        if cut:
            break

check(26) #input value here
