import math, random
from collections import defaultdict, Counter
from linear_algebra import dot


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