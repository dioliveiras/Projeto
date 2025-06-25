import datetime

def registrar_log(tipo_tarefa, status_tarefa, duracao):    
    with open('src/logs.txt', 'a') as arquivo:
        agora = datetime.datetime.now()
        arquivo.write(f'[{agora.strftime("%Y-%m-%d %H:%M:%S")}] {tipo_tarefa} {status_tarefa} - {duracao:.3f}s\n')
        


