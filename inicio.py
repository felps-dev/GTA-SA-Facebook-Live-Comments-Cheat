import requests
import json
import time
from fbtoken import TOKEN_ID
from cheats import cheat_list
from datetime import datetime
from directinput import executar_cheat

#variáveis
print("FELPS 2019 PORRA\n")
print("Insira o ID da LIVE")
VIDEO_ID = input()
URL = "https://streaming-graph.facebook.com/" + VIDEO_ID + "/live_comments"
CPM = 50
PARAMETROS = {'access_token': TOKEN_ID, 'comment_rate':'ten_per_second'}
last_ID = ''
queued_ids = []
cheat_rate = 0

def pode_cheatar(user_id):
    result = False
    id_index = -1
    for i, qid in enumerate(queued_ids):
        if qid['id'] == user_id:
            id_index = i
    if id_index != -1:
        #Está registrado
        segundos_faltado = (datetime.now() - queued_ids[id_index]['time']).total_seconds()
        if segundos_faltado >= cheat_rate:
            result = True
            queued_ids[id_index]['time'] = datetime.now()
        else:
            result = False
            print(str(user_id) + ' ainda não pode realizar cheats. ' + str(cheat_rate - segundos_faltado) + 's faltando.')
    else:
        #não está
        queued_ids.append({'id':user_id,'time':datetime.now()})
        result = True
    return result


#REQUEST para conseguir os comentarios
r = requests.get(URL, params = PARAMETROS, stream=True)
for raw in r.iter_lines():
    if raw:
        raw_dec = raw.decode("utf-8")
        if len(raw_dec) > 6:
            comentario = json.loads(raw_dec[6:len(raw_dec)])
            view_id = comentario['view_id']
            mensagem = comentario['message']
            if comentario['message'] in cheat_list:
                #Processar o cheat.
                if pode_cheatar(comentario['view_id']):
                    #Pode realizar o cheat
                    if executar_cheat(mensagem[1:len(mensagem)]):
                        print(str(comentario['view_id']) + ' FEZ O CHEAT ' + mensagem)
                    else:
                        print(str(comentario['view_id']) + ' ERRO NO CHEAT ' + mensagem)
