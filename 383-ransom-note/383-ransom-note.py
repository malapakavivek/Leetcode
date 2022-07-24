class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
        for i in ransom:
            if i in mag:
                if ransom[i] > mag[i]:
                    return False
            else:
                return False
        return True

        