from flask import Flask 
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'message':'hello, world'}
    
class HelloName(Resource):
    def get(self, name):
        return {'data':'hello, {}'.format(name)}
    
api.add_resource(Helloworld, '/helloworld');
api.add_resource(HelloName, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)