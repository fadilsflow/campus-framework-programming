from flask import render_template, redirect, url_for, flash, request
from models.user_model import User
from lib import db

def init_routes(app):
    @app.route('/')
    def list_users():
        users = User.query.all()
        return render_template('list_users.html', users=users)

    @app.route('/users/create', methods=['GET'])
    def create_user_page():
        return render_template('create_user.html')

    @app.route('/users/create', methods=['POST'])
    def create_user_web():
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            
            if not name or not email:
                flash('Name and email are required', 'danger')
                return redirect(url_for('create_user_page'))
                
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email already exists', 'danger')
                return redirect(url_for('create_user_page'))
                
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            
            flash('User created successfully!', 'success')
            return redirect(url_for('list_users'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating user: {str(e)}', 'danger')
            return redirect(url_for('create_user_page'))

    @app.route('/users/<int:user_id>', methods=['GET'])
    def view_user(user_id):
        user = User.query.get_or_404(user_id)
        return render_template('view_user.html', user=user)

    @app.route('/users/<int:user_id>/edit', methods=['GET'])
    def edit_user_page(user_id):
        user = User.query.get_or_404(user_id)
        return render_template('edit_user.html', user=user)

    @app.route('/users/<int:user_id>/edit', methods=['POST'])
    def update_user_web(user_id):
        try:
            user = User.query.get_or_404(user_id)
            name = request.form.get('name')
            email = request.form.get('email')
            
            if not name or not email:
                flash('Name and email are required', 'danger')
                return redirect(url_for('edit_user_page', user_id=user_id))
                
            # Check if email is being changed and if it's already taken
            if email != user.email and User.query.filter_by(email=email).first():
                flash('Email already exists', 'danger')
                return redirect(url_for('edit_user_page', user_id=user_id))
                
            user.name = name
            user.email = email
            db.session.commit()
            
            flash('User updated successfully!', 'success')
            return redirect(url_for('list_users'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating user: {str(e)}', 'danger')
            return redirect(url_for('edit_user_page', user_id=user_id))

    @app.route('/users/<int:user_id>/delete', methods=['POST'])
    def delete_user_web(user_id):
        try:
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting user: {str(e)}', 'danger')
        
        return redirect(url_for('list_users'))
