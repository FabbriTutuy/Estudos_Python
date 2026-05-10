from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)

print("Os valores sorteados foram: ", end="")

for numeros in n :
    print(f"{numeros} " , end="")

print(f"\nO maior número sorteado foi {max(n)}")
print(f"O menor número sorteado foi: {min(n)}")