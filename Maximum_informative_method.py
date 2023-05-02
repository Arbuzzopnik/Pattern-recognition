import numpy as np
import math


def ent(param):
    return param * (- math.log2(param))


def get_max(param_P, param_I, param_pi):
    maximum = 0
    for i in range(len(param_P)):
        for j in param_P[i]:
            param_I[i] += ent(j)
        if param_I[i] > maximum:
            maximum_index = i
            maximum = param_I[i]
    param_pi.append(maximum_index)
    return param_I, param_pi


def get_first_cic(D):
    first_cic = [[] for _ in range((len(D) - 1) * 2)]
    for i in range(len(D[0])):
        for j in range(len(D)):
            if D[j][i] == 0:
                first_cic[i * 2].append(j)
            else:
                first_cic[(i * 2) + 1].append(j)
    return first_cic


def get_propability(first_cic, probabilities):
    P = [[0] * 2 for i in range(int(len(first_cic) / 2))]
    for i in range(0, len(first_cic), 2):
        for j in first_cic[i]:
            P[int(i / 2)][0] += probabilities[j]
        for j in first_cic[i + 1]:
            P[int(i / 2)][1] += probabilities[j]
    return P


def show_propability_info(first_cic):
    count = 1
    count_pi = 1
    for i in first_cic:
        print(
            f'π{int(count_pi)} = {int((count - 1)) % 2} при S={i}; P(π{int(count_pi)} = {int((count - 1)) % 2}) = {P[int(count_pi) - 1][int((count - 1)) % 2]} ')
        count += 1
        count_pi += 0.5
    print('')


def show_informative_info(I,number_of_pi):
    for i in range(len(I)):
        if I[i] != 0:
            print(f'I{i + 1} = {I[i]}')
    print(f'Наибольшая информативность у π{number_of_pi + 1}\n')


def start_data():
    probabiliti = [[0.0483, 0.0234, 0.0315, 0.0748, 0.0658, 0.7563],
                   [0.0518, 0.0166, 0.0251, 0.0611, 0.0338, 0.8116],
                   [0.008, 0.0161, 0.0593, 0.0503, 0.078, 0.7883],
                   [0.0246, 0.06, 0.0163, 0.0332, 0.0693, 0.7967],
                   [0.0518, 0.0166, 0.0338, 0.0251, 0.0611, 0.8116],
                   [0.0412, 0.05, 0.0681, 0.0327, 0.0242, 0.7837],
                   [0.0087, 0.0177, 0.0268, 0.0361, 0.0455, 0.8653],
                   [0.0416, 0.0505, 0.0595, 0.033, 0.0245, 0.7909],
                   [0.0175, 0.0547, 0.0265, 0.0357, 0.0087, 0.8569],
                   [0.0242, 0.0499, 0.0773, 0.0588, 0.0079, 0.7818]]

    variants = [[[0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 1, 1, 0],
                 [1, 0, 1, 1, 0],
                 [1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 1, 1, 0],
                 [1, 0, 1, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 1, 1, 0],
                 [1, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 1, 0, 0],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 0, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 0, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 1, 0, 0, 0],
                 [1, 0, 0, 1, 0],
                 [1, 1, 0, 1, 0],
                 [1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]],

                [[0, 1, 0, 0, 1],
                 [1, 0, 1, 0, 0],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1]]]

    t = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
         [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    return probabiliti, variants, t


def status(m, k, t, checks):
    for i in range(k):
        checks.append(t[m][-k + i])
    return checks


def get_informative(pi_list, D, checks, probabilities, I):
    for i in range(5):
        ans = 0
        if i in pi_list:
            continue
        for j in range(6):
            flag = False
            if D[j][i] == checks[0]:
                flag = True
                for n in range(1, k):
                    if D[j][pi_list[-k + n]] != checks[n]:
                        flag = False
                        break
            if flag:
                ans += probabilities[j]
        if ans != 0:
            I[i] += ent(ans)
    return I


def show_results(pi_list):
    for i in range(len(pi_list)):
        pi_list[i] += 1
    print('искомое множество проверок: π', end='')
    print('{', *pi_list, '}')


if __name__ == '__main__':
    probabiliti, variants, t = start_data()
    variant = 15
    D = variants[variant % 10 - 1]
    probabilities = probabiliti[variant % 10 - 1]
    I = [0] * (len(D) - 1)
    pi_list = []

    H = sum([ent(i) for i in probabilities])
    first_cic = get_first_cic(D)
    P = get_propability(first_cic, probabilities)
    I, pi_list = get_max(P, I, pi_list)
    show_propability_info(first_cic)
    show_informative_info(I,pi_list[0])

    for k in range(2, len(D[0])):
        checks = []
        I = [0] * (len(D) - 1)
        for m in range(2 ** k):
            checks = status(m, k, t, checks)
            print(checks)
            I = get_informative(pi_list, D, checks, probabilities, I)
            checks.clear()
        maximum = 0
        for i in range(len(I)):
            if I[i] > maximum:
                maximum = I[i]
                maximum_index = i
        pi_list.append(maximum_index)
        show_informative_info(I,maximum_index)
        if maximum == H:
            break
    show_results(pi_list)



