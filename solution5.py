# Write code for algorithm 5 below
def palindrome(word):
    # return s == s[ ::-1]

   if len(word) < 2:
      
   else:
        if word[0] == word[-1]:
                return palindrome(word[1:-1])
        else:
                return False
        
print(palindrome("racecar"))
