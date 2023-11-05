from aocd import get_data, submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)
masses = list(map(int, puzzle.input_data.split('\n')))

answer_a = sum(list(map(lambda n: n // 3 - 2, masses)))
submit(answer_a, part="a", day=1, year=2019)

def cost(mass):
    fuel = mass // 3 - 2
    if (fuel) <= 0:
        return 0
    else:
        return fuel + cost(fuel)

answer_b = sum(list(map(cost, masses)))
submit(answer_b, part="b", day=1, year=2019)