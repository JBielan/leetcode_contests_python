class Solution:
    def indexPairs(self, text, words):
        result = []
        for word in words:      # for every word
            length = len(word)      # store length so no need to call len function more
            for i in range(len(text) - length + 1):     # i from 0 to last index needed to check all possibilites
                if text[i: i + length] == word:     # for every i check if slice equals word
                    result.append([i, i + length - 1])      # if yes, just add coordinates

        result = sorted(result, key=lambda k: [k[0], k[1]])     # sort result in order to first and second item
        return result