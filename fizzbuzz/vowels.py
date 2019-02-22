def count_vowels(my_string):
    my_set = set ()
    vowels_in_string = set()

    vowels = ["a", "e", "i", "o", "u"]

    for el in my_string:
        if my_string.count(el) >= 2:
            my_set.add(el)

        if el in vowels: 
            vowels_in_string.add(el)    

    string_of_vowels = ",".join(vowels_in_string)
    num_of_duplicates = len(my_set)

    return (string_of_vowels, num_of_duplicates)

my_string = input("enter the vowel:")

result = count_vowels(my_string)
print (result) 