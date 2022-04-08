from flask import Flask, jsonify, request
import sys
from storage import giveArticle, giveLiked, giveDisliked
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)
import csv
all_articles = []
with open("./articles.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
liked_articles = []
disliked_articles = []

@app.route("/getPopularArticles")
def popular_articles():
    data= []
    for article in output:
        d = {
            "url": article[0],
              "text": article[1],
            "title": article[2],
            "lang": article[3],
            "total_events": article[4]
        }
        data.append(d)
    return jsonify({
        "data": data,
        "status": "success"
    }), 200

@app.route("/recommendedArticles")
def recommendedArticles():

    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[4])
        for data in output:

            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "text": recommended[1],
            "title": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200




@app.route("/getArticle")
def getArticle():
    return jsonify({"data": all_articles[0], "status": "success"}) 

@app.route('/likedArticles', methods = ["POST"])
def likedArticles():
    # print(all_articles[0])
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    }), 201

@app.route('/dislikedArticles', methods = ["POST"])
def dislikedArticles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
  app.run()