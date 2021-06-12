from flask import request, jsonify
from flask.views import MethodView
import random

from .models import Questoes
from .schemas import QuestoesSchema
from ..utils.filters import filters

class QuestoesList(MethodView):
    def post(self):
        data = request.get_json(force=True)
        schema = QuestoesSchema()

        questao = schema.load(data)

        questao.save()

        return schema.dump(questao), 201

class QuestoesDetail(MethodView):
    def post(self, numero_questao):
        data = request.get_json(force=True)

        schema = filters.getSchema(
            qs = request.args,
            schema_cls=QuestoesSchema,
            many=False
        )
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        gabarito = schema.dump(questao)
  
        if (data['resposta'] == gabarito["resposta"]):
                return {"resultado": "certo"}, 200
        return {"resultado": "errado"}, 200

    def get(self, numero_questao):
        schema = filters.getSchema(
            qs = request.args,
            schema_cls=QuestoesSchema,
            many=False,
            rel=['resposta', 'create_time', 'update_time']
        )
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        return schema.dump(questao), 200

    def delete(self, numero_questao):
        questao = Questoes.query.filter_by(numero=numero_questao).first_or_404()
        questao.delete(questao)
        return {}, 204

class QuestaoAleatoria(MethodView):
    def get(self):
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=QuestoesSchema,
            many=True,
            rel=['resposta', 'create_time', 'update_time']
        )
        questoes = schema.dump(Questoes.query.all())
        questao = questoes[random.randint(0, len(questoes) - 1)]
        return questao, 200