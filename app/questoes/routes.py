from flask import Blueprint
from .controllers import QuestoesDetail, QuestoesList, QuestaoAleatoria

questoes_api = Blueprint('questoes_api', __name__)

questoes_api.add_url_rule(
    '/questoes', view_func=QuestoesList.as_view('questoes_list'), methods=['POST']
)

questoes_api.add_url_rule(
    '/questoes/<int:numero_questao>', view_func=QuestoesDetail.as_view('questoes_detail'), methods=['GET', 'DELETE', 'POST']
)

questoes_api.add_url_rule(
    '/questoes/random', view_func=QuestaoAleatoria.as_view('questoes_aleatorias'), methods=['GET']
)