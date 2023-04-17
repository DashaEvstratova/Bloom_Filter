import math

from bloom_filter import BloomFilter

def add_text_in_bloom_filter(text):
    text = text.strip().split(' ')
    res = set()
    for i in text:
        if i[-1] == '.' or i[-1] == ',' or i[-1] == '!' or i[-1] == '?':
            res.add(i[:-1:])
        else:
            res.add(i)
    p = 0.08
    m = len(res)
    n = int(((math.log(p, 2))/math.log(2, math.e)) * (-m))+1
    k = int((n/m)*math.log(2, math.e))
    bloom_fil = BloomFilter(n, k, m)
    for i in res:
        bloom_fil.add(i)
    return bloom_fil
