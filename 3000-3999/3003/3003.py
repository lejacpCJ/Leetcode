from typing import List
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        # Convert each character to a bitmask representing its unique letter
        letters_mask = [1 << (ord(letter) - ord("a")) for letter in s]

        # Helper function to compute prefix (or suffix) partition counts and unique letter masks
        def make_prefix(letters_mask: List[int]):
            prefix = [0]  # Number of partitions up to each position
            prefix_mask = [0]  # Bitmask of unique letters up to each position
            unique_letters_mask = 0
            partitions = 0
            for letter_mask in letters_mask:
                unique_letters_mask |= letter_mask  # Add this letter to the set
                # If unique letters exceed k, start a new partition
                if unique_letters_mask.bit_count() > k:
                    partitions += 1
                    unique_letters_mask = letter_mask  # Start new partition with current letter
                prefix.append(partitions)
                prefix_mask.append(unique_letters_mask)
            return prefix, prefix_mask

        # Compute prefix and suffix partition info
        prefix, prefix_mask = make_prefix(letters_mask)
        # For suffix, reverse the string and process similarly
        suffix, suffix_mask = make_prefix(letters_mask[::-1])

        max_partitions_after_operations = 0
        # Try changing each index to any other letter and calculate the resulting partitions
        for index in range(n):
            # Combine partitions from prefix and suffix (excluding current index)
            partitions = prefix[index] + suffix[-(index + 2)]
            # Bitmask of unique letters in left and right (excluding current index)
            unique_letters_mask = prefix_mask[index] | suffix_mask[-(index + 2)]
            # Case 1: If we can add a new unique letter at this index without exceeding k
            if min(unique_letters_mask.bit_count() + 1, 26) <= k:
                partitions += 1
            # Case 2: Both sides are full (k unique letters), and there is at least one letter not present
            elif (
                prefix_mask[index].bit_count()
                == suffix_mask[-(index + 2)].bit_count()
                == k
                and unique_letters_mask.bit_count() < 26
            ):
                partitions += 3
            # Case 3: Otherwise, flipping this index creates two partitions
            else:
                partitions += 2
            # Track the maximum partitions possible
            max_partitions_after_operations = max(
                max_partitions_after_operations, partitions
            )
        return max_partitions_after_operations