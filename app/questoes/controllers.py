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
        return 

    def get(self, numero_questao):
        schema = filters.getSchema(
            qs = request.args,
            schema_cls=QuestoesSchema,
            many=False
        )
        questao = Questoes.query.filter_by(numero_questao).first_or_404()
        return schema.dump(questao), 200

    def delete(self, numero_questao):
        questao = Questoes.query.filter_by(numero_questao).first_or_404()
        questao.delete(questao)
        return {}, 204

class QuestaoAleatoria(MethodView):
    def get(self):
        return