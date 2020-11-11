class Solution:
   
    # it makes sense to use the tuple structure here because the keys are immutable.
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            cur_key = tuple(sorted(w))
            if tuple(sorted(w)) in d.keys():
                d[cur_key].append(w)
                
            else:
                key = tuple(sorted(w))
                d[key] = [w]
        return d.values()
                        
# ['input', 'tam', 'mat'] -> [['tam', 'mat'], ['input']]
