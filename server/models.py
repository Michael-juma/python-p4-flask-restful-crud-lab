from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize SQLAlchemy
db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    # Enable serialization of all fields by default
    serialize_rules = ('-created_at', '-updated_at')  # optional

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'

