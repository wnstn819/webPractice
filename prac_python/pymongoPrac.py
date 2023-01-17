from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 


#패트릭스의 평점 가져오기
target_movie = db.movies.find_one({'title':'매트릭스'})
print(target_movie['star'])




#  매트릭스 평점과 같은 평점의 영화 제목들을 가져오기
for movie in list(db.movies.find({})) :
    if target_movie['star'] == movie['star']:
        print(movie['title'])


# 매트릭스 영화의 평점 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star' :'0'}})


db.movies.update_one({'title':'매트릭스'},{'$set':{'star' :'9.39'}})