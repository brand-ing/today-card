import datetime

def set_date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return today