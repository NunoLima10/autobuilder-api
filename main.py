from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)
        

if __name__=="__main__":
    # api.add_resource(Scoreboard,"/")
    app.run(host='0.0.0.0', port=3000,debug=True)
