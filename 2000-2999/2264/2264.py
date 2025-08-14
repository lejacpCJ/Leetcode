class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = -1  # Store the largest digit found in a good integer
        
        # Iterate through all substrings of length 3
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                # Update max_good if this digit is larger
                max_good = max(max_good, int(num[i]))
        
        # If no good integer was found, return empty string
        if max_good == -1:
            return ""
        # Return the largest good integer as a string of length 3
        return str(max_good) * 3