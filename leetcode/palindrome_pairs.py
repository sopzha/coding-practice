class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        # Hash table mapping full words to indices
        word_idx = dict()
        # Hash table mapping suffixes (palindrome prefixes) to indices
        suffix_idx = dict()
        # Hash table mapping palindromes to indices
        palindrome_idx = dict()
        # Empty string case
        empty_idx = None

        # Build index mappings
        for idx, word in enumerate(words):
            if word == "":
                empty_idx = idx
                continue
            
            word_idx[word] = idx

            if word == word[::-1]:
                palindrome_idx[word] = idx

            for char_idx in range(1, len(word)):
                prefix, suffix = word[:char_idx], word[char_idx:]
                if prefix == prefix[::-1]:
                    if suffix in suffix_idx:
                        suffix_idx[suffix].append(idx)
                    else:
                        suffix_idx[suffix] = [idx]

        palindrome_pairs = []
        # Build palindrome pairs
        for idx, word in enumerate(words):
            if word == "":
                for palin_idx in palindrome_idx.values():
                    palindrome_pairs.append([idx, palin_idx])
                continue
            
            # Full words only case
            for char_idx in range(len(word) - 1, -1, -1):
                prefix, suffix = word[:char_idx], word[char_idx:]
                if suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_idx and idx != word_idx[rev_prefix]:
                        palindrome_pairs.append([idx, word_idx[rev_prefix]])

            # Full words and suffixes case
            rev_word = word[::-1]
            if rev_word in word_idx and idx != word_idx[rev_word]:
                palindrome_pairs.append([idx, word_idx[rev_word]])
            if rev_word in suffix_idx:
                for suff_idx in suffix_idx[rev_word]:
                    if idx != suff_idx:
                        palindrome_pairs.append([idx, suff_idx])

            if word in palindrome_idx and empty_idx is not None:
                palindrome_pairs.append([idx, empty_idx])
        
        return palindrome_pairs