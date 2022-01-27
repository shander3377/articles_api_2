from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, disliked_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations

app = Flask(__name__)

@app.route("/getPopularArticles")
def popular_articles():
    data: []
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
def recommended_articles():
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




@ap.proute("/getArticle")
def getArticle():
    return jsonify({"data": all_articles[0], "status": "success"}) 

@app.route('/likedArticles', methods = ["POST"])
def likedMovies():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/dislikedArticles', methods = ["POST"])
def likedMovies():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201


