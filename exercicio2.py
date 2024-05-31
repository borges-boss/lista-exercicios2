vector = [10, 20, 30, 40, 50, 30, 60, 70, 80, 90, 100, 30, 120, 130, 140]
pos = []

for i in range(len(vector)):
    if vector[i] == 30:
        pos.append(i)

if len(pos) > 0:
    print("\nO número 30 aparece nas seguintes posições: ", pos)
else:
    print("\nO número 30 não aparece no vetor.")