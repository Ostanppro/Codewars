# https://www.codewars.com/kata/58738d518ec3b4bf95000192

import re
from collections import defaultdict

def execute_rs1(code):
    grid = defaultdict(lambda: " ")
    i, j = 0, 0
    d = complex(0, 1)
    grid[(i, j)] = "*"
    for command, times in re.findall(r"([FLR])(\d*)", code):
        times = int(times) if times else 1
        for _ in range(times):
            if command == "F":
                i += int(d.real)
                j += int(d.imag)
                grid[(i, j)] = "*"
            elif command == "L":
                d *= 1j
            elif command == "R":
                d *= -1j
    min_y = min(y for y, x in grid)
    max_y = max(y for y, x in grid)
    min_x = min(x for y, x in grid)
    max_x = max(x for y, x in grid)
    return "\r\n".join("".join(grid[(y, x)] for x in range(min_x, max_x + 1)) for y in range(min_y, max_y + 1))

def execute(code):
    repl = lambda m: m.group(1) * (int(m.group(2)) if m.group(2) else 1)
    while code != (code_repl := re.sub(r"\((\w*)\)(\d*)", repl, code)):
        code = code_repl
    return execute_rs1(code)