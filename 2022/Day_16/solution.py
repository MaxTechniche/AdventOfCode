import pytest
import re
from time import perf_counter


def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        if time_delta * 1000 < 1:
            print(str(time_delta * 1000000)[:6], "μs")
        elif time_delta < 1:
            print(str(time_delta * 1000)[:6], "ms")
        else:
            print(str(time_delta)[:6], "s")
    return wrapper()


class Valve:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        
    def __repr__(self):
        print(type(self.tunnels[0]))
        return f"Valve {self.name}, flow rate: {self.flow_rate}, tunnels: {[str(tunnel) for tunnel in self.tunnels]}"

    def __str__(self):
        return self.name
    
def graph_it(data):
    valves = dict()
    for line in data.strip().splitlines():
        valve = re.findall(r"Valve \w+", line)[0][6:]
        flow_rate = int(re.findall(r"\d+", line)[0])
        try:
            v = re.findall(r"valves ((\w+[, ]{0,2})*)", line)[0][0].split(", ")
            valves[valve] = Valve(valve, flow_rate, v)
        except IndexError:
            continue

    for valve in list(valves.keys()):
        for i, tunnel in enumerate(valves[valve].tunnels):
            if tunnel in valves:
                valves[valve].tunnels[i] = valves[tunnel]
            else:
                valves[tunnel] = Valve(tunnel, 0, [])  # !
                valves[tunnel].tunnels.append(valves[valve])
                
    for valve in valves.values():
        for i, tunnel in enumerate(valve.tunnels):
            if type(tunnel) == str:
                valve.tunnels[i] = valves[tunnel]
    return valves

MAX_FLOW = {"total_flow": 0}

def solve(valve, turn, rate, total_flow, opened_tunnels=None, actions=("move", "open")):
    if opened_tunnels is None:
        opened_tunnels = set()
    total_flow += rate
    if turn == 0:
        if total_flow > MAX_FLOW["total_flow"]:
            MAX_FLOW["total_flow"] = total_flow
            print("new max", MAX_FLOW["total_flow"])
    elif turn < 0:
        return
    tunnels = sorted(valve.tunnels, key=lambda x: (x not in opened_tunnels, x.flow_rate), reverse=True)
    for tunnel in tunnels:
        for action in actions:
            if action == "move":
                solve(tunnel, turn-1, rate, total_flow, opened_tunnels, ("move", "open"))
            elif action == "open":
                if tunnel in opened_tunnels:
                    continue
                opened_tunnels.add(tunnel)
                rate += tunnel.flow_rate
                solve(tunnel, turn-1, rate, total_flow, opened_tunnels, ("move"))
                rate -= tunnel.flow_rate
                opened_tunnels.remove(tunnel)
                

def compute1(data):
    valves = graph_it(data)
    AA = valves["AA"]
    
    solve(AA, 30, 0, 0)
    print(MAX_FLOW["rate"])
    return MAX_FLOW["rate"]

def compute2(data):
    pass


def main():
    with open("2022/Day_16/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""", 1651),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("", 0),
    ])
@pytest.mark.skip
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
