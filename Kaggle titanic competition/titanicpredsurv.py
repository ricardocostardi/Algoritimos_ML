import pandas as pd 
import numpy as np 
from sklearn import preprocessing,  neighbors, svm, cross_validation
from sklearn.naive_bayes import MultinomialNB



#Li o arquivo de treino em CSV

df = pd.read_csv('train.csv')

# substitui os valures nulos, por 9999.

df.fillna(value=9999,inplace=True)

# Retirei as colunas que não interessão para mim

df.drop(['PassengerId','Name','Ticket','Fare','Cabin'], 1, inplace=True)


# No eixo X, ou seja as features ficam todas as colunas, menos a classe

X_df = df.drop(['Survived'], 1)

# No eixo Y somente a classe, ou aquilo que está se tentando prever

Y_df = df['Survived']



# Transformo as colunas não numericas em colunas numericas

Xdummies_df = pd.get_dummies(X_df,columns=['Embarked','Sex'])
Ydummies_df = Y_df



X = Xdummies_df
y = Ydummies_df



# Realizo a divisão da minhas base para treino e para saber o quão foi o algoritimo

X_train, X_test, y_train, y_test =  cross_validation.train_test_split(X, y, test_size=0.2)


# Utilizo o algoritimo support vector machines

svmm = svm.SVC()

# Treino

svmm.fit(X_train, y_train)

# Vejo como ele se sai contra o resto da base reservado para teste, dentro da base de treino

confidencee = svmm.score(X_test, y_test)

#############################################################################


# Agora irei fazer a mesma coisa para o arquivo de teste, poderia fazer uma função
# desse algoritimo e chama-la para realizar a previsão para outros arquivos
# mas não irei fazer isso agora.

#Li o arquivo de treino em CSV

df = pd.read_csv('test.csv')

# substitui os valures nulos, por 9999.

df.fillna(value=9999,inplace=True)

# Retirei as colunas que não interessão para mim

df.drop(['Name','Ticket','Fare','Cabin'], 1, inplace=True)


# No eixo X, ou seja as features ficam todas as colunas, menos a classe

X_df = df

# No eixo Y somente a classe, ou aquilo que está se tentando prever





# Transformo as colunas não numericas em colunas numericas

Xdummies_df = pd.get_dummies(X_df,columns=['Embarked','Sex'])




X = Xdummies_df



"""

def predicttitanic(x):

	x.drop(['PassengerId'])

	return(svmm.predict(x))
"""
# predicttitanic(passanger)

print(svmm.predict(X))