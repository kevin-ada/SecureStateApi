from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    return pwd_context.hash(password)


def verify_hashed_password(plain, hashed):
    return pwd_context.verify(plain, hashed)
