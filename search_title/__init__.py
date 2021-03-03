from flask import Blueprint
from flask_restplus import Api
from search_title.search import api as search

blueprint = Blueprint('apis', __name__)

api = Api(blueprint, title='content_search')


api.add_namespace(search, path='/search')