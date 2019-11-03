from sqlalchemy.sql import func
from storrmbox.database import (
    db,
    SurrogatePK,
    Model,
    relationship,
    check_password_hash,
    generate_password_hash
)
from .torrent import Torrent
from .token import Token


class User(SurrogatePK, Model):
    __tablename__ = "users"

    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=func.now())
    # last_update = db.Column(db.DateTime, index=False, unique=False, nullable=True, onupdate=func.now())
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    # torrents = relationship(Torrent, backref=db.backref("torrents"))
    owned_tokens = relationship("Token", backref="user", lazy='dynamic')

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User {}>'.format(self.username)
