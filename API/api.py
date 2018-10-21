from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def home():
    return {'hello': 'world'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# app = Flask(__name__)
# api = Api(app)

# @app.route('/')
# def hello_world():
    # return 'Flask Dockerized'

# class HelloWorld(Resource):
    # def get(self):
        # return {'hello': 'world'}

# class Sharks(Resource):
	# def post(self):
		# request_json = request.get_json()
		# sharktype = request.args.get('type',"")
		# if sharktype.lower() == 'greatwhite':
			# return json.dumps({'Name': 'white'})
		# else:
			# return json.dumps({'Name':'NOPEEE','Age':0,'Type':'Left Shark'})

# api.add_resource(HelloWorld, '/hello')
# api.add_resource(Sharks, '/sharks')

# if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')