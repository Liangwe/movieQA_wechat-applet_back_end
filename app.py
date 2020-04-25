from functools import wraps
from flask import Flask, request, make_response, jsonify
from query.query_main import Query

app = Flask(__name__)
query = Query()

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

@app.route('/')
def hello_world():
    return 'Hello World! every one'


# @app.route("/getImage", methods=['GET'])
# @allow_cross_domain
# def get_image(url):
#
#     return jsonify(url)

@app.route("/getToast",methods=['GET'])
@allow_cross_domain
def get_toast():
    question = request.values['info']
    ans = query.parse(question.encode('utf-8'))
    return jsonify(ans)



if __name__ == '__main__':
    app.run()
