from app import db

class Feed(db.Model):
    rss_i=db.Column(db.INT,primary_key=True,index=True,autoincrement=True)
    name=db.Column(db.Text,default='')
    link=db.Column(db.Text,default='')
    article_1=db.Column(db.Text,default='')
    article_2=db.Column(db.Text,default='')

    def __repr__(self):
        return '<Feed {}>'.format(self.name)