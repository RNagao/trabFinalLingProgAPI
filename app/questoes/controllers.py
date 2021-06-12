from flask import request, jsonify
from flask.views import MethodView

from .models import Questoes
from .schemas import QuestoesSchema
from ..utils.filters import filters

class QuestoesList(MethodView):
    def post(self):
        data = request.json
        schema = QuestoesSchema()

        questao = schema.load(data)

        questao.save()

        return schema.dump(questao), 201

class QuestoesDetail(MethodView):
    def post(self, numero_questao):
        data = request.json
        schema = filters.getSchema(
            qs = request.args,
            schema_cls=QuestoesSchema,
            many=False
        )
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        gabarito = schema.dump(questao)
        print (gabarito)
        print (data)
        if (data["resposta"] == gabarito["resposta"]):
                return {"resultado": "certo"}
        return {"resultado": "errado"}

    def get(self, numero_questao):
        schema = filters.getSchema(
            qs = request.args,
            schema_cls=QuestoesSchema,
            many=False
        )
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        return schema.dump(questao), 200

    def delete(self, numero_questao):
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        questao.delete(questao)
        return {}, 204

class QuestaoAleatoria(MethodView):
    def get(self):
        return