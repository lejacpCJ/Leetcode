class Solution:
    def soupServings(self, n: int) -> float:
        # For large n, probability approaches 1.0
        if n >= 4800:
            return 1.0
        
        # Scale down by 25 to reduce state space
        # All operations are multiples of 25
        def helper(a, b, memo):
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a <= 0 and b <= 0:
                # Both empty at same time
                return 0.5
            if a <= 0:
                # A empty first
                return 1.0
            if b <= 0:
                # B empty first
                return 0.0
            
            # Calculate probability for each operation
            prob = 0.25 * (
                helper(a - 4, b, memo) +      # pour 100mL A, 0mL B
                helper(a - 3, b - 1, memo) +  # pour 75mL A, 25mL B
                helper(a - 2, b - 2, memo) +  # pour 50mL A, 50mL B
                helper(a - 1, b - 3, memo)    # pour 25mL A, 75mL B
            )
            
            memo[(a, b)] = prob
            return prob
        
        # Convert n to units of 25mL and round up
        units = (n + 24) // 25
        return helper(units, units, {})