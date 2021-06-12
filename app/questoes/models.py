from ..extensions import db
from ..models import BaseModel

class Questoes(BaseModel):
    __tablename__ = 'questoes'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True)
    pergunta = db.Column(db.String(500), default="")
    opcaoA = db.Column(db.String(500), default="")
    opcaoB = db.Column(db.String(500), default="")
    opcaoC = db.Column(db.String(500), default="")
    opcaoD = db.Column(db.String(500), default="")
    resposta = db.Column(db.String(1), default="")
