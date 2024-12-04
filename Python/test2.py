from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask (__name__)
api = Api(app)

todos = {
    1: {"task": "write hello world program","summary":"write the code using python."},
    
}

class ToDo(Resource):
    def get (self, todo_id):
        if todo_id not in todos:
            return{'message': 'todo not found'}
        return todos[todo_id]
    
    def post (self, todo_id):
        data = request.get_json()
        if todo_id in todos:
            abort(409, message="task alredy exist")
        else:
            todos[todo_id] = data 
            return todos[todo_id]
        
def put(self, todo_id):
    data = request.get_json()
    if todo_id not in todos:
        abort(404, message="task not found ")
        todos[todo_id]=data
        return todos[todo_id]
    
    def delete(self, todo_id):
        if todo_id not in todos:
            return {'message': 'invalid todo id'}
        else:
            del todos[todo_id]
            return {'message': 'deleted todo'}
        
class ToDoList(Resource):
    def get (self):
        return todos
        
api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')
if __name__ == '__main__':
    app.run(debug=True)
