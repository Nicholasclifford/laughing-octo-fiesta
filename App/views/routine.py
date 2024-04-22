from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from.index import index_views

from App.controllers import (
    login
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


@app.route('/create_routine', methods=['POST'])
@jwt_required()
def create_routine():
    # Get the routine name from the form data
    routine_name = request.form.get('routine_name')

    # Create a new routine with the provided name and user id
    new_routine = Routine(name=routine_name, current_user.id)
    
    # Add the new routine to the database session
    db.session.add(new_routine)
    
    # Commit the changes to the database
    db.session.commit()

    # Redirect to a route or URL where you want to go after creating the routine
    return redirect(url_for('/'))  # Redirect to the index route