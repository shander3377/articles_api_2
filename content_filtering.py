from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df1 = pd.read_csv('articles.csv')
df1 = df1[df1['title'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df1['title'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

df1 = df1.reset_index()
indices = pd.Series(df1.index, index=df1['contentId'])

def get_recommendations(contentId):
    idx = indices[int(contentId)]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return df1[["url", "title", "text", "lang", "total_events"]].iloc[article_indices].values.tolist()