from search_title import blueprint as api
from flask import Flask, request, g
from flask_cors import CORS
from search_title.assignment import parseXML
import threading


app = Flask(__name__)
CORS(app)
app.register_blueprint(api, url_prefix='/search_articles')



if __name__ == '__main__':
    t1 = threading.Thread(target=parseXML)
    t1.start()
    t1.join()
    app.run(host="0.0.0.0", debug=False, port=5010)
