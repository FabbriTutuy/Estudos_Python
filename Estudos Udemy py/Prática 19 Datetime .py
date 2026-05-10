
import datetime

agora = datetime.datetime.now()
agora_hora = agora.time()
data_hoje = datetime.date.today()
futuro = data_hoje + datetime.timedelta(days=10)

print(agora)
print(futuro)
print(type(agora))
print(agora_hora)