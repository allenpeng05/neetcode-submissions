class Solution:
    # create a dictionary, key = sorted word, value = list of words
    # at the end, return all values in the dictionary
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)
        
        answer = []
        for v in d.values():
            answer.append(v)
        return answer



        
        