from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people_sw'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Character %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name" :  self.name,
            "height" : self.height,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "homeworld" : self.homeworld,
            "url" : self.url
        }


class Planets(db.Model):
    __tablename__ = 'planets_sw'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(50), nullable=False)
    orbital_period = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.String(50), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    gravity = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    surface_water =  db.Column(db.String(50), nullable=False)
    population =  db.Column(db.String(50), nullable=True)
    url = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Planet %r>' % self.name
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "diameter" : self.diameter,
            "climate" : self.climate,
            "gravity" : self.gravity,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "population" : self.population,
            "url" : self.url
        }

class Favorites(db.Model):
    __tablename__ = 'favorites_sw'
   
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)
    favorite_id = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    users = db.relationship(User)
    def __repr__(self):
        return '<Favorite %r>' % self.favorite_id  

    def serialize(self):
        return {
            "tipo" : self.tipo,
            "favorite_id" : self.favorite_id
        }