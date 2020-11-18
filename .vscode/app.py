from flask import Flask, redirect, url_for, request
from flask_pymongo import PyMongo
# from flask_pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://newUser:newUser@cluster0.n4cos.mongodb.net/quiz?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/addQues', methods = ['POST'])
def addQues():
    db_collection = mongo.db.ques
    req_data = request.get_json()
    print (req_data)
    db_collection.insert_one(req_data)
    # question = req_data['question']
    # options = req_data['options']
    # answer = req_data['answer']
    return "Added"
    # return '''
    #        The question is: {}
    #        The options are: {}
    #        The answer in : {}
    #        '''.format(question, options, answer)

@app.route('/score', methods = ['POST'])
def score():
    data = request.get_json()
    # print(data)
    # temp = [{"opt":"Iron Man","related":"Iron Man"},{"opt":"Hulk","related":"Hulk"},{"opt":"Thor", "related":"Thor"},{"opt":"Hulk","related":"Hulk"}]
    # n = len(temp)
    # print (temp[0])
    # next((item for item in data if item["related"] == "Hulk"))
    
    #global max_count
    freq_count = 0
    #global result 
    result = ""
    def check(temp):
        count = 0
        
        #print(max_count)
        #print(temp)
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
    # app.debug = True
    # app.run()
    # app.run(debug=True)