#1
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

#2
def find_prefix(dictionary, word, temp = []):
	for x in dictionary:
		if word.startswith(x) :
			temp.append(x)
			word = word.split(x)[1]
			return find_prefix(dictionary, word, temp)

	return temp if not word else False

if __name__ == "__main__":
	dictionary = ['pro', 'gram', 'merit', 'program', 'it', 'programmer']
	word = input("Enter your value: ") 

	if word.startswith(tuple(dictionary)) :
		for x in dictionary :
			if word.startswith(x) :
				if word == x :
					print(x)
				else : 
					res = find_prefix(dictionary, word.split(x)[1],[x])
					if res : 
						print(', '.join(res))


	else : 
		print("< no way >")
		
#3
# python_3

def wordBreak(dict, str, out=''):

    if not str:
        print(out)
        return

    for i in range(1, len(str) + 1):
        prefix = str[:i]
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)


if __name__ == '__main__':

    # List dictionary
    dict = [
        "pro", "gram", "merit", "program", "it", "programmer"
    ]

    # input String
    n = input("Your String: ")

    wordBreak(dict, n)
