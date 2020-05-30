def check(n):
    result = ''
    data = n.split(' ')
    array =  ["hot", "dot", "dog", "lot", "log"]
    result = []
    status_one = False
    status_two = False
    for x in array:
        if data[0].startswith(x[0]) and data[0].endswith(x[2]):
            status_one = True
            break
        else:
            status_one = False
    for x in array:
        if data[1].startswith(x[0]) and data[1].endswith(x[2]):
            status_two = True
            break
        else:
            status_two = False
    if status_one and status_two:
        for arr in array:
            for i in range(len(data)):
                if data[i] == arr:
                    result.append(data[i])
                    break
                else:
                    if data[i][0] == arr[0] and data[i][1] != arr[1] and data[i][2] == arr[2]:
                        result.append(data[i])
                        result.append(arr)
                        break
                    elif data[i][0] != arr[0] or data[i][2] != arr[2]:
                        result.append(arr)
                        break
            if data[1] == arr:
                break
            elif data[1][0] == arr[0] and data[1][1] != arr[1] and data[1][2] == arr[2]:
                result.append(data[1])
                break
        print(result)
    else:
        pass


n = 'hit dig' #input value here
check(n)