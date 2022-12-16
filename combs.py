# Importing itertools library to get the combinations
import itertools

# Main Function [ Gets the combination of numbers that equals the  main number ]
def pair(lst, t):
    result = [a for i in range(len(lst), 0, -1)
              for a in itertools.combinations(lst, i)
              if sum(a) == t]

    for combs in result:
        for elements in combs:
            if elements in lst:
                lst.remove(elements)
    lst.sort()
    print(lst)
    return lst

# Call the function pair(list,number)
# pair([1, 2, 3], 2)
