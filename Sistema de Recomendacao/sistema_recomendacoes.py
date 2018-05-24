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

"""
Agora para achar usuarios similares e sugerir coisas nas quais eles
tenham interesses irei usar a similaridade do cosseno. Com dois vetores v e w
sera medido o angulo entre v e w, se os dois apontarem para a mesma direcao
então a similaridade do cosseno e 1, caso apontem para direções opostas  a similaridade
será -1. e se um dos vetores forem zero a similaridade será também 0.
Com isso teremos um indice de similaridade entre usuarios.
Para calcular isso irei definir duas funções.

"""

"""

A primeira função dot recebe dois vetores como parametro
e multiplica seus elementos Ex v1 * w1, v2 * w2...
Isso ira me permitir multipicar os elementos dos vetores um a um.
a função zip permiter iterar em tuplas, o que e necessario aqui, pois
o primiro elemento do vetor v tem que ser multiplicado pelo
primeiro elemento do vetor w e assim por diante

"""


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

"""

A segunda função ira implentar a formula para a similaridade dos cossenos.
A formula e a seguinte produto dos vetores v, w dividido pela raiz quadrada dos
vetores v e w ao quadrado, o resultoado ira variar de -1 a 1

mais info sobre a formula: https://en.wikipedia.org/wiki/Cosine_similarity

"""    

def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v,v) * dot(w, w))



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



# Agora podemos calcular a similariedades em pares dos nossos usuarios
# importante que isso de calcular todas as similariedades dos usuarios 
# e algo que funciona com bases pequenas médias, em bases muito grandes
# e interessante transformar isso em uma função e algo parecido

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interest_matrix]
                     for interest_vector_i in user_interest_matrix]


"""

Agora que temos mapeados todas as similariedades entre todos os usuarios
podemos definir uma função que traga os usuarios mais similares a um determinado
usuario, tirando usuarios com similariedade 0 e o proprio usuario

"""

def most_similar_users_to(user_id):
    pairs = [(other_user_id, similarity)

    # o enumerate realiza um count na lista, começando do zero até o final
    # ou seja no meu caso ira trazer o 'ID' do usuario e sua similariedade        

             for other_user_id, similarity in enumerate(user_similarities[user_id])

    #tirando o proprio ID que estamos utilizando e só trazendo similaridade maior que 0   

             if user_id != other_user_id and similarity > 0 ]
      
    #retorna a lista ordenada pelos mais similares primeiro

    return sorted(pairs, key=lambda pair: pair[1], reverse=True)    

print(most_similar_users_to(0))



         #...continua