# Imports
from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, email: str, username: str, password= str):
    # Check for existing user inside db
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("Email already registered")

    # Otherwise lets create the user
    user = User(
            email=email,
            username=username,
            password=hash_password(password)
    )

    # Commit to db
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, email: str, password: str):
    # Check if user exists
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None

    # Password Check
    if not verify_password(password, user.password):
        return None

    # Authenticated user return token
    token = create_access_token({"sub": str(user.id)})
    return token
