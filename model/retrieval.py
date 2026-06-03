
from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ast
import pandas as pd 


#loading data==============================================================
datalink = pd.read_csv("data/data_bersih_final.csv", on_bad_lines='warn')
sentences = datalink['stopword_removal']
print(datalink['stopword_removal'].head())

#mengubah data menjadi list of list===========================================================
datalink['stopword_removal'] = datalink['stopword_removal'].apply(ast.literal_eval)
print(type(datalink['stopword_removal'].iloc[0]))

#Trained Wors2Vec model============================================================
from gensim.models import Word2Vec

model = Word2Vec(
    sentences=datalink['stopword_removal'],
    vector_size=100,               # dimensi
    window=5,                      # konteks
    min_count=2,                   # buang kata jarang
    workers=4,
    sg=1,
    epochs=20
)

# mengubah data menjadi vektor==========================================================================================
def doc_vector(stopword_removal):
    vectors = []

    for word in stopword_removal:
        if word in model.wv:
            vectors.append(model.wv[word])

    if len(vectors) > 0:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

doc_vectors = np.array([
    doc_vector(doc) for doc in datalink['stopword_removal']
])

#menghitung retrieval dan cosine similarity==========================================================================================
def retrieve_documents(query, top_k=5):

    q_tokens = query.lower().split()

    q_vec = doc_vector(q_tokens)

    similarity = cosine_similarity(
        [q_vec],
        doc_vectors
    )

    top_idx = similarity[0].argsort()[-top_k:][::-1]

    results = []

    for i in top_idx:

        if similarity[0][i] > 0:

            results.append({
                "score": similarity[0][i],
                "poin_id": datalink['poin_id'].iloc[i],
                "keyword": datalink['keyword'].iloc[i],
                "title": datalink['title'].iloc[i],
                "text": datalink['text'].iloc[i]

            })

    return results

