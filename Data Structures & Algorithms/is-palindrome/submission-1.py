class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for i in s:
            if i.isalnum():
                str+=i

        str = str.lower()
        return str == str[::-1]        

        