def list_sort (lis):

    even = []
    odds = []
    chars = []

    d = dict()

    for x in lis:
        if isinstance(x , str):
            chars.append(x)

        if isinstance(x, (int, float)): 
            if x % 2 == 0:
                even.append(x)

        
            else: 
                 odds.append(x)
        

    d["even"] = sorted(even)
    d["odds"] = sorted(odds)
    d["chars"] = sorted(chars)
    return d


print(list_sort([15, 2.0, 5, 's', 10, 20, "great", 5.9]))

           




