def check_prime_number(num):
    if num > 1 and num < 1000000:
        for i in range(2,num):
            if (num % i) == 0:
                return '{} is not a prime number'.format(num)
            else:
                return '{} is a prime number'.format(num)
    else:
        return '{} is a prime number'.format(num)
            
def loop_n(n):
    distinct_array = set(n)
    for i in distinct_array:
        print(check_prime_number(i))


n =[2,3,4,4,4,6,7,7,9,5,6,7,8, 407, 408, 17]
loop_n(n)