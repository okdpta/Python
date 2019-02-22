def power (num, power_raise):
    #2^4 = 2*2*2*2
    if power_raise >0:
        power_raise = power_raise - 1
        return num * power(num, power_raise)
    else:
        return 1

result = power(3, 3)
print (result)