def count_matching_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example list of strings
string_list = ['aba', 'xyz', '1221', 'level', 'radar', 'hello', 'a', 'ab', 'fgf']

# Counting matching strings
matching_count = count_matching_strings(string_list)

print("Expected Result :", matching_count)
