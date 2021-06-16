from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    asignatura =  db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Preguntas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
            # do not serialize the password, its a security breach
        }

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    unidad = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "unidad": self.description
            # do not serialize the password, its a security breach
        }

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    unidad = db.Column(db.String(80), unique=False, nullable=False)
    document = db.Column(db.String(500), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "unidad": self.unidad,
            "document": self.description
            # do not serialize the password, its a security breach
        }
