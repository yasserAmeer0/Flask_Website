from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user
from .models import User, Note
from . import db
import json

supervisor = Blueprint('supervisor', __name__)

@supervisor.route('/supervisor')
@login_required
def RetrieveList():
    users = User.query.all()
    items = Note.query.all()
    return render_template("supervisor.html",items = items, users = users)


#Here the submit button will be able to update the user database, it'll check if price1 is already set then put it in price 2 and so on
@supervisor.route('/<int:id>/deleting',methods = ['GET','POST'])
@login_required
def deleting(id):
    item = Note.query.filter_by(id=id).first()
    if request.method == 'POST':
        if item:
           db.session.delete(item)

           db.session.commit()
 
        return redirect(url_for('supervisor.RetrieveList'))
 
    return redirect(url_for('supervisor.RetrieveList'))

@supervisor.route('/<int:id>/accept',methods = ['GET','POST'])
@login_required
def accept(id):
    item = Note.query.filter_by(id=id).first()
    if request.method == 'POST':
        if item:
           admin = request.form.getlist('admin')
           message = f"the Acquisition of the {admin} has been chosen to the pruchased"
           
           db.session.delete(item)
           db.session.commit()
           flash(message)
        return redirect(url_for('supervisor.RetrieveList'))
       
    return redirect(url_for('supervisor.RetrieveList'))
 





