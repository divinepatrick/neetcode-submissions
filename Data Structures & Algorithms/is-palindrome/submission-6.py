class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make s only alpha-numeric
        clean_s = "".join(char for char in s if char.isalnum())
        inverse_clean_s = clean_s[::-1]
        
        if clean_s.lower() == inverse_clean_s.lower():
            return True
        return False