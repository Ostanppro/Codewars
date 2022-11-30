# https://www.codewars.com//kata/585ba6dff59b3cef3f000132

def reduce_by_rules(lst, rules):
    rule, result = 0, lst[0]
    for i in range(1, len(lst)):
        result = rules[rule % len(rules)](result, lst[i])
        rule += 1
    return result