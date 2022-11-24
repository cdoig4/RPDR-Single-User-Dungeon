import itertools

question_1 = ['Contouring', 'Other makeup thing', 'Another makeup thing']
permutations = list(itertools.permutations(question_1))

print("Choose the correct order of the %d permutations below: " % len(permutations))

for sequence_number, permutation in enumerate(permutations, 1):
    print("%d:\t%s" % (sequence_number, permutation))