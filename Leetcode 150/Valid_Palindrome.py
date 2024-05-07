class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()

        # NOTED -> String += i Coz we made a new string named as string, in this we add all the element of the string and after that we compare the string to find the palindrome.

        left = 0 
        right = len(string) - 1
        # string = string.lower()
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        # for i in s:
        #     if s.isalnum():
        #         s += 1

        #     left = 0
        #     right = len(s) - 1
        #     s = s.lower()

        #     while left <= right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -=1
        #     return True
        # for i in s:
        #     if i.isalnum():
        #     # if s[i] != s[-i]:
        #         return True
        #     else:
        #         return False  

            # s.split()
            # start = 0
            # end = -1
            # for i in s:
            #     if i.isalnum():
            #         return True
            #     elif(s == " "):
            #         return True    
            #     else:
            #         return False
                
            #     start += 1
            #     end -= 1

            # start = 0
            # end = [::-1]
            # for i in s :
            #     if start == end:
            #         return True
            #     else:
            #         return False