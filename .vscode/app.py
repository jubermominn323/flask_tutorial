from flask import Flask, redirect, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://newUser:newUser@cluster0.n4cos.mongodb.net/quiz?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/addQues', methods = ['POST'])
def addQues():
    db_collection = mongo.db.ques
    req_data = request.get_json()
    print (req_data)
    db_collection.insert_one(req_data)
    return "Added"
    

@app.route('/score', methods = ['POST'])
def score():
    data = request.get_json()
    
    freq_count = 0 
    result = ""
    def check(temp):
        count = 0
        for value in data:
            if value['related'] == temp:
                count = count + 1
                nonlocal freq_count
                nonlocal result
                if count >= freq_count:
                    freq_count = count
                    result = value['related']
        
    for value in data:
        check(value['related'])
        
    return '''
        You are {}
    '''.format(result)

if __name__ == '__main__':
    app.run(debug=True)
    