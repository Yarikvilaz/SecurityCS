def change_to_scheme(graph):
    scheme = {}
    for k, v in graph.items():
        scheme[k - 1] = []
        for i in v:
            scheme[k - 1].append(i - 1)
    return scheme


def dfs(graph, start=0):
    res = []

    def dfs_recursion(start, visited):
        nonlocal res
        visited.append(int(start))

        if len(graph[start]) == 0:
            res.append(list(visited))
            visited.pop()
            return

        for n in graph[start]:
            dfs_recursion(n, visited)

        visited.pop()

    dfs_recursion(start, [])
    return res


def possible_variants(graph_size):
    # making list of all possible variants
    possible_var = []
    for i in range(2 ** graph_size):
        var = []
        tmp = i
        for j in range(graph_size, -1, -1):
            if tmp // (2 ** j) == 1:
                tmp = tmp % (2 ** j)
                var.append(j)
        possible_var.append(sorted(var))
    return possible_var


def workable_pathes(ways, pos_var):
    # making list of all workable pathes
    possible_pathes = []
    for i in pos_var:
        for j in ways:
            if set(j).issubset(set(i)):
                possible_pathes.append(i)
                break
    return possible_pathes


def get_probability(work_path, graph_size):
    # finding P_system
    Ptndv = 0
    for i in work_path:
        temp = 1
        for j in range(graph_size):
            if int(j) in i:
                temp *= P[j]
            else:
                temp *= 1 - P[j]
        Ptndv += temp
    return Ptndv


P = [0.32, 0.82, 0.15, 0.24, 0.66, 0.99, 0.93]

graph = {
    1: [3, 4],
    2: [3, 5, 7],
    3: [4, 5, 7],
    4: [5, 6],
    5: [6, 7],
    6: [],
    7: []
}
scheme = change_to_scheme(graph)
scheme_size = len(scheme)

ways = []
ways1 = dfs(scheme, 0)
ways2 = dfs(scheme, 1)
ways.extend(ways1)
ways.extend(ways2)

print("All ways:")
for i, j in zip(dfs(graph, start=1), dfs(graph, start=2)):
    print(*i, " - ", *j)

pos_var = possible_variants(scheme_size)
work_path = workable_pathes(ways, pos_var)

p_system = get_probability(work_path, scheme_size)
print("\nProbability: ", p_system)
