import numpy as np
from table import Table
from cipher import Solver, CipherText

FREQUENCIES = [0.062321425641578554, 0.012490536584451168, 0.01569462056098424, 0.038945910280960894, 0.09354190740267625, 0.01607432912294354, 0.020204245704253908, 0.05280527279247521, 0.048790206331757464, 0.0008695794844870301, 0.009398958848498628, 0.03420892877651807, 0.01733299268943824, 0.051150493503936544, 0.061266679636136065, 0.013003846307099847, 0.000986773485091751, 0.05073328286178374, 0.046202562798405226, 0.06807565107127037, 0.02286689339799317, 0.00681834695518267, 0.019683904341568945, 0.0009000499246442576, 0.020201901824241815, 0.0006211282032050216, 0.17688324899271757, 0.01438439163422346, 0.013264016988442328, 0.0011133430057448498, 0.0017696294091312877, 0.007469945598544919]

ciphertext_data_input = CipherText(0.35)
letters = "abcdefghijklmnopqrstuvwxyz .,!?\n"

buckets = [[] for i in range(32)]
for i in range(ciphertext_data_input.length()):
    buckets[i%32].append(ciphertext_data_input[i])
bucket_frequencies = [[0 for j in range(32)] for i in range(32)]
for i in range(len(buckets)):
    for character in buckets[i]:
        num = int(character)
        bucket_frequencies[i][num] += 1/len(buckets[i])

def score(actual_frequencies, key_frequencies):
    differences = 0
    for i in range(32):
        differences += actual_frequencies[i]*key_frequencies[i]
    return differences

table = Table()

bestKeys = []
for bucket_freq in bucket_frequencies:
    scores = []
    for key in table.table:
        key_freq_list = []
        for code in key:
            key_freq_list.append(bucket_freq[code])
        scores.append(score(FREQUENCIES, key_freq_list))
    bestKey = scores.index(max(scores))
    bestKeys.append(bestKey)

print(bestKeys)

solver = Solver()
solver.decode_and_print_all(bestKeys)

