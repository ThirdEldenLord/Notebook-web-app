from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import data_base
import json

views = Blueprint('views', __name__)

#Go to homepage function
@views.route('/', methods=['GET', 'POST'])
def home():      
    return render_template("home.html", user=current_user)

#Function for add new note
@views.route('/notes', methods=['GET', 'POST'])
@login_required
def add_notes():
    if request.method == 'POST':
        note = request.form.get('note')
        #notes should be atleast 3 letter
        if len(note) < 3:
            flash('Your note should be longer', category='error')
        else:
            new_note = Note(note=note, user_id=current_user.id)
            data_base.session.add(new_note)
            data_base.session.commit() 
            flash('Note successfuly added', category='success')  
            
    return render_template("notes.html", user=current_user)

#Go to notes page function
@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    return render_template("notes.html", user=current_user)

#Function for delete our notes
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            data_base.session.delete(note)
            data_base.session.commit()
            flash('Note successfuly deleted', category='success')

    return jsonify({})