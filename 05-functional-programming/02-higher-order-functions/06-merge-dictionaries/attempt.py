# Write a function `merge_dictionaries(d1, d2, merge_function)` that returns a new dictionary using the following rules:

# * If a key only appears in `d1`, simply copy it and its corresponding value to the resulting dictionary.
# * Same for `d2`.
# * If a key `k` appears both in `d1` and `d2`, then the corresponding values `d1[k]` and `d2[k]` are fed to `merge_function`.
#   This becomes the value for `k` in the resulting dictionary.

def merge_dictionaries(d1, d2, merge_function):
    result = dict(d1)
    for k, v in d2.items:
        if k in result:
            result[k] += merge_function(result[k], v)
        else:
            result[k] = v
    return result        