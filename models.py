from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"



class Pet(db.Model):
    """pet"""

    __tablename__="pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text,
                     nullable=True)
    age = db.Column(db.Integer,
                     nullable=True)
    notes = db.Column(db.Text,
                     nullable=True)
    available = db.Column(db.Text,
                     nullable=True, default="Yes")
    
    def image_url(self):
        """Return image for pet"""

        return self.photo_url or GENERIC_IMAGE













def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)