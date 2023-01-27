#api 서버 만들어야됨
#몽고DB 사용하기 위해 설치
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://test:test@54.180.160.102',27017)
db = client.dbFinal


# html 홈 화면
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/final/list', methods=['GET'])
def show_start():
    stars = list(db.list.find({},{'_id': False}).sort('like',-1))
    return jsonify({'result':'success', 'list' : stars})

    
@app.route('/final/add',methods=['POST'])
def add_list():

    
    name = request.form['name']
    recent_work = request.form['recent']

    doc = {
        'name' : name,
        'recent' : recent_work,
        'like' : 0,
    }
    db.list.insert_one(doc)
    print('완료!', name)

    return jsonify({'result' : 'success'})

@app.route('/final/delete', methods=['POST'])
def delete_list():

    name = request.form['name']
    db.list.delete_one({'name' : name})

    return jsonify({'result': 'success'})

@app.route('/final/like', methods=['POST'])
def like_list():
    name_give = request.form['name_give']
    db.list.update_one({'name':name_give},{'$set':{'like':db.list.find_one({'name':name_give})['like']+1}})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


