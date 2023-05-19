## PYTHONPATHS
1.  [How to set Folder in Python Path](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c) 


## Dictionary

1. Create a dictionary quickly

        keys = [234,2345,235213,2]

        values = ['sdf','dasfs','daf','asdf']
        
        data = dict(zip(keys,values))
    
    Output is a Dictionary.


## Bisect
1. Bisect in python is use to add an element in list or tuple.

        bisect(a:list,7)
    
    where a :- is a list/tuple of elements [1,2,3,4,5]
    
    It enters 7 at index 5
    
    Basically it finds which index the element should be inserted.

    It returns the index where it should be inserted.

    If there is already an element then rightmost index is given

    Time Complexity :- O(log(n))

    Note:- bisect assumes the list is sorted in ascending order else the behaviour is undefined.

2. Bisect_left 

    Inserts element in the left side.

3. Bisect_right

    Inserts element on the right side


## Regular Expressions
1. Positive Lookbehind Assertions

    Positive lookbehind assertion is a type of assertion in regular expressions that matches a pattern only if it is immediately preceded by another pattern. In other words, it looks behind the current position in the string to check if a specific pattern exists before the current position.

    The syntax for positive lookbehind assertion is (?<=pattern), where pattern is the pattern to match. The (?<=pattern) syntax indicates that the match should only be made if the specified pattern exists immediately before the current position.

        import re

        # define the regular expression pattern
        pattern = r"(?<=@)(example\.com)"

        # read the text file
        with open("emails.txt", "r") as f:
            text = f.read()

        # find all matches in the text
        matches = re.findall(pattern, text)

        # print the domain names that match the pattern
        for match in matches:
            print(match)

    In this example, the regular expression pattern r"(?<=@)(example\.com)" matches any string that follows the "@" symbol and is exactly equal to "example.com". The positive lookbehind assertion (?<=@) ensures that the pattern is preceded by the "@" symbol, but the "@" symbol is not included in the match.