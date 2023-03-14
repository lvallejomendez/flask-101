from flask import Flask
app = Flask(__name__)

# This code creates a Flask server and adds a home endpoint “/“ that returns the string hello world.
@app.route("/")
def index():
    return "hello world"

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
