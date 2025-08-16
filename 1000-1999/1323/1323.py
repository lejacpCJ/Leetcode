class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = [n for n in str(num)]
        # If there is no '6', return the original number
        if '6' not in num_str:
            return num
        i = 0
        # Iterate through the digits to find the first '6'
        while i < len(num_str):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
            i += 1
        # Join the list back to a string and convert to int
        return int(''.join(num_str))