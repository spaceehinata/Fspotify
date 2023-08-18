from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user
from f.website.models import User, Song
from f.website import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        song = request.form.get('song')

        if song is not None:
            current_user.favorite_songs.append(song)
            db.session.commit()
            flash('Song added!', category='success')
        else:
            flash('Invalid song!', category='error')

    return render_template("home.html", user=current_user)


@views.route('/delete-song', methods=['POST'])
def delete_song():
    song = json.loads(request.data)
    songId = song['songId']
    song = Song.query.get(songId)
    if song:
        current_user.favorite_songs.remove(song)
        db.session.commit()

    return jsonify({})
