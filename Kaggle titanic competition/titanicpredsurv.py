import pandas as pd 
import numpy as np 
from sklearn import preprocessing,  neighbors, svm
from sklearn.naive_bayes import MultinomialNB



df = pd.read_csv('train.csv')

df.drop(['PassengerId','Name','Ticket'], 1, inplace=True)


df = df.astype(object).where(pd.notnull(df),None)


X_df = df.drop(['Survived','Cabin'], 1)
Y_df = df['Survived']



Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df



X = Xdummies_df
y = Ydummies_df



clf = MultinomialNB()

clf.fit(X, y)

"""

dft = pd.read_csv('test.csv')

print(dft)

dft = pd.read_csv('test.csv')


dft.drop(['PassengerId'], 1, inplace=True)
dft = pd.get_dummies(dft['Embarked'])

X_test = np.array(dft.drop(['Survived','Cabin'], 1))
y_test = np.array(dft['Survived'])


confidence = clf.score(X_test, y_test)
"""

dft = pd.read_csv('test.csv')

dft.drop(['PassengerId','Name','Ticket'], 1, inplace=True)


dft= dft.astype(object).where(pd.notnull(dft),None)


X_dft = dft.drop(['Survived','Cabin'], 1)
Y_dft = dft['Survived']



Xdummies_dft = pd.get_dummies(X_dft)
Ydummies_dft = Y_dft

X_test = Xdummies_dft
y_test = Ydummies_dft


confidence = clf.score(X_test, y_test)

print(confidence)