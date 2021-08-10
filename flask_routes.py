from datetime import datetime
from flask import Flask

now = datetime.now()

date_formatted = now.strftime("%d/%m/%Y %H:%M:%S %p")
print(date_formatted)
hour = int(now.strftime("%H"))
message = ''
if hour > 0 and hour < 12:
    message = "Bom dia!"
elif hour >= 12 and hour < 18:
    message = "Boa tarde!"
else:
    message = "Boa noite!"

home_return = {
    "data": "Hello Flask"
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
