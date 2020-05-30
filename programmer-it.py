def check(n):
    array =  ['pro', 'gram', 'merit', 'program', 'it', 'programmer']
    result = ''
    cut = False
    for i in array:
        if i in n:
            result += '{}, '.format(i)
        else:
            cut = True
    if cut:
        pass
    else:
        print(result)


check('programmerit') #input value here