from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note
from . import db
import json

cart = Blueprint('cart', __name__)


@cart.route('/cart')
@login_required
def RetrieveList():
    items = Note.query.all()
    return render_template("cart.html",items = items, current_user = current_user)
    
@cart.route('/<int:id>/update',methods = ['GET','POST'])
def update(id):
    item = Note.query.filter_by(id=id).first()
    if request.method == 'POST':
        if item:
            db.session.delete(item)
            db.session.commit()
 
            name = request.form['name']
            quantity = request.form['quantity']
            details = request.form['details']
            price1=request.form['price1']
            item = Note(id=id, name=name, quantity=quantity, details = details,price1=price1)
 
            db.session.add(item)
            db.session.commit()
            #return redirect(f'/adminpage')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', item = item)
