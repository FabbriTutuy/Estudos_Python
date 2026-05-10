import math
a = float(input('Digite o ângulo que você desejar '))
seno = math.sin(math.radians(a))
print ('O ângulo {} tem o SENO  de {:.2f} .'.format(a , seno))
c = math.cos(math.radians(a))
print ('O ângulo de {} tem COSSENO de {2:.f} .'.format(a ,c ))
t = math.tan(math.radians(a))
print ('O ângulo {} tem o TANGENTE {:.2f}'.format(a , t))
