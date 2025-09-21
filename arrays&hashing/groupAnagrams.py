class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs : 
            sort_word = "".join(sorted(i))
            groups[sort_word].append(i)
        
        return list(groups.values())
                    


            
 


            
                