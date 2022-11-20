import collections

def t_in_s(t_freq, s_freq):
    """
    Return True if every character in t_freq (including duplicates) is contained 
    in s_freq, else False
    """
    for char in t_freq:
        if char not in s_freq or s_freq[char] < t_freq[char]:
            return False
    return True

def minimum_window_substring(s, t):
    """
    Given two strings s and t of lengths m and n respectively, return the minimum
    window substring of s such that every character in t (including duplicates) 
    is included in the window. If there is no such substring, return the empty 
    string "".
    """
    t_freq = dict(collections.Counter(t))
    s_freq = dict()

    min_substring = ""
    left_ptr = right_ptr = 0

    while right_ptr < len(s):
        # Update count of current character in s
        s_freq[s[right_ptr]] = 1 if s[right_ptr] not in s_freq \
                                 else s_freq[s[right_ptr]] + 1

        # Move right pointer until end of s or t contained in s
        while right_ptr < len(s) - 1 and not t_in_s(t_freq, s_freq):
            right_ptr += 1
            s_freq[s[right_ptr]] = 1 if s[right_ptr] not in s_freq \
                                     else s_freq[s[right_ptr]] + 1
        # If t contained in s, move left pointer to minimize window substring
        while t_in_s(t_freq, s_freq):
            valid_substring = s[left_ptr:right_ptr + 1]
            if not min_substring or len(valid_substring) < len(min_substring):
                min_substring = valid_substring
            s_freq[s[left_ptr]] -= 1
            left_ptr += 1        
        
        right_ptr += 1

    return min_substring

s = "ADOBECODEBANC"
t = "ABC"
output = "BANC"
assert(minimum_window_substring(s, t) == output)