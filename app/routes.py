from flask import render_template,flash,redirect,url_for
from app import app, db
from app.forms import AddFeedForm, EditFeedForm
from app.models import Feed

@app.route('/')

@app.route('/index')
def index():
    feeds = Feed.query.all()
    return render_template('index.html', feeds=feeds)

@app.route('/delete_feed/<string:id>', methods=['POST'])
def delete_feed(id):
    feed = Feed.query.filter_by(rss_i=id).first()
    db.session.delete(feed)
    db.session.commit()
    flash('Feed Deleted for {}'.format(feed.name), 'success')
    return redirect(url_for('index'))


@app.route('/add_feed', methods=['GET', 'POST'])
def add_feed():
    form = AddFeedForm()
    if form.validate_on_submit():
        feed=Feed(name=form.name.data,link=form.link.data,
                  article_1=form.article_1.data,article_2=form.article_2.data)
        db.session.add(feed)
        db.session.commit()
        flash('Feed Created for {}'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('add_feed.html', title='Add Feed', form=form)

@app.route('/edit_feed/<string:id>', methods=['GET', 'POST'])
def edit_feed(id):
    form = EditFeedForm()
    feed = Feed.query.filter_by(rss_i=id).first()
    if form.validate_on_submit():
        feed.name=form.name.data
        feed.link=form.link.data
        feed.article_1=form.article_1.data
        feed.article_2=form.article_2.data
        print(feed.name)
        db.session.commit()
        flash('Feed Edited for {}'.format(form.name.data))
        return redirect(url_for('index'))
    form.name.data = feed.name
    form.link.data = feed.link
    form.article_1.data = feed.article_1
    form.article_2.data = feed.article_2

    return render_template('edit_feed.html', title='Edit Feed', form=form)