import numpy as np 
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd 

"""
Usando pandas para ler os dados do arquivo e jogando
no meu dataframe. A biblioteca pandas já ira deixar tudo
acertado, colunas separadas e nomeadas

"""

df = pd.read_csv('breast-cancer-wisconsin.data.txt')

# utilizando replace para substituir as linhas em que o 
# valor for desconhecido por -99999, dessa forma ficara
# claro que se trata de um outlier e será descartado

df.replace('?',-99999, inplace=True)

# Deletando a coluna ID que não sera usada
# O uso do Inplace=True diz que a dado deve efetivamente
# ser retirado da tabela

df.drop(['id'], 1, inplace=True)

"""
Declaro o x e y do meu 'grafico', por convenção semr pre x e y
e com o x sempre maiúsculo. O eixo x ficam minhas features, meus atributos,
no eixo do y fica minha classe, ou aquilo que desejo prever
Então o que fiz foi, no x declarei que deve ter todas as colunas
menos a coluna class ( que e minha classe), e no eixo y só deve ter
a coluna class.

"""
X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

"""
Nessa parte eu declaro minhas variaveis de treino e teste,
tanto para o x quanto para o y. Utilizo o cross_validation
pois o mesmo realiza a sorteio (no sentido de misturar)
dos meus dados, evitando que a base de treino e de teste fique 
enviezada por algum motivo de repetição de dados, por fim
realizo a divisão da minha base, reservando 20% dela para teste
através do train_test_split

"""

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)



# inicio o Support Vector Classification

clf = svm.SVC()

# utilizo minhas variaveis para realizar a treino atraves
# da função .fit

clf.fit(X_train, y_train)

# utilizo outra variavel para gravar meu percentual de
# confiança, ouo seja, o tanto que meu modelo está acertando
# utilizando como comparação a amostra de test

confidence = clf.score(X_test, y_test)

print(confidence)

"""

Agora irei declarar um exemplo que eu mesmo irei criar
para o algoritimo prever o tipo que ele é

"""

example_measures = np.array([[4,2,1,1,1,2,3,2]])

# transformando em um vetor com reshape 

example_measures = example_measures.reshape(len(example_measures), -1)

# chamando a função predict para predizer a que classe pertence nosso exemplo

prediction = clf.predict(example_measures)
print(prediction)