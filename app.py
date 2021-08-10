from datetime import datetime
from flask import Flask

now = datetime.utcnow()

year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

hour = now.strftime("%H")

minutes = now.strftime("%M")

seconds = now.strftime("%S")

am_pm = now.strftime("%p")

date_formatted = f'{day}/{month}/{year} {hour}:{minutes}:{seconds} {am_pm}'

# date_time = now.strftime("%m/%d/%Y %H:%M:%S %p")
# Eu poderia ter usado esse método acima, porém fiz um a um
# pra facilitar na lógica da mensagem de bom dia, boa tarde ou boa noite
# e evitar de ter que manipular a string resultante

message = ''
if int(hour) > 00 and int(hour) < 12:
    message = "Bom dia!"
elif int(hour) >= 12 and int(hour) < 18:
    message = "Boa tarde!"
else:
    message = "Boa noite!"

home_return = {
    "data": "Hello Flask!"
}

current_datetime_return = {
    "current_datetime": date_formatted,
    "message": message
}

app = Flask(__name__)


@app.route('/')
def home():
    return home_return


@app.route('/current_datetime')
def current_datetime():
    return current_datetime_return
