import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movie =""

def movies_prediction(movie = "avengers"):
    
    # loading data set of movies
    movies_data = pd.read_csv(r'C:\Users\JASH\Desktop\MCA\ML DataSet\movies1.csv')

    # selectimg the relevant features for recommandation
    selected_features = ['genres','keywords','tagline','cast','director']
    #print(selected_features)

    #replacing the null values with null string
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')


    # combing all the Selected features
    combine_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

    #print(combine_features)


    # converting the text data to feature vectors 
    vectorizer = TfidfVectorizer()


    feature_vectors = vectorizer.fit_transform(combine_features)
    #print(feature_vectors)


    # getting the similarity scores using cosine similarity
    similarity = cosine_similarity(feature_vectors)
    #print(similarity)

    #print(similarity.shape)


    # getting the movie name / user input
    movie_name = movie


    # creating a list with all the names given in the dataset
    list_of_all_titles = movies_data['title'].tolist()
    #print(list_of_all_titles)


    # finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    #print(find_close_match)

    close_match = find_close_match[0]
    #print(close_match)


    # finding the index of the movies with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    #print(index_of_the_movie) 


    # getting a list of similar movies
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    #print(similarity_score)

    #len(similarity_score)

    #sorting the movies based on thier similarity score
    sorting_similarity_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    #print(sorting_similarity_movies)



    # print the name of similar movies  based on the index

    #print("Movies Suggested for your: \n")

    i=1
    lis = []

    for movie in sorting_similarity_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        
        if(i<30):
            print(i,'.',title_from_index)
            lis.append(title_from_index)
            i+=1
    return lis

#movies_prediction(movie)










