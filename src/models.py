from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,

            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(120), unique=True, nullable=False)
    orbital_period = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    residents = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.surface_population,
            "residents": self.residents,
            # do not serialize the password, its a security breach
        }
    
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    manufacturer = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80), unique=False, nullable=False)
    hyperdrive_rating = db.Column(db.Integer)
    mglt = db.Column(db.Integer)
    starship_class = db.Column(db.String(80), unique=False, nullable=False)
    pilots = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer)
    created = db.Column(db.String(120), unique=True, nullable=False)
    crew = db.Column(db.Integer)
    edited= db.Column(db.String(120), unique=True, nullable=False)
    length = db.Column(db.Integer)
    manufacturer = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    model = db.Column(db.String(80), unique=False, nullable=False)
    passenger = db.Column(db.String(80), unique=False, nullable=False)
    pilots = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created,
            "crew": self.crew,
            "edited": self.edited,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "passenger": self.passenger,
            "pilots": self.pilots,
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    people_id= db.Column(db.Integer, db.ForeignKey("people.id"))
    planets_id= db.Column(db.Integer, db.ForeignKey("planets.id"))
    starships_id= db.Column(db.Integer, db.ForeignKey("starships.id"))
    vehicles_id= db.Column(db.Integer, db.ForeignKey("vehicles.id"))


    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planets_id": self.planets_id,
            "starships_id": self.starships_id,
            "vehicles_id": self.vehicles_id,
        }
    