from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)


class CallingAPI(Resource):
    

    def get(self):
        return {"status": "hi this flask setup was successful",
                "message": "Nothing sent in the data part"
                }

    def post(self):
        message = None

        if request.form['data'] == "dateandtime":
            message = str(datetime.now())

        if request.form['data'] == "name":
            message = "Arnab"

        return {"message": message}
        

api.add_resource(CallingAPI, '/messagereader')

if __name__ == "__main__":
    app.run(debug=True)
