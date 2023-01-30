from pymongo import MongoClient
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbjungle

# HTML을 주는 부분


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/memo/list', methods=['GET'])
def card_list():
    result = list(db.memoList.find({},{'_id' :False}))
    return jsonify({'result': 'success', 'list': result})
    


@app.route('/memo/add',methods=['POST'])
def add_card():

    
    title = request.form['title']
    result = list(db.memoList.find({'title':title},{'_id' : False}))
    if len(result) > 0:
        return jsonify({'result' : 'fail'})
    text = request.form['text']
    doc = {
        'title' : title,
        'text' : text,
    }
    db.memoList.insert_one(doc)



    return jsonify({'result' : 'success'})


@app.route('/memo/update', methods=['POST'])
def update_list():
    first = request.form['first']
    title = request.form['title']
    text = request.form['text']
   
    result = list(db.memoList.find({'title':title},{'_id' : False}))
    if len(result) > 0 and first != title:
        return jsonify({'result' : 'fail'})
    db.memoList.update_one({'title':first},{'$set': {"text": text,"title": title}})
    return jsonify({'result': 'success'})


@app.route('/memo/delete', methods=['POST'])
def delete_list():

    title = request.form['title']
    db.memoList.delete_one({'title' : title})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)