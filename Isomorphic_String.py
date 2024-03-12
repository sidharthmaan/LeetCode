''' https://leetcode.com/problems/isomorphic-strings/ '''
''' In Isomorphic string we have to check that the string have the same occurence of indexes
for eg egg and add in both case a=0, d=1, another d also = to 1 this return (011)
In both case the output is same so this will return true. 
Append function is use to append or store the index value, if the index value is same then it will return true.'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        listS = []
        listT = []
        # len(s) == len(t)
        for i in s:
            listS.append(s.index(i))
        for i in t:
            listT.append(t.index(i))

        if listS == listT:
            return True
        else:
            return False