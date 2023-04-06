class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = collections.Counter(changed)
        originals = []
        for multiple in count.keys():
            if multiple == 0:
                if count[multiple] % 2 > 0:
                    return []
                originals += [0] * (count[multiple] // 2)

            elif count[multiple] > 0:
                factor = multiple
                while factor % 2 == 0 and factor // 2 in count:
                    factor = factor // 2

                while factor in count:
                    if count[factor] > 0:
                        if count[factor + factor] < count[factor]:
                            return []
                        originals += [factor] * count[factor]
                        count[factor + factor] -= count[factor]
                        count[factor] = 0
                    factor += factor
        return originals
