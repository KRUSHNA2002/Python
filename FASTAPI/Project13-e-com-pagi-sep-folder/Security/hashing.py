from passlib.context import CryptContext



pwt_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwt_context.hash(
        password
    )

def verify_password(
        plain,
        hashed
):
    
    return pwt_context.verify(
        plain,
        hashed
    )