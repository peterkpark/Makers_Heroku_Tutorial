import json
import os
from flask import Flask, request
import requests

application = Flask(__name__)

# # Take note of the two endpoints below. They may look the same but one processes GET requests and one processes POST requests

# If a GET request is made
@application.route("/person", methods=["GET"])
def person():
    print("Getting a random person")

    person_json = requests.get("https://randomuser.me/api").json()

    return person_json


# If a POST request is made
@application.route("/person", methods=["POST"])
def person_of_nationality():
    nationality = request.form.get("nationality")

    print(f"Search for person with nationality {nationality}")

    person_json = requests.get(
        "https://randomuser.me/api", params={"nat": nationality}
    ).json()

    return person_json


# If a GET request is made
@application.route("/people", methods=["GET"])
def people():
    number_of_people = request.args.get("number_of_people")

    print(f"Search for {number_of_people} people")

    person_json = requests.get(
        "https://randomuser.me/api", params={"results": number_of_people}
    ).json()

    return person_json

# If a GET request is made
@application.route("/getComments", methods=["GET"])
def get_comments():
    f = open("comments.json", "r")
    comments = json.load(f)
    f.close()

    return comments


# If a POST request is made
@application.route("/addComments", methods=["POST"])
def add_comment():
    name = request.form.get("name")
    flavor = request.form.get("flavor")
    comment = request.form.get("comment")

    comment_to_append = {
        "name": name,
        "flavor": flavor,
        "comment": comment
    }

    f = open("comments.json", "r")
    comments = json.load(f)
    f.close()

    print(comments)

    comments['comments'].append(comment_to_append)

    f = open("comments.json", "w")
    f.write(json.dumps(comments))
    f.close()


    return comment_to_append

if __name__ == "__main__":
    application.run()
