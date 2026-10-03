"""
Problem: Encode and Decode Strings
LeetCode: 271
Pattern: Length-prefixed encoding
Time: O(n)
Space: O(n)
Attempts: 1
Date: 2026-10-03
Notes: Prepend each string with len(s) + '#'. Decode reads length until '#',
       then reads exactly that many characters.
"""

def encode(strs):
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        result.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return result

if __name__ == "__main__":
    original = ["lint", "code", "love", "you"]
    encoded = encode(original)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decode(encoded)}")
    assert decode(encode(original)) == original

    edge_cases = [[""], ["#", "##"], ["a" * 100]]
    for case in edge_cases:
        assert decode(encode(case)) == case, f"Failed on {case}"
    print("All tests passed")
