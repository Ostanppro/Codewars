# https://www.codewars.com//kata/61e2edfeaf28c2001b57af98

def subsequence_sums(a, qs):
    cumulated, staggered = [0], [0]
    for i, n in enumerate(a, 1):
        cumulated.append(cumulated[-1] + n)
        staggered.append(staggered[-1] + n * i)
    return [staggered[e] - staggered[s-1]
            - (s-1) * (cumulated[e] - cumulated[s-1])
            for s, e in qs]