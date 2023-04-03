import zlib
import math


class BloomFilter:
    def __init__(self, len_of_bloom_filter: int):
        self.array = []
        self.bloom_array = []
        self.n = len_of_bloom_filter
        for i in range(0, self.n):
            self.bloom_array.append(0)

    def __str__(self):
        return f"array is: {self.array}, bloom filter is: {self.bloom_array}"

    def _make_hash(self, word):
        adler32 = zlib.adler32(word.encode("utf-8")) % self.n
        crc32 = zlib.crc32(word.encode("utf-8")) % self.n
        return [adler32, crc32]

    def add(self, word):
        res = self._make_hash(word)
        self.bloom_array[res[0]] = 1
        self.bloom_array[res[1]] = 1
        self.array.append(word)
        return True

    def check_filter(self, word):
        res = self._make_hash(word)
        probability_false_positive = 0
        availability = False
        if self.bloom_array[res[0]] == 1 and self.bloom_array[res[1]] == 1:
            availability = True
            probability_false_positive = (
                1 - (math.e ** ((-2 * len(self.array)) / self.n))
            ) ** 2
        if availability:
            return probability_false_positive
        else:
            return False
