from aiohttp.client import *
from aiohttp import payload, web
from aiohttp.client import request
from random import choice
import os

HOST_IP = "0.0.0.0"
HOST_PORT = 1288

state = 0 

def handler_function(request):
    global state
    global using
    global rec
    global mat
    buttons = []
    end_session = False
    message = ''
    tts = ''
    session = request['session']
    version = request['version']
    request = request['request']
    list_of_request = request['nlu']['tokens']

### Start
    if session['new'] or state == 0:
        with open('using.txt', newline='', encoding="utf-8") as using:   
            using = using.readlines()

        with open('recycling.txt', newline='', encoding="utf-8") as rec:   
            rec = rec.readlines()

        with open('materials.txt', newline='', encoding="utf-8") as mat:   
            mat = mat.readlines()

        message = "Привет! Чтобы узнать, можно ли переработать материал, просто введи его код или идентификатор"  
        tts = "^Привет^! Чтобы узнать, можно ли переработать материал, просто введи его код или идентификатор" 
        buttons = [button('Что такое код?'), button('Что такое идентификатор?')]
        state = 10

    ### Start    
    elif state == 10:

        if 'код' in list_of_request:
            message = ("Код переработки — это треугольник с цифрой внутри. Цифры обозначают материал, из которого сделан предмет")
            tts = "Код переработки — это треугольник с цифрой внутри. Цифры обозначают материал, из которого сделан предмет"

        elif 'идентификатор' in list_of_request:
            message = ('Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником с цифрой внутри')
            tts = 'Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником с цифрой внутри'

        elif 'спасибо' in list_of_request or 'стоп' in list_of_request or 'выход' in list_of_request or 'не' in list_of_request or 'заверши' in list_of_request or 'пока' in list_of_request:
            state = 100

### Main part

# Plastic
        elif 'один' in list_of_request or '01' in list_of_request or '1' in list_of_request or 'пэт' in list_of_request or 'pet' in list_of_request or 'pete' in list_of_request:
            message = mat[0] + '\n'+ "Использование: " + using[0] + '\n' + rec[0]
            tts = message

        elif 'два' in list_of_request or '02' in list_of_request or '2' in list_of_request or 'пэ' in list_of_request or 'пнд' in list_of_request or 'пэвп' in list_of_request or 'ашдипии' in list_of_request or 'хдпе' in list_of_request or 'hdpe' in list_of_request or 'pehd' in list_of_request:
            message = mat[1] + '\n' + "Использование: " + using[1] + '\n'+ rec[1]
            tts = message

        elif 'три' in list_of_request or '03' in list_of_request or '3' in list_of_request or 'пвх' in list_of_request or 'пвс' in list_of_request or 'пвк' in list_of_request or 'pvc' in list_of_request:
            message = mat[2] + '\n' + "Использование: " + using[2] + '\n'+ rec[2]
            tts = message

        elif 'четыре' in list_of_request or '04' in list_of_request or '4' in list_of_request or 'пвд' in list_of_request or 'пэнп' in list_of_request or 'лдпе' in list_of_request or 'ldpe' in list_of_request or 'peld' in list_of_request:
            message = mat[3] + '\n' + "Использование: " + using[3] + '\n'+ rec[3]
            tts = message

        elif 'пять' in list_of_request or '05' in list_of_request or '5' in list_of_request or 'пп' in list_of_request or 'pp' in list_of_request or 'рр' in list_of_request:
            message = mat[4] + '\n' + "Использование: " + using[4] + '\n'+ rec[4]
            tts = message

        elif 'шесть' in list_of_request or '06' in list_of_request or '6' in list_of_request or 'пс' in list_of_request or 'ps' in list_of_request:
            message = mat[5] + '\n' + "Использование: " + using[5] + '\n'+ rec[5]
            tts = message

        elif 'семь' in list_of_request or '07' in list_of_request or '7' in list_of_request or 'о' in list_of_request or 'o' in list_of_request or 'other' in list_of_request or 'другое' in list_of_request:
            message = mat[6] + '\n' + "Использование: " + using[6] + '\n'+ rec[6]
            tts = message

        elif 'абс' in list_of_request or 'abs' in list_of_request:
            message = mat[7] + '\n' + "Использование: " + using[7] + '\n'+ rec[7]
            tts = message

        elif 'пк' in list_of_request or 'рс' in list_of_request or 'pc' in list_of_request:
            message = mat[8] + '\n' + "Использование: " + using[8] + '\n'+ rec[8]
            tts = message
    
# Paper
        elif 'двадцать' in list_of_request or '20' in list_of_request:
            message = mat[9] + '\n' + "Использование: " + using[9] + '\n'+ rec[9]
            tts = message

        elif 'двадцать один' in list_of_request or '21' in list_of_request:
            message = mat[10] + '\n' + "Использование: " + using[10] + '\n'+ rec[10]
            tts = message

        elif 'двадцать два' in list_of_request or '22' in list_of_request:
            message = mat[11] + '\n' + "Использование: " + using[11] + '\n'+ rec[11]
            tts = message

        elif 'двадцать три' in list_of_request or '23' in list_of_request:
            message = mat[12] + '\n' + "Использование: " + using[12] + '\n'+ rec[12]
            tts = message
        
        elif 'пэп' in list_of_request or 'пап' in list_of_request or 'рар' in list_of_request or 'pap' in list_of_request:
            message = "Целлюлозная продукция (гофрированный картон, картон, бумага)." + '\n\n' + "Использование: Коробки, открытки, журналы, газеты, офисная бумага." + '\n' + rec[9]
            tts = message

# Metals
        elif 'сорок' in list_of_request or 'фу' in list_of_request or '40' in list_of_request or 'fu' in list_of_request:
            message = mat[13] + '\n' + "Использование: " + using[13] + '\n'+ rec[13]
            tts = message

        elif 'сорок' in list_of_request or '41' in list_of_request or 'ал' in list_of_request or 'al' in list_of_request or 'алу' in list_of_request or 'alu' in list_of_request:
            message = mat[14] + '\n' + "Использование: " + using[14] + '\n'+ rec[14]
            tts = message
        
# Organic materials of natural origin
        elif 'пятьдесят' in list_of_request or '50' in list_of_request or 'for' in list_of_request or 'фор' in list_of_request:
            message = mat[15] + '\n' + "Использование: " + using[15] + '\n'+ rec[15]
            tts = message

        elif 'пятьдесят один' in list_of_request or '51' in list_of_request:
            message = mat[16] + '\n' + "Использование: " + using[16] + '\n'+ rec[16]
            tts = message
        
        elif 'шестьдесят' in list_of_request or '60' in list_of_request or 'tex' in list_of_request or 'текс' in list_of_request:
            message = mat[17] + '\n' + "Использование: " + using[17] + '\n'+ rec[17]
            tts = message

        elif 'шестьдесят один' in list_of_request or '61' in list_of_request:
            message = mat[18] + '\n' + "Использование: " + using[18] + '\n'+ rec[18]
            tts = message

# Glass
        elif 'семьдесят' in list_of_request or '70' in list_of_request:
            message = mat[19] + '\n' + "Использование: " + using[19] + '\n'+ rec[19]
            tts = message
        
        elif 'семьдесят один' in list_of_request or '71' in list_of_request:
            message = mat[20] + '\n' + "Использование: " + using[20] + '\n'+ rec[20]
            tts = message

        elif 'семьдесят два' in list_of_request or '72' in list_of_request:
            message = mat[21] + '\n' + "Использование: " + using[21] + '\n'+ rec[21]
            tts = message
        
        elif 'семьдесят три' in list_of_request or '73' in list_of_request:
            message = mat[22] + '\n' + "Использование: " + using[22] + '\n'+ rec[22]
            tts = message

        elif 'семьдесят четыре' in list_of_request or '74' in list_of_request:
            message = mat[23] + '\n' + "Использование: " + using[23] + '\n'+ rec[23]
            tts = message
        
        elif 'семьдесят пять' in list_of_request or '75' in list_of_request:
            message = mat[24] + '\n' + "Использование: " + using[24] + '\n'+ rec[24]
            tts = message

        elif 'семьдесят шесть' in list_of_request or '76' in list_of_request:
            message = mat[25] + '\n' + "Использование: " + using[25] + '\n'+ rec[25]
            tts = message

        elif 'семьдесят семь' in list_of_request or '77' in list_of_request:
            message = mat[26] + '\n' + "Использование: " + using[26] + '\n'+ rec[26]
            tts = message
        
        elif 'семьдесят восемь' in list_of_request or '78' in list_of_request:
            message = mat[27] + '\n' + "Использование: " + using[27] + '\n'+ rec[27]
            tts = message

        elif 'семьдесят девять' in list_of_request or '79' in list_of_request:
            message = mat[28] + '\n' + "Использование: " + using[28] + '\n'+ rec[28]
            tts = message
        
# Composite materials
        elif 'восемьдесят один' in list_of_request or '81' in list_of_request:
            message = mat[29] + '\n' + "Использование: " + using[29] + '\n'+ rec[29]
            tts = message

        elif 'восемьдесят два' in list_of_request or '82' in list_of_request:
            message = mat[30] + '\n' + "Использование: " + using[30] + '\n'+ rec[30]
            tts = message
        
        elif 'восемьдесят четыре' in list_of_request or '84' in list_of_request:
            message = mat[31] + '\n' + "Использование: " + using[31] + '\n'+ rec[31]
            tts = message

        elif 'девяносто' in list_of_request or '90' in list_of_request:
            message = mat[32] + '\n' + "Использование: " + using[32] + '\n'+ rec[32]
            tts = message
        
        elif 'девяносто два' in list_of_request or '92' in list_of_request:
            message = mat[33] + '\n' + "Использование: " + using[33] + '\n'+ rec[33]
            tts = message

        elif 'девяносто восемь' in list_of_request or '98' in list_of_request:
            message = mat[34] + '\n' + "Использование: " + using[34] + '\n'+ rec[34]
            tts = message
            
        elif 'эс лдпе' in list_of_request or 'эс алу' in list_of_request or 'эс пап' in list_of_request or 'эс пэпэ' in list_of_request or 'c/pap' in list_of_request or 'с/рар' in list_of_request or 'с/рр' in list_of_request or 'c/pp' in list_of_request or 'c/ldpe' in list_of_request or 'c/alu' in list_of_request:
            message = "Композиционный материал, выполненный из смеси различных материалов" + '\n\n' + "Использование: кофе, соусы, сгущенка, лапша быстрого приготовления, зубная паста, косметический крем" + '\n\n'+ rec[34]
            tts = message

### Another answer
        else:
            message = choice(["Повторите, пожалуйста, ещё раз", "Попробуйте указать число — код материала", "Кажется, такого материала я ещё не знаю"])
            tts = message

### Finish

    if state == 100:
        message = choice(['До новых встреч!', "Спасибо, что интересуетесь экологией!", "Проведите день с пользой!"])
        tts = message
        end_session = True

### Processing responses

    response_message = {
        "response": 
        {
            "text": message,
            "tts": tts,
            "buttons": buttons,
            "end_session": end_session
        },
        "session": 
        {
            derived_key: session[derived_key] for derived_key 
            in ['session_id', 'user_id', 'message_id']
        },
            "version": version
    }
    return response_message

def button(title):
    return {"title": title}

async def skill_eco(request_obj):
    request_message = await request_obj.json()
    response = handler_function(request_message)

    return web.json_response(response)

def init():
    app = web.Application() 
    app.router.add_post("/skill_eco", skill_eco)
    web.run_app(app, host = HOST_IP, port = os.getenv('PORT', 5000))

if __name__ == "__main__":
    init()

