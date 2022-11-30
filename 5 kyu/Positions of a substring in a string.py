# https://www.codewars.com//kata/59f3956825d575e3330000a3

import re

conv = 'AA CC GG TT RGA YCT MAC KGT SGC WAT BCGT DAGT HACT VACG NACGT'
table = {c: f"[{''.join(grp)}]" for c, *grp in conv.split()}

def get_pos(base, strng, query):
    base = dict(re.findall(r'^(\w+).*\s+(\w+) ?$', base, re.M))
    if query not in base: return "This query name does not exist in given Base"
    return ' '.join(str(m.start() + 1) for m in
        re.finditer(''.join(map(table.get, base[query])), strng.upper())) \
        or f"{query} is not in given string"