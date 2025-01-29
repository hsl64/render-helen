from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="static/", index_file="index.htm", autorefresh=True)

#  note - you can change the prefix above and get rid of this route if you just want to host static
#  @app.route('/', methods=['GET'])
#  def hello():
#    return make_response("testing~")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)