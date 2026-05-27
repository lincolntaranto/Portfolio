import bcrypt

from main import ACESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from models import Usuario

from jose import jwt, JWTError

from datetime import datetime, timedelta, timezone

def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_senha(senha: str, hash: str) -> bool:
    return bcrypt.checkpw(senha.encode("utf-8"), hash.encode("utf-8"))

ALGORITHM = "HS256"

def criar_token(id_usuario):
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=int(ACESS_TOKEN_EXPIRE_MINUTES))
    dic_info = {
        "sub" : id_usuario,
        "exp" : data_expiracao
    }
    jwt_encoded = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_encoded

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif not verificar_senha(senha, usuario.senha):
        return False
    return usuario
