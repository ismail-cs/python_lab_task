d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}

# Combine values for common keys
for key in d1.keys():
    if key in d2:
        combined_dict[key] = d1[key] + d2[key]
    else:
        combined_dict[key] = d1[key]

# Add keys from d2 not present in d1
for key in d2.keys():
    if key not in d1:
        combined_dict[key] = d2[key]

print("Sample output:", combined_dict)
