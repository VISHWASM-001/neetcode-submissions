class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        a = []

        for key, value in freq.items():
            a.append((value, key))

        a.sort(reverse=True)

        result = []

        for value, key in a:
            result.append(key)

        return result[:k]