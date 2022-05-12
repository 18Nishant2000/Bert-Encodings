from flask import Flask, request, Response
import main as m

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the MOLECULE BACKEND API</h1>"
    

@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        data = request.get_json()
        try:
            query = data['query']
            print(query)
            result = m.run(query)
            return result
        except:
            return Response(response='fail')
    return Response(response='GET Request', status=404)

if __name__ == '__main__':
    app.run()