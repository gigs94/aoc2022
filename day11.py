from aocd import lines
import math
import time


test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def monk_stats(t):
    monkies = []
    ops = ["+", "-", "*"]
    monk = {
        "items": {},
        "op": None,
        "ov1": 0,
        "ov2": 0,
        "test": 0,
        "t": 0,
        "f": 0,
        "inspected": 0,
    }
    for tt in t:
        l = tt.split()
        if len(l) == 0:
            monkies.append(monk)
            monk = {
                "items": {},
                "op": None,
                "ov1": 0,
                "ov2": 0,
                "test": 0,
                "t": 0,
                "f": 0,
                "inspected": 0,
            }
        elif l[0] == "Monkey":
            monkey = l[1]
        elif l[0] == "Starting":
            monk["items"] = [int(x.strip(",")) for x in l[2:]]
            monk["items"].reverse()
        elif l[0] == "Operation:":
            # '''Operation: new = old * old'''
            monk["ov1"] = l[3]
            monk["op"] = l[4]
            monk["ov2"] = l[5]
        elif l[0] == "Test:":
            monk["test"] = int(l[3])
        elif l[1] == "true:":
            monk["t"] = int(l[5])
        elif l[1] == "false:":
            monk["f"] = int(l[5])

    monkies.append(monk)

    return monkies


def observe_monks(monkies, worry, cw):
    for n, m in enumerate(range(len(monkies))):
        monk = monkies[m]
        for _ in range(len(monk["items"])):
            i = monk["items"].pop()
            one = i if monk["ov1"] == "old" else monk["ov1"]
            two = i if monk["ov2"] == "old" else monk["ov2"]
            wla = eval(f'{one}{monk["op"]}{two}')
            wla = wla % cw if worry else wla // 3
            test = wla % int(monk["test"]) == 0
            monkies[monk["t"]]["items"].append(wla) if test else monkies[monk["f"]][
                "items"
            ].append(wla)
            monk["inspected"] += 1


def run(t, rounds, worry):
    monkies = monk_stats(t)

    cw = math.prod([m["test"] for m in monkies])
    print(f"{cw}")

    tic = time.perf_counter()
    for i in range(rounds):
        observe_monks(monkies, worry, cw)
        if i % 1000 == 0:
            toc = time.perf_counter()
            print(f"@{i} {toc - tic:0.4f} seconds")
            tic = time.perf_counter()

    inspections = sorted([i["inspected"] for i in monkies], reverse=True)
    print(f"answer: {inspections[0]*inspections[1]}")


t = test.splitlines()
run(t, 20, False)
run(t, 10000, True)
run(lines, 10000, True)
