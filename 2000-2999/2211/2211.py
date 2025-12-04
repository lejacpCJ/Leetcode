class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        stack_len = 0
        prev = ""
        for dir in directions:
            if prev == "" and dir == "L":
                continue
            elif dir == "R":
                stack_len += 1
                prev = "R"
            elif dir == "L":
                if prev == "R":
                    ans += 1
                    ans += stack_len
                    stack_len = 0
                    prev = "S"
                elif prev == "S":
                    ans += 1
            else:
                if prev == "R":
                    ans += stack_len
                    stack_len = 0
                prev = "S"
        return ans