import pandas as pd

data=pd.read_csv('Top Indian Places to Visit.csv')

features = ['Google review rating' , 'time needed to visit in hrs' , 'Number of google review in lakhs']
weights = {'Google review rating' : 40, 'time needed to visit in hrs':-20, 'Number of google review in lakhs':20}
place_scores = data[features].mul(pd.Series(weights), axis=1).sum(axis=1)
    
data['Score'] = place_scores

def rank_weekend_places(city_name, data):

    city_data = data[(data['City'] == city_name) & (~data['Weekly Off'].str.contains('Saturday|Sunday'))]

    ranked_places = city_data.sort_values(by='Score', ascending=False)
    return ranked_places[['Name' , 'Type' , 'Score']]

city_name = input()

ranked_places = rank_weekend_places(city_name,data)
print("Top Weekend Places to Visit in" , city_name)
print(ranked_places.head(10))
