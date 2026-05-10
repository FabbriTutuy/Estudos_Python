f = str(input('Digite uma frase ')).upper()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('O A aparece pela primeira vez na(o) {} posição'.format(f.find('A')+1))
print('A letra A apareceu pela ultima vez na(o) {} posição'.format(f.rfind('A')+1))
