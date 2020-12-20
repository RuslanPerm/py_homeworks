n, m = map(int, input().split())

information, self_way_to_self = [], 0
min_way, row = {}, {}
for i in range(m):
    weight, v1, v2 = map(int, input().split())
    information.append([v1, v2, weight])
for i in range(n):
    ways_long = {}
    for j in information:
        jc = j.copy()
        if i in jc[:2]:
            jc.remove(i)
            ways_long[jc[0]] = jc[1]
    row[i] = ways_long

unvisited_picks = {}
visited_picks = {}
start = int(input())

for i in row.keys():
    unvisited_picks[i] = None
    min_way[i] = []

unvisited_picks[start] = self_way_to_self
min_way[start] = [start]

while True:
    for neighbour, dist in row[start].items():
        if neighbour not in unvisited_picks:
            continue
        new_way = self_way_to_self + dist
        a = min_way[start].copy()
        if unvisited_picks[neighbour] is None or unvisited_picks[neighbour] > new_way:
            a.append(neighbour)
            min_way[neighbour] = a
            unvisited_picks[neighbour] = new_way

    visited_picks[start] = self_way_to_self
    del unvisited_picks[start]
    if not unvisited_picks:
        break
    variants = []
    for k in unvisited_picks.items():
        if k[1]:
            variants.append(k)
    start, self_way_to_self = sorted(variants, key=lambda x: x[1])[0]
print(min_way)
print(visited_picks)