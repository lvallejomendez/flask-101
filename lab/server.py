"""
Creation of a Flask service
"""
from flask import Flask, make_response, request

app = Flask(__name__)

###################################################
# Hard coded list for this simple use case. This data was generated with Mockaroo.
###################################################
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

###################################################

# This code creates a Flask server and adds a home endpoint “/“ that returns the string hello world.
@app.route("/")
def index():
    return "Hello World!"

# flask --app server --debug run
# in another terminal run: curl -X GET -i -w '\n' localhost:5000

# Send custom HTTP code back with a tuple.
@app.route("/no_content")
def no_content():
    """
    Return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """
    return ({"message":"No content found"}, 204)

# Send custom HTTP code back with the make_response() method.
@app.route("/exp")
def index_explicit():
    """
    Return 'Hello World!' message with a status code of 200
    Returns:
        string: Hello World!
        status code: 200
    """
    resp = make_response({"message":"Hello World!"})
    resp.status_code = 200
    return resp

# Create an end point that returns the person’s data to the client in JSON format.
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def name_search():
    """
    Find a person in the database
    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    query = request.args.get("q")

    if not query:
        return {"message":"Invalid input parameter"}, 422

    # this code goes through data and looks for the first_name
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    return {"message":"Person not found"}, 404

@app.route("/count")
def count():
    try:
        return {"data count": f"{len(data)} items found"}, 200
    except NameError:
        return {"message": "Data not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    """
    Reads an Account
    This endpoint will ask for a person based on the id that is requested
    """
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message":"Person not found"}, 404
