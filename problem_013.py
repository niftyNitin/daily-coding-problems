def get_longest_substring(s, k):
    if not s:
        return ''
    if len(s) < k:
        return s
    if k == 1:
        return s[0]

    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1

    distinct_count = 0
    seen_chars = set()
    candidate = s
    remaining_string = None

    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_count += 1

        if distinct_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break

    longest_remaining = get_longest_substring(remaining_string, k)

    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring

assert get_longest_substring('abcba', 2) == 'bcb'
assert get_longest_substring('abbbccbca', 2) == 'bbbccbc'
assert get_longest_substring('cbbbcaba', 1) == 'c'
assert get_longest_substring('aabbcaaczzbb', 3) == 'aabbcaac'
