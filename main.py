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
    global boosty
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

    ### Start question   
    elif state == 10:

        if 'код' in tokens or 'кот' in tokens:
            message = ("Код переработки — это треугольник из стрелок с цифрой внутри. Цифры обозначают материал, из которого сделан предмет")
            tts = "Код переработки — это треугольник из стр`елок с цифрой внутри. Цифры обозначают материал, из которого сделан предмет"

        elif 'второе' in tokens or 'идентификатор' in tokens:
            message = ('Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником из стрелок с цифрой внутри')
            tts = 'Идентификатор переработки — это буквы на русском или латинице, расположенные под треугольником из стр`елок с цифрой внутри'

        elif 'спасибо' in tokens or 'стоп' in tokens or 'выход' in tokens or 'не' in tokens or 'заверши' in tokens or 'пока' in tokens or 'хватит' in tokens:
            state = 100

        elif 'понятно' in tokens or 'понял' in tokens or 'поняла' in tokens or 'ясно' in tokens or 'хорошо' in tokens or 'окей' in tokens:
            message = 'Рада помочь!'
            tts = message

### Main part

# Plastic
        elif 'один' in tokens or '01' in tokens or '1' in tokens or 'пэт' in tokens or 'pet' in tokens or 'pete' in tokens:
            message = mat[0] + '\n'+ "Примеры использования: " + using[0] + '\n' + rec[0] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message 

        elif 'два' in tokens or '02' in tokens or '2' in tokens or 'пэ' in tokens or 'пнд' in tokens or 'пэвп' in tokens or 'ашдипии' in tokens or 'хдпе' in tokens or 'hdpe' in tokens or 'pehd' in tokens:
            message = mat[1] + '\n' + "Примеры использования: " + using[1] + '\n'+ rec[1] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = "Полиэтилен низкого давления. Примеры использования: упаковки от шампуня, геля для д`уша, моющих средств. Такие упаковки обычно имеют большой шов на дне. Успешно перерабатывается!"

        elif 'три' in tokens or '03' in tokens or '3' in tokens or 'пвх' in tokens or 'пвс' in tokens or 'пвк' in tokens or 'pvc' in tokens:
            message = mat[2] + '\n' + "Примеры использования: " + using[2] + '\n'+ rec[2]
            tts = message

        elif 'четыре' in tokens or '04' in tokens or '4' in tokens or 'пвд' in tokens or 'пэнп' in tokens or 'лдпе' in tokens or 'ldpe' in tokens or 'peld' in tokens:
            message = mat[3] + '\n' + "Примеры использования: " + using[3] + '\n'+ rec[3] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'пять' in tokens or '05' in tokens or '5' in tokens or 'пп' in tokens or 'pp' in tokens or 'рр' in tokens:
            message = mat[4] + '\n' + "Примеры использования: " + using[4] + '\n'+ rec[4] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'шесть' in tokens or '06' in tokens or '6' in tokens or 'пс' in tokens or 'ps' in tokens:
            message = mat[5] + '\n' + "Примеры использования: " + using[5] + '\n'+ rec[5] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'семь' in tokens or '07' in tokens or '7' in tokens or 'о' in tokens or 'o' in tokens or 'other' in tokens or 'другое' in tokens:
            message = mat[6] + '\n' + "Примеры использования: " + using[6] + '\n'+ rec[6]
            tts = message

        elif 'абс' in tokens or 'abs' in tokens:
            message = mat[7] + '\n' + "Примеры использования: " + using[7] + '\n'+ rec[7] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'пк' in tokens or 'рс' in tokens or 'pc' in tokens:
            message = mat[8] + '\n' + "Примеры использования: " + using[8] + '\n'+ rec[8] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'pa' in tokens or 'па' in tokens or 'ра' in tokens:
            message = mat[9] + '\n' + "Примеры использования: " + using[9] + '\n'+ rec[9] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

# Paper

        elif 'двадцать' in tokens or '20' in tokens:
            message = mat[10] + '\n' + "Примеры использования: " + using[10] + '\n'+ rec[10] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('двадцать' in tokens and 'один' in tokens) or '21' in tokens:
            message = mat[11] + '\n' + "Примеры использования: " + using[11] + '\n'+ rec[11] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('двадцать' in tokens and 'два' in tokens) or '22' in tokens:
            message = mat[12] + '\n' + "Примеры использования: " + using[12] + '\n'+ rec[12] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('двадцать' in tokens and 'три' in tokens) or '23' in tokens:
            message = mat[13] + '\n' + "Примеры использования: " + using[13] + '\n'+ rec[13] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
                
        elif 'пэп' in tokens or 'пап' in tokens or 'рар' in tokens or 'pap' in tokens:
            message = "Целлюлозная продукция (гофрированный картон, картон, бумага)." + '\n\n' + "Примеры использования: коробки, открытки, журналы, газеты, офисная бумага." + '\n\n' + rec[9] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

# Metals

        elif 'сорок' in tokens or 'фу' in tokens or '40' in tokens or 'fu' in tokens:
            message = mat[14] + '\n' + "Примеры использования: " + using[14] + '\n'+ rec[14] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('сорок' in tokens and 'один' in tokens) or '41' in tokens or 'ал' in tokens or 'al' in tokens or 'алу' in tokens or 'alu' in tokens:
            message = mat[15] + '\n' + "Примеры использования: " + using[15] + '\n'+ rec[15] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
# Organic materials of natural origin

        elif 'пятьдесят' in tokens or '50' in tokens or 'for' in tokens or 'фор' in tokens:
            message = mat[16] + '\n' + "Примеры использования: " + using[16] + '\n'+ rec[16]
            tts = message

        elif ('пятьдесят' in tokens and 'один' in tokens) or '51' in tokens:
            message = mat[17] + '\n' + "Примеры использования: " + using[17] + '\n'+ rec[17]
            tts = message

        elif 'шестьдесят' in tokens or '60' in tokens or 'tex' in tokens or 'текс' in tokens:
            message = mat[18] + '\n' + "Примеры использования: " + using[18] + '\n'+ rec[18] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = "Хл`опок. Примеры использования: тканевые принадлежности, нити, вата. Одежду можно сдать на переработку или продать" + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"

        elif ('шестьдесят' in tokens and 'один' in tokens) or '61' in tokens:
            message = mat[19] + '\n' + "Примеры использования: " + using[19] + '\n'+ rec[19]
            tts = message     

# Glass

        elif 'семьдесят' in tokens or '70' in tokens:
            message = mat[20] + '\n' + using[20] + '\n'+ rec[20] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
        elif ('семьдесят' in tokens and 'один' in tokens) or '71' in tokens:
            message = mat[21] + '\n' + using[21] + '\n'+ rec[21] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('семьдесят' in tokens and 'два' in tokens) or '72' in tokens:
            message = mat[22] + '\n' + using[22] + '\n'+ rec[22] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
        elif ('семьдесят' in tokens and 'три' in tokens) or '73' in tokens:
            message = mat[23] + '\n' + using[23] + '\n'+ rec[23] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('семьдесят' in tokens and 'четыре' in tokens) or '74' in tokens:
            message = mat[24] + '\n' + using[24] + '\n'+ rec[24] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
        elif ('семьдесят' in tokens and 'пять' in tokens) or '75' in tokens:
            message = mat[25] + '\n' + using[25] + '\n'+ rec[25]
            tts = message

        elif ('семьдесят' in tokens and 'шесть' in tokens) or '76' in tokens:
            message = mat[26] + '\n' + "Примеры использования: " + using[26] + '\n'+ rec[26]
            tts = message

        elif ('семьдесят' in tokens and 'семь' in tokens) or '77' in tokens:
            message = mat[27] + '\n' + using[27] + '\n'+ rec[27]
            tts = message
        
        elif ('семьдесят' in tokens and 'восемь' in tokens) or '78' in tokens:
            message = mat[28] + '\n' + using[28] + '\n'+ rec[28]
            tts = message

        elif ('семьдесят' in tokens and 'девять' in tokens) or '79' in tokens:
            message = mat[29] + '\n' + using[29] + '\n'+ rec[29]
            tts = message
        
# Composite materials

        elif 'восемьдесят' in tokens or '80' in tokens:
            message = mat[30] + '\n' + "Примеры использования: " + using[30] + '\n'+ rec[30]
            tts = message

        elif ('восемьдесят' in tokens and 'один' in tokens) or '81' in tokens:
            message = mat[31] + '\n' + "Примеры использования: " + using[31] + '\n'+ rec[31] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif ('восемьдесят' in tokens and 'два' in tokens) or '82' in tokens:
            message = mat[32] + '\n' + "Примеры использования: " + using[32] + '\n'+ rec[32] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
        elif ('восемьдесят' in tokens and 'три' in tokens) or '83' in tokens:
            message = mat[33] + '\n' + "Примеры использования: " + using[33] + '\n'+ rec[33] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message
        
        elif ('восемьдесят' in tokens and 'четыре' in tokens) or '84' in tokens:
            message = mat[34] + '\n' + using[34] + '\n'+ rec[34] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'c/pap' in tokens or 'с/рар' in tokens or 'эс пэп' in tokens or 'эс пап' in tokens:
            message = mat[30] + '\n' + using[34] + '\n'+ rec[34] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'девяносто' in tokens or '90' in tokens or 'c/pe' in tokens or 'с/ре' in tokens or 'c/*' in tokens or 'с/*' in tokens:
            message = mat[35] + '\n' + "Примеры использования: " + using[35] + '\n'+ rec[35]
            tts = message
       
        elif ('девяносто' in tokens and 'один' in tokens) or '91' in tokens:
            message = mat[36] + '\n' + "Примеры использования: " + using[36] + '\n'+ rec[36]
            tts = message

        elif ('девяносто' in tokens and 'два' in tokens) or '92' in tokens:
            message = mat[37] + '\n' + "Примеры использования: " + using[37] + '\n'+ rec[37]
            tts = message

        elif ('девяносто' in tokens and 'пять' in tokens) or '95' in tokens:
            message = mat[38] + '\n' + "Примеры использования: " + using[38] + '\n'+ rec[38]
            tts = message

        elif ('девяносто' in tokens and 'шесть' in tokens) or '96' in tokens or 'c/alu' in tokens or 'эс алу' in tokens:
            message = mat[39] + '\n' + using[39] + '\n'+ rec[39]
            tts = message

        elif ('девяносто' in tokens and 'семь' in tokens) or '97' in tokens:
            message = mat[40] + '\n' + "Примеры использования: " + using[40] + '\n'+ rec[40]
            tts = message

        elif ('девяносто' in tokens and 'восемь' in tokens) or '98' in tokens or 'c/gl' in tokens:
            message = mat[41] + '\n' + using[41] + '\n'+ rec[41]
            tts = message       

# Batteries

        elif 'восемь' in tokens or '08' in tokens or '8' in tokens or 'lead' in tokens or 'pb' in tokens:
            message = mat[42] + '\n' + using[42] + '\n' + rec[42] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'девять' in tokens or '09' in tokens or '9' in tokens or '19' in tokens or 'alkaline' in tokens or 'алкалайн' in tokens:
            message = mat[43] + '\n' + using[43] + '\n' + rec[43] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'десять' in tokens or '10' in tokens or 'nicd' in tokens or 'ni-cd' in tokens:
            message = mat[44] + '\n'+ using[44] + '\n' + rec[44] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = 'Н`икель-к`адмиевый аккумулятор. Используется в электронных устройствах. Ни в коем случае не выбрасывайте! Обязательно сдайте в пункт приёма на утилизацию' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
        
        elif 'одиннадцать' in tokens or 'nimh' in tokens or '11' in tokens or 'ni-mh' in tokens:
            message = mat[45] + '\n' + using[45] + '\n' + rec[45] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = 'Н`икель-металл-гидридный аккумулятор. Используется в электронных устройствах. Ни в коем случае не выбрасывайте! Обязательно сдайте в пункт приёма на утилизацию' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
        
        elif 'двенадцать' in tokens or '12' in tokens or 'li' in tokens or 'liion' in tokens or 'li-ion' in tokens or 'lion' in tokens:
            message = mat[46] + '\n' + using[46] + '\n' + rec[46] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'тринадцать' in tokens or '13' in tokens or 'so' in tokens or 'z' in tokens:
            message = mat[47] + '\n' + using[47] + '\n' + rec[47] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = message

        elif 'четырнадцать' in tokens or '14' in tokens or 'cz' in tokens:
            message = mat[48] + '\n\n' + using[48] + '\n\n' + rec[48] + '\n' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"
            tts = 'М`арганцево-ц`инковый элемент. Используется в батарейках и аккумуляторах. Ни в коем случае не выбрасывайте! Обязательно сдайте в пункт приёма на утилизацию' + "Ближайший пункт приёма вы можете найти на карте: https://recyclemap.ru"


        elif 'luv' in tokens or '120701' in tokens or '12072001' in tokens  or '12.07.2001' in tokens  or 'love' in tokens :
            message = 'luv u too, durling ♡'

### Another answer
        else:
            message = choice(["Не могу найти такой код, наверное, вы придумали новый!", "Кажется, такого материала я ещё не знаю"])
            tts = message

### Finish

    if state == 100:
        boosty = "Если вам понравился навык, то вы можете поддержать автора: https://boosty.to/leomilevsky/single-payment/donation/75054?share=target_link"
        message = choice(['До новых встреч!', "Спасибо, что интересуетесь экологией!", "Проведите день с пользой!"]) + "\n\n"
        tts = message
        message += boosty
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

