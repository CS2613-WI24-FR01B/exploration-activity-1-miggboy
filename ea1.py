import pandas as pd
import numpy as np
import ast

# Movie Recommendation Program
# We use pandas to process a dataset of movies from IMDB
# Source: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
# Based on user preferences, we recommend a set of movies

# Read in the CSV file
df = pd.read_csv('movies_metadata.csv')

# Prompt user input for search
print("****************************")
print("This program will recommend 5 movies based on your preferences")
print("What category of film do you want to watch?")
genre = input("Example: Action, Fantasy, Thriller, Horror, etc: ")

rate = input("What is the minimum rating you'd prefer? Please enter 0-10: ")

# Convert the strings in the genres column to dictionaries
df['genres'] = df['genres'].apply(ast.literal_eval)

# Create DataFram by filtering movies by genre and minimum rating.
# We also only include movies with more than 100 user reviews - this filters out random outliers
# (ex: A movie that nobodies ever heard of from 1954 with a single 10 star review coming out on top)
filtered_movies = df[(df['genres'].apply(lambda x: any(d['name'] == genre for d in x))) & 
                     (df['vote_average'] >= float(rate)) & 
                     (df['vote_count'] > 100)]

# Sort the filtered movies by rating in descending order
sorted_movies = filtered_movies.sort_values(by='vote_average', ascending=False)

# Retrieve top 5 movies
recommendations = sorted_movies.head(5)

# Print the titles of the recommended movies
print(recommendations['title'])

# Note that often times if a user picks a high rating number, like 9, there will be less than 5, or even 0 recommendations
# This is because, realistically, there are very few IMDB movies that crack the upper-echelon while still being a relevant film
# with a fair amount of reviews. 