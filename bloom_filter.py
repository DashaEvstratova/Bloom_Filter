import zlib
import math


class BloomFilter:
    def __init__(self, len_of_bloom_filter: int, k:int, m:int):
        self.array = []
        self.bloom_array = []
        self.n = len_of_bloom_filter
        self.k = k
        self.m = m
        for i in range(0, self.n):
            self.bloom_array.append(0)

    def __str__(self):
        return f"array is: {self.array}, bloom filter is: {self.bloom_array}"

    def _make_hash(self, word):
        res = []
        for i in range(1, self.k+1):
            x = (ord(word[0])+ord(word[-1])*i) % self.n
            res.append(x)
        return res

    def add(self, word):
        res = self._make_hash(word)
        for i in range(0, self.k):
            self.bloom_array[res[i]] = 1
            self.array.append(word)
        return True

    def check_filter(self, word):
        res = self._make_hash(word)
        probability_false_positive = 0
        availability = False
        c = 0
        for i in range(0, self.k):
            if self.bloom_array[res[i]] == 1:
                c +=1
        if c == self.k:
            availability = True
            probability_false_positive = (
                1 - (math.e ** ((-self.k * self.m) / self.n))
            ) ** self.k
        if availability:
            return probability_false_positive
        else:
            return False
