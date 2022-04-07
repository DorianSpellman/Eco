from secrets import token_urlsafe
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
    tokens = request['nlu']['tokens']

### Start
    if session['new'] or state == 0:
        with open('using.txt', newline='', encoding="utf-8") as using:   
            using = using.readlines()

        with open('recycling.txt', newline='', encoding="utf-8") as rec:   
            rec = rec.readlines()

        with open('materials.txt', newline='', encoding="utf-8") as mat:   
            mat = mat.readlines()

        message = "Привет! Чтобы узнать, можно ли переработать материал, просто введите его код или идентификатор. Если не знаете, что это, то смело спросите меня!"  
        tts = "^Привет^! Чтобы узнать, можно ли переработать материал, просто введите его код или идентификатор. Если не знаете, что это, то смело спросите меня!" 
        buttons = [button('Что такое код?'), button('Что такое идентификатор?')]
        state = 10

    ### Start    
    elif state == 10:

        if 'код' in tokens or 'кот' in tokens:
            message = ("Код переработки — это треугольник с цифрой внутри. Цифры обозначают материал, из которого сделан предмет")
            tts = "Код переработки — это треугольник с цифрой внутри. Цифры обозначают материал, из которого сделан предмет"

        elif 'второе' in tokens or 'идентификатор' in tokens:
            message = ('Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником с цифрой внутри')
            tts = 'Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником с цифрой внутри'

        elif 'спасибо' in tokens or 'стоп' in tokens or 'выход' in tokens or 'не' in tokens or 'заверши' in tokens or 'пока' in tokens or 'хватит' in tokens:
            state = 100

### Main part

# Paper

        elif ('двадцать' in tokens and 'один' in tokens) or '21' in tokens:
            message = mat[10] + '\n' + "Примеры использования: " + using[10] + '\n'+ rec[10]
            tts = message

        elif ('двадцать' in tokens and 'два' in tokens) or '22' in tokens:
            message = mat[11] + '\n' + "Примеры использования: " + using[11] + '\n'+ rec[11]
            tts = message

        elif ('двадцать' in tokens and 'три' in tokens) or '23' in tokens:
            message = mat[12] + '\n' + "Примеры использования: " + using[12] + '\n'+ rec[12]
            tts = message
        
        elif 'двадцать' in tokens or '20' in tokens:
            message = mat[9] + '\n' + "Примеры использования: " + using[9] + '\n'+ rec[9]
            tts = message
        
        elif 'пэп' in tokens or 'пап' in tokens or 'рар' in tokens or 'pap' in tokens:
            message = "Целлюлозная продукция (гофрированный картон, картон, бумага)." + '\n\n' + "Примеры использования: коробки, открытки, журналы, газеты, офисная бумага." + '\n\n' + rec[9]
            tts = message

# Metals

        elif ('сорок' in tokens and 'один' in tokens) or '41' in tokens or 'ал' in tokens or 'al' in tokens or 'алу' in tokens or 'alu' in tokens:
            message = mat[14] + '\n' + "Примеры использования: " + using[14] + '\n'+ rec[14]
            tts = message

        elif 'сорок' in tokens or 'фу' in tokens or '40' in tokens or 'fu' in tokens:
            message = mat[13] + '\n' + "Примеры использования: " + using[13] + '\n'+ rec[13]
            tts = message
        
# Organic materials of natural origin

        elif ('пятьдесят' in tokens and 'один' in tokens) or '51' in tokens:
            message = mat[16] + '\n' + "Примеры использования: " + using[16] + '\n'+ rec[16]
            tts = message

        elif 'пятьдесят' in tokens or '50' in tokens or 'for' in tokens or 'фор' in tokens:
            message = mat[15] + '\n' + "Примеры использования: " + using[15] + '\n'+ rec[15]
            tts = message

        elif ('шестьдесят' in tokens and 'один' in tokens) or '61' in tokens:
            message = mat[18] + '\n' + "Примеры использования: " + using[18] + '\n'+ rec[18]
            tts = message
        
        elif 'шестьдесят' in tokens or '60' in tokens or 'tex' in tokens or 'текс' in tokens:
            message = mat[17] + '\n' + "Примеры использования: " + using[17] + '\n'+ rec[17]
            tts = message


# Glass
        
        elif ('семьдесят' in tokens and 'один' in tokens) or '71' in tokens:
            message = mat[20] + '\n' + using[20] + '\n'+ rec[20]
            tts = message

        elif ('семьдесят' in tokens and 'два' in tokens) or '72' in tokens:
            message = mat[21] + '\n' + using[21] + '\n'+ rec[21]
            tts = message
        
        elif ('семьдесят' in tokens and 'три' in tokens) or '73' in tokens:
            message = mat[22] + '\n' + using[22] + '\n'+ rec[22]
            tts = message

        elif ('семьдесят' in tokens and 'четыре' in tokens) or '74' in tokens:
            message = mat[23] + '\n' + using[23] + '\n'+ rec[23]
            tts = message
        
        elif ('семьдесят' in tokens and 'пять' in tokens) or '75' in tokens:
            message = mat[24] + '\n' + using[24] + '\n'+ rec[24]
            tts = message

        elif ('семьдесят' in tokens and 'шесть' in tokens) or '76' in tokens:
            message = mat[25] + '\n' + "Примеры использования: " + using[25] + '\n'+ rec[25]
            tts = message

        elif ('семьдесят' in tokens and 'семь' in tokens) or '77' in tokens:
            message = mat[26] + '\n' + using[26] + '\n'+ rec[26]
            tts = message
        
        elif ('семьдесят' in tokens and 'восемь' in tokens) or '78' in tokens:
            message = mat[27] + '\n' + using[27] + '\n'+ rec[27]
            tts = message

        elif ('семьдесят' in tokens and 'девять' in tokens) or '79' in tokens:
            message = mat[28] + '\n' + using[28] + '\n'+ rec[28]
            tts = message

        elif 'семьдесят' in tokens or '70' in tokens:
            message = mat[19] + '\n' + using[19] + '\n'+ rec[19]
            tts = message
        
# Composite materials
        elif ('восемьдесят' in tokens and 'один' in tokens) or '81' in tokens:
            message = mat[29] + '\n' + "Примеры использования: " + using[29] + '\n'+ rec[29]
            tts = message

        elif ('восемьдесят' in tokens and 'два' in tokens) or '82' in tokens:
            message = mat[30] + '\n' + "Примеры использования: " + using[30] + '\n'+ rec[30]
            tts = message
        
        elif ('восемьдесят' in tokens and 'четыре' in tokens) or '84' in tokens:
            message = mat[31] + '\n' + using[31] + '\n'+ rec[31]
            tts = message
       
        elif ('девяносто' in tokens and 'два' in tokens) or '92' in tokens:
            message = mat[33] + '\n' + "Примеры использования: " + using[33] + '\n'+ rec[33]
            tts = message

        elif ('девяносто' in tokens and 'восемь' in tokens) or '98' in tokens:
            message = mat[34] + '\n' + using[34] + '\n'+ rec[34]
            tts = message
        
        elif 'девяносто' in tokens or '90' in tokens:
            message = mat[32] + '\n' + "Примеры использования: " + using[32] + '\n'+ rec[32]
            tts = message
            
        elif 'эс лдпе' in tokens or 'эс алу' in tokens or 'эс пап' in tokens or 'эс пэпэ' in tokens or 'c/pap' in tokens or 'с/рар' in tokens or 'с/рр' in tokens or 'c/pp' in tokens or 'c/ldpe' in tokens or 'c/alu' in tokens:
            message = "Композиционный материал, выполненный из смеси различных материалов" + '\n\n' + "Примеры использования: кофе, соусы, сгущенка, лапша быстрого приготовления, зубная паста, косметический крем" + '\n\n'+ rec[34]
            tts = message

# Plastic
        elif 'один' in tokens or '01' in tokens or '1' in tokens or 'пэт' in tokens or 'pet' in tokens or 'pete' in tokens:
            message = mat[0] + '\n'+ "Примеры использования: " + using[0] + '\n' + rec[0]
            tts = message

        elif 'два' in tokens or '02' in tokens or '2' in tokens or 'пэ' in tokens or 'пнд' in tokens or 'пэвп' in tokens or 'ашдипии' in tokens or 'хдпе' in tokens or 'hdpe' in tokens or 'pehd' in tokens:
            message = mat[1] + '\n' + "Примеры использования: " + using[1] + '\n'+ rec[1]
            tts = message

        elif 'три' in tokens or '03' in tokens or '3' in tokens or 'пвх' in tokens or 'пвс' in tokens or 'пвк' in tokens or 'pvc' in tokens:
            message = mat[2] + '\n' + "Примеры использования: " + using[2] + '\n'+ rec[2]
            tts = message

        elif 'четыре' in tokens or '04' in tokens or '4' in tokens or 'пвд' in tokens or 'пэнп' in tokens or 'лдпе' in tokens or 'ldpe' in tokens or 'peld' in tokens:
            message = mat[3] + '\n' + "Примеры использования: " + using[3] + '\n'+ rec[3]
            tts = message

        elif 'пять' in tokens or '05' in tokens or '5' in tokens or 'пп' in tokens or 'pp' in tokens or 'рр' in tokens:
            message = mat[4] + '\n' + "Примеры использования: " + using[4] + '\n'+ rec[4]
            tts = message

        elif 'шесть' in tokens or '06' in tokens or '6' in tokens or 'пс' in tokens or 'ps' in tokens:
            message = mat[5] + '\n' + "Примеры использования: " + using[5] + '\n'+ rec[5]
            tts = message

        elif 'семь' in tokens or '07' in tokens or '7' in tokens or 'о' in tokens or 'o' in tokens or 'other' in tokens or 'другое' in tokens:
            message = mat[6] + '\n' + "Примеры использования: " + using[6] + '\n'+ rec[6]
            tts = message

        elif 'абс' in tokens or 'abs' in tokens:
            message = mat[7] + '\n' + "Примеры использования: " + using[7] + '\n'+ rec[7]
            tts = message

        elif 'пк' in tokens or 'рс' in tokens or 'pc' in tokens:
            message = mat[8] + '\n' + "Примеры использования: " + using[8] + '\n'+ rec[8]
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

