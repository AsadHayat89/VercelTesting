
import flask
app = flask.Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_request():
    result=""
    return result
@app.route('/',methods=["GET"])
def index():
    print("asdfd")
    return "render_template('index.html')"

ports=0
if __name__ == "__main__": 
    app.run(debug=False)
