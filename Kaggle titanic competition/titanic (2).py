import pandas as pd 
import numpy as np 
from sklearn import preprocessing,  neighbors, svm, cross_validation
from sklearn.naive_bayes import MultinomialNB


test_df = pd.read_csv('train.csv')
train_df = pd.read_csv('test.csv')

