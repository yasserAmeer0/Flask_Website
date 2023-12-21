from flask import Blueprint, render_template, request, flash, jsonify,redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

#SEARCH
@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        note = request.form.get('item')
        quantity = request.form.get('quantity')
        detail = request.form.get('detail')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(name=note, quantity = quantity, details = detail ,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Item added to cart!', category='success')
    
    return render_template("search.html", user=current_user)


#HOME 
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


#DELETE
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


