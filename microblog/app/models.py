from typing import Optional
import sqlalchemy as sa 
import sqlalchemy.orm as so
from app import db



class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, index=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f'<User {self.user_name}>'
