import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def t_in_s(t_freq, s_freq):
            """
            Return True if every character in t (including duplicates) is contained in s, 
            else False
            """
            for char in t_freq:
                if char not in s_freq or s_freq[char] < t_freq[char]:
                    return False
            return True

        t_freq = dict(collections.Counter(t))
        s_freq = dict()

        min_substring = ""
        left_ptr = right_ptr = 0

        while right_ptr < len(s):
            s_freq[s[right_ptr]] = 1 if s[right_ptr] not in s_freq \
                                    else s_freq[s[right_ptr]] + 1

            while right_ptr < len(s) - 1 and not t_in_s(t_freq, s_freq):
                right_ptr += 1
                s_freq[s[right_ptr]] = 1 if s[right_ptr] not in s_freq \
                                        else s_freq[s[right_ptr]] + 1
            while t_in_s(t_freq, s_freq):
                valid_substring = s[left_ptr:right_ptr + 1]
                if not min_substring or len(valid_substring) < len(min_substring):
                    min_substring = valid_substring
                s_freq[s[left_ptr]] -= 1
                left_ptr += 1        
            
            right_ptr += 1

        return min_substring