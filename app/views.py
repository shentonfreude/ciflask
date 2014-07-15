from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello world'

def goodby():
    return 'Goodby world'
