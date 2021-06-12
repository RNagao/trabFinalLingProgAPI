from .models import Questoes
from ..extensions import ma

class QuestoesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Questoes
        load_instance=True
        ordered=True

    id = ma.Integer(dump_only=True)
    numero = ma.Integer(required=True)
    pergunta = ma.String(required=True)
    opcaoA = ma.String(required=True)
    opcaoB = ma.String(required=True)
    opcaoC = ma.String(required=True)
    opcaoD = ma.String(required=True)
    resposta = ma.String(required=True)
    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)