from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user
from .models import User, Note
from . import db
import json

admin = Blueprint('admin', __name__)

@admin.route('/adminpage')
@login_required
def RetrieveList():
    users = User.query.all()
    items = Note.query.all()
    return render_template("adminpage.html",items = items, users = users)


#Here the submit button will be able to update the user database, it'll check if price1 is already set then put it in price 2 and so on
@admin.route('/<int:id>/submittingprice',methods = ['GET','POST'])
def update(id):
    item = Note.query.filter_by(id=id).first()
    if request.method == 'POST':
        if item:

            price=request.form.get('price')

            if(not item.price1):
                item.price1 = price
                if int(price)<=5000:
                   message = f"the Acquisition of the admin 1 has been chosen to the purchased because it less than 5000$" 
                   db.session.delete(item)
                   db.session.commit()
                   flash(message)

            elif(not item.price2):
                item.price2 = price
            elif(not item.price3):
                item.price3 = price

            db.session.commit()
 
        return redirect(url_for('admin.RetrieveList'))
 
    return redirect(url_for('admin.RetrieveList'))