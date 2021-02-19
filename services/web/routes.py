from manage import create_app, init_db
from database import Song
import flask

app = create_app()
init_db()

#------------ GET REQUEST ------------#

# Route to get all songs
@app.route("/songs", methods=["GET"])
def get_songs():
	"""This funtion returns all the songs in the database"""
	return flask.jsonify({"Songs": Song.get_all_songs()})


# Route to get a song by id
@app.route("/songs/<int:id>", methods=["GET"])
def get_song_by_id(id):
	"""This function returns a song using its id"""
	return flask.jsonify({"Song": Song.get_song_by_id(id)})

#------------ POST REQUEST ------------#

# Route to add a new song
@app.route("/songs", methods=["POST"])
def add_song():
	"""This function adds a song to the database"""
	request_data = flask.request.get_json() # get data from client
	Song.add_song(request_data["Title"], request_data["Artist"], request_data["Duration"])
	return flask.Response("Song added", 201, mimetype="application/json")

#------------ PUT REQUEST ------------#

# Route to update a song
@app.route("/songs/<int:id>", methods=["PUT"])
def update_song_by_id(id):
	"""This function updates a song using its id"""
	request_data = flask.request.get_json()
	Song.update_song_by_id(id, request_data["Title"], request_data["Artist"], request_data["Duration"])
	return flask.Response("Song updated", 200, mimetype="application/json")

#------------ DELETE REQUEST ------------#

# Route to delete a song
@app.route("/songs/<int:id>", methods=["DELETE"])
def delete_song_by_id(id):
	"""This function deletes a song using its id"""
	Song.delete_song_by_id(id)
	return flask.Response("Song deleted", 200, mimetype="application/json")