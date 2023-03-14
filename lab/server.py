from flask import Flask, make_response
app = Flask(__name__)

# This code creates a Flask server and adds a home endpoint “/“ that returns the string hello world.
@app.route("/")
def index():
    return "Hello World!"

# flask --app server --debug run
# in another terminal run: curl -X GET -i -w '\n' localhost:5000

# Send custom HTTP code back with a tuple.
@app.route("/no_content")
def no_content():
    """return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """
    return ({"message":"No content found"}, 204)

# Send custom HTTP code back with the make_response() method.
@app.route("/exp")
def index_explicit():
    """return 'Hello World!' message with a status code of 200
    Returns:
        string: Hello World!
        status code: 200
    """
    resp = make_response({"message":"Hello World!"})
    resp.status_code = 200
    return resp