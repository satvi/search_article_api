from flask import request
from flask_restplus import reqparse,Namespace,Resource
from assignment import get_data

api=Namespace('search',description='searching article')

get_parser=reqparse.RequestParser()
get_parser.add_argument('search_title',required=True,help='',type=str)
@api.route('/search')

class Search(Resource):
    @api.doc('search')
    @api.expect(get_parser, validate=True)
    def get(self):
        try:
            searchQuery = {}
            title = request.args.get('search_title', None)

            if title is not None:
                searchQuery['search_title'] = title

            result = get_data(searchQuery)
            if result:
                return {'response_code': 200, 'status': 'sucess','result':result}
            else:
                return {'response_code': 200, 'status': 'sucess', 'result': 'No content avaliable for given word'}

        except Exception as e:
            return {'response_code':400,'status':'failure','result':'ERROR in search the word'}