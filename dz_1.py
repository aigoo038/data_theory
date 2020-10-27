from collections import Counter, deque, OrderedDict
import operator

in_str = 'AGGACTAAAAACG'
out_str = dict(Counter(in_str))
temp = out_str.copy()


def encode(dct):

    new_dct = dct.copy()
    for i in new_dct:
        new_dct.update({i: ''})
    while len(dct) > 1:
        sorted_dct = dict(sorted(dct.items(), key=lambda kv: kv[1], reverse=True))
        mins = list(sorted_dct.keys())[len(sorted_dct) - 2:]

        min_1 = mins[0]
        min_2 = mins[1]
        min_val = sorted_dct[min_1]
        min_value = sorted_dct[min_2]
        del sorted_dct[min_2]
        del dct[min_2]

        new_dct.update({min_2: '1' + str(new_dct[min_2])})
        new_dct.update({min_1: '0' + str(new_dct[min_1])})

        dig = min_val + min_value
        sorted_dct.update({min_1: dig})
        dct.update({min_1: dig})

    return new_dct


def frequency(dct):
    length = len(dct)
    for key, value in out_str.items():
        a = value/length
        out_str[key] = a


frequency(in_str)
c = encode(out_str)
print('Input:  ', in_str, '\n')
print("Symbol\tWeight\tHuffman Code")

for p, c in c.items():
    print("%s\t\t%s\t\t%s" % (p[0], temp[p], c))
