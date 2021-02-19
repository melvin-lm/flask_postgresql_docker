import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Song(db.Model):
	__tablename__ = "songs"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	artist = db.Column(db.String, nullable=False)
	duration = db.Column(db.String, nullable=False) # e.g., "4:22" "4'22''" "4m 22s"...  

	def json(self):
		"""This function returns the output as JSON"""
		return {"id": self.id, "Title": self.title, "Artist": self.artist, "Duration": self.duration}

	def get_song_by_id(id):
		"""This function returns a song using its id"""
		return [Song.json(Song.query.filter_by(id=_id).first())]

	def get_all_songs():
		"""This function returns all the songs in the database"""
		return [Song.json(song) for song in Song.query.all()]

	def add_song(title, artist, duration):
		"""This function adds a song to the database"""
		new_song = Song(title=title, artist=artist, duration=duration)
		db.session.add(new_song)
		db.session.commit()

	def update_song_by_id(id, title, artist, duration):
		"""This function updates a song using its id"""
		song_to_update = Song.query.filter_by(id=id).first()
		song_to_update.title = title
		song_to_update.artist = artist
		song_to_update.duration = duration
		db.session.commit() 

	def delete_song_by_id(id):
		"""This function deletes a song using its id"""
		Song.query.filter_by(id=id).delete()
		db.session.commit()
