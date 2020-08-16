import bisect


def prefix_query(prefix, strs):
    dictionary = [dic.lower() for dic in sorted(strs)]

    _next_key = prefix[:-1] + chr(ord(prefix[-1])+1)
    return dictionary[bisect.bisect(dictionary, prefix):bisect.bisect(dictionary, _next_key)]

strs = ['dog', 'deer', 'deal' , 'ddong']
prefix = 'de'
print(prefix_query(prefix, strs))