db = [32, 314, 3, 755, 407, 439, 59, 1036, 142,
      631, 317, 1175, 1991, 1329, 68, 126, 31,
      420, 229, 173, 188, 938, 326, 1802, 424, 10,
      668, 266, 1, 442, 459, 341, 293, 227, 104,
      866, 110, 798, 70, 379, 355, 1232, 115, 230,
      928, 2183, 387, 40, 903, 947, 169, 1733,
      217, 628, 230, 871, 1360, 512, 19, 19, 359,
      34, 575, 152, 741, 244, 379, 80, 401, 225,
      334, 1301, 227, 335, 345, 2268, 1049, 354,
      13, 441, 923, 995, 223, 350, 617, 2101, 174,
      1852, 601, 335, 308, 1763, 273, 658, 499,
      1027, 135, 8, 384, 3460]

db.sort()
y = 0.76
t_pr_tr_op = 1914
t_fail_rate = 489

n = len(db)
Tcp = sum(db) / len(db)

k = 10
h = (db[-1] - 0) / k

intervals = [round(_ * h, 1) for _ in range(1, k + 1)]
print("Intervals= ", intervals)


def find_the_interval(number, intervals):
    for i in range(k):
        if intervals[i] <= number <= intervals[i + 1]:
            return i


Ni = [0] * 10
for i in range(len(db)):
    for j in range(len(intervals)):
        if intervals[j] >= db[i]:
            Ni[j] += 1
            continue
N = [Ni[0]]
for i in range(1, len(Ni)):
    N.append(Ni[i] - Ni[i - 1])
print("N(i)= ", N)

f = [round(N[_] / (h * n), 6) for _ in range(len(intervals))]
print("f(i)= ", f)

P = [0 for _ in range(k)]
for i in range(k):
    square = 0
    for j in range(i + 1):
        square += (f[j] * h)
    P[i] = round(1 - square, 5)
print("P(t)= ", P, "\n")

d_01 = round((P[0] - y) / (P[0] - 1), 2)
print("d(1,0)= ", d_01)
T_y = round(h - h * d_01, 2)
print("Tγ= ", T_y)


def probability_for_time(time, frequency_arr, intervals):
    number_of_interval = find_the_interval(time, intervals)
    square = 0
    for i in range(number_of_interval + 1):
        if i != number_of_interval:
            square += (frequency_arr[i] * h)
        else:
            square += (frequency_arr[i] * (time - intervals[i]))
    p = round(1 - square, 4)
    return p


intervals.insert(0, 0)
pr_tr_op = probability_for_time(t_pr_tr_op, f, intervals)
print("P= ", round(pr_tr_op, 4))


def intensity_for_time(time, frequency_arr, intervals):
    number_of_interval = find_the_interval(time, intervals)
    p = probability_for_time(time, frequency_arr, intervals)
    return round(frequency_arr[number_of_interval] / p, 4)


fail_rate = intensity_for_time(t_fail_rate, f, intervals)
print("λ= ", fail_rate)
