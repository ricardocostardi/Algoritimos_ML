import math, random
from collections import defaultdict, Counter



"""
Esse será um algoritimo para sistema de recomendação
que existe por exemplono netflix e na amazon. Claro que
a comprexidade desse não se equipara com os deles, mas e uma
introduçao de como pode ser desenvolvido um algoritimo do tipo
a base que irei utilizar sera feita na 'mão' para praticidade
mas ela pode vir de um banco de dados, arquivos JSON, CSV ou outras
fontes, neste caso serauma lista de listas, onde cada lista contém os
interesses de uma determinada pessoa.

"""

users_interests = [
    ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probability"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathematics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
    ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", "Big Data"],
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probability"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
    ["libsvm", "regression", "support vector machines"]
]


# Irei recomendar interesses para um usuario baseado em interesses em commun
# com outros usuarios

# Primeiro irei ordenar os interesses, e atribuir um indice para casa
# interesse unico

unique_interests = sorted(list({ interest 
                                  for users_interests in users_interests
                                  for interest in users_interests  }))


"""

Agora temos que saber em que cada um dos usuarios estão interessados
irei fazer uma função para interar sobre os interesses dos usuarios 
e me retornar um vetor com 1s e 0s sendo 1 o usuario tem interesse naquele
assunto e 0 não tem

"""

def make_user_interest_vector(users_interests):
    return [1 if interest in users_interests else 0
            for interest in unique_interests]

"""

Agora que tenho essa função, posso criar uma matrix de interesses dos usuarios
utilizando mapping

"""    

user_interest_matrix = list(map(make_user_interest_vector, users_interests))   

print(user_interest_matrix)   
                               