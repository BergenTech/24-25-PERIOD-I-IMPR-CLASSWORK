import csv
def read_csv_file(file_path):
    movies = []
    with open(file_path, 'r', encoding="utf-8", newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movies.append(row)
    return movies

def print_movie_info(movies, num_movies=5):
    print(f"Showing {min(num_movies, len(movies))} movies:")
    for i in range(min(num_movies, len(movies))):
        movie = movies[i]
        # print(movie)
        print(f"ID: {movie['Movie_ID']}, Title: {movie['Title']}, Year: {movie['Release_Year']}, Rating: {movie['Rating']}" )

def clean_movie_data(movies):
    cleaned_movies = []
    seen_ids = set()
    for movie in movies:
        #skip if we've seen this movie id before
        if movie["Movie_ID"] in seen_ids:
            continue
        # Add to set of seen IDs
        seen_ids.add(movie["Movie_ID"])
        # Make a copy of the movie to clean
        clean_movie = movie.copy()
        #1 - Fix the capitalization in titles
        clean_movie["Title"] = clean_movie['Title'].strip().title()
        #2 - Handle missing values
        if not clean_movie['Rating'] or clean_movie['Rating'].strip()=="":
            clean_movie['Rating'] = "0.0"
        if not clean_movie['Genre'] or clean_movie['Genre'].strip()=="":
            clean_movie['Genre'] = "Unknown"
        cleaned_movies.append(clean_movie)    
    return cleaned_movies

def main():
    print("=== Part 1: Reading and Exploring Data ===")
    # Step 1: Read the movie_data.csv file
    movies = read_csv_file("movie_data.csv")
    print(f"Total movies in dataset: {len(movies)}")
    # Step 2: Print the total number of movies
    print_movie_info(movies,7) # will print first 5 as default
    # print_movie_info(movies, 1) # will print only 1 movie
    # print_movie_info(movies, 200) # will for the length of the list of dict
    # Step 3 - Display the first 5 cleaned movies
    cleaned_movies = clean_movie_data(movies)
    print_movie_info(cleaned_movies,7)
if __name__ == "__main__":
    main()
