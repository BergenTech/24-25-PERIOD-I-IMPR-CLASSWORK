"""
Movie Data Processing - Part 1: Reading Data
This script focuses on reading and exploring movie data from a CSV file.
"""

import csv

def read_csv_file(file_path):
    """
    Read the CSV file and return a list of dictionaries.
    Each dictionary represents one movie with column names as keys.
    """
    # Your code will go here
    movies = []
    with open(file_path, 'r', encoding="utf-8", newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movies.append(row)
    return movies

def print_movie_info(movies, num_movies=5):
    """
    Print information about the first num_movies in the list.
    """
    # Your code will go here
    print(f"Showing {min(num_movies, len(movies))} movies:")
    for i in range(min(num_movies, len(movies))):
        movie = movies[i]
        print(movie)
        # print(f"ID: {movie['Movie_ID']}, Title: {movie['Title']}, Year: {movie['Release_Year']}, Rating: {movie['Rating']}" )

def main():
    """
    Main function to read and explore the movie data.
    """
    print("=== Part 1: Reading and Exploring Data ===")
    
    # Step 1: Read the movie_data.csv file
    # Your code will go here
    movies = read_csv_file("movie_data.csv")
    print(f"Total movies in dataset: {len(movies)}")
    
    # Step 2: Print the total number of movies
    # Your code will go here
    print_movie_info(movies,200)
    # Step 3: Display the first 5 movies
    # Your code will go here
    
    # Step 4: Print some observations about data issues
    # print("\nObserved data issues:")
    # Your observations will go here

if __name__ == "__main__":
    main()
