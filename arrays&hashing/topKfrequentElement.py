class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        tuple_list = list(count_dict.items())
        sorted_items = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        return res

            
            
