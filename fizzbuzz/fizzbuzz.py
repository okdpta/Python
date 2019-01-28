def Fizzbuzz (list_1,list_2):
    
    list_1 = [6,8,4,5,9,6]
    list_2 = [4,7,5,4,9,6,8,7,6]
    total_length = len(list_1) + len(list_2)

    #total number of items in both lists
    print(total_length)

    #if total_length is divisible by both 3 and 5
    if total_length % 3 == 0 and total_length % 5 == 0:
      print ("FizzBuzz")

      #if total_length is divisible by 3 
    elif total_length % 3 == 0: 
      print ("Fizz")

      #if total_length is divisible by 5
    elif total_length % 5 == 0:
     print ("Buzz")
    else: 
        #prints value of total_length
     print (total_length)



Fizzbuzz ([],[])


