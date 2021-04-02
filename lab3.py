import lab2
import math

T = 1390
K1 = 3
K2 = 3


def get_T(t, p_sys):
    return round((-1) * t / math.log(p_sys))


def get_g_(revsys, sys):
    return round(revsys / sys, 2)


def pr_reverse_result(p, q, t):
    print("Preversed_system = ", p)
    print("Qreversed_system = ", q)
    print("Treversed_system = ", t)


def pr_winning_reliability(q, p, t):
    print("G_q = ", q)
    print("G_p = ", p)
    print("G_t = ", t)


def common_(parameter, K):
    print('Common', parameter, '->')
    print("-" * 16)
    if parameter == 'load':
        p_revsystem = 1 - math.pow(1 - p_system, K + 1)
        q_revsystem = 1 - p_revsystem
    elif parameter == 'unload':
        q_revsystem = q_system / math.factorial(K + 1)
        p_revsystem = 1 - q_revsystem
    else:
        print("Choose the right parameter!")
        return

    t_revsystem = get_T(T, p_revsystem)
    pr_reverse_result(p_revsystem, q_revsystem, t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    pr_winning_reliability(g_q, g_p, g_t)


def distribute_(parameter, K):
    newP = []
    newQ = []
    print('Distribute', parameter, '->')
    print("-" * 20)

    if parameter == 'load':
        for i in range(len(lab2.P)):
            newP.append(1 - math.pow(1 - lab2.P[i], K + 1))
            newQ.append(1 - newP[i])
    elif parameter == 'unload':
        for i in range(len(lab2.P)):
            newP.append(1 - (1 - lab2.P[i]) / math.factorial(K + 1))
            newQ.append(1 - newP[i])
    else:
        print("Choose the right parameter!")
        return

    lab2.P = newP
    p_revsystem = lab2.get_probability(lab2.work_path, lab2.scheme_size)

    q_revsystem = 1 - p_revsystem
    t_revsystem = get_T(T, p_revsystem)
    pr_reverse_result(p_revsystem, q_revsystem, t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    pr_winning_reliability(g_q, g_p, g_t)


def do_task(task):
    print("_" * 40)
    if task[0] == 'common':
        common_(parameter=task[1], K=task[2])
    elif task[0] == 'distribute':
        distribute_(parameter=task[1], K=task[2])


if __name__ == '__main__':
    task1 = ['common', 'load', K1]
    task2 = ['common', 'unload', K2]

    p_system = lab2.p_system
    q_system = 1 - p_system
    t_system = get_T(T, p_system)
    print("Psystem: ", p_system)
    print("Qsystem: ", q_system)
    print("Tsystem: ", t_system)

    do_task(task1)
    do_task(task2)
