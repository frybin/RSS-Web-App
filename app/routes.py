from flask import render_template,flash,redirect,url_for
from app import app, db
from app.forms import LoginForm
from app.models import Feed

@app.route('/')

@app.route('/index')
def index():
    feeds = Feed.query.all()
    return render_template('index.html', feeds=feeds)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/delete_feed/<string:id>', methods=['POST'])
def delete_feed(id):
    db.session.delete(id)
    db.session.commit()
    flash('Article Deleted', 'success')
    return redirect(url_for('index'))