sequence = list(range(1, 101))
modified_sequence = []  # определяем переменную для результата

for sequences in sequence:
    if sequences % 5 == 0 and sequences % 3 == 0:
        modified_sequence.append('FuzzBuzz')
    elif sequences % 5 == 0:
        modified_sequence.append('Buzz')
    elif sequences % 3 == 0:
        modified_sequence.append('Fuzz')
    else:
        modified_sequence.append(str(sequences))

print(', '.join(modified_sequence))
