class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = {}
        for word1, word2 in similarPairs:
            if word1 not in similar:
                similar[word1] = set()
            if word2 not in similar:
                similar[word2] = set()
            similar[word1].add(word2)
            similar[word2].add(word1)

        if len(sentence1) != len(sentence2):
            return False

        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2:
                if word1 not in similar or word2 not in similar:
                    return False
                if word1 not in similar[word2]:
                    return False
        
        return True
        