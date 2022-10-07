import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go
import logging
import sys

logging.StreamHandler(sys.stdout)

my_data_url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv"
def data_import(url):
    data = pd.read_csv(url)
    logging.info(data.head())
    return data

def plot_figures(data: pd.DataFrame):
    figure = px.scatter(data_frame = data, x="Sales",
                    y="TV", size="TV", trendline="ols")
    figure.show()

    figure = px.scatter(data_frame = data, x="Sales",
                    y="Newspaper", size="Newspaper", trendline="ols")
    figure.show()

    figure = px.scatter(data_frame = data, x="Sales",
                        y="Radio", size="Radio", trendline="ols")
    figure.show()


# correlation = data.corr()
# print(correlation["Sales"].sort_values(ascending=False))

def prepare_train_test_set(data):
    x = np.array(data.drop(["Sales"], axis=1))
    y = np.array(data["Sales"])
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.2, 
                                                    random_state=42)
    return xtrain, xtest, ytrain, ytest

def build_and_fit_model(xtrain, xtest, ytrain, ytest):
    model = LinearRegression()
    model.fit(xtrain, ytrain)
    print(model.score(xtest, ytest))
    return model

def prediction(model, features):
#features = [[TV, Radio, Newspaper]] of data[0]
    print(model.predict(features))

if __name__ == '__main__':
    data = data_import(my_data_url)
    xtrain, xtest, ytrain, ytest = prepare_train_test_set(data)
    model = build_and_fit_model(xtrain, xtest, ytrain, ytest)