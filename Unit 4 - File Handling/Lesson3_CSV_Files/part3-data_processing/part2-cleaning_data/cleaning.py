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
        print(movie)
        # print(f"ID: {movie['Movie_ID']}, Title: {movie['Title']}, Year: {movie['Release_Year']}, Rating: {movie['Rating']}" )

def main():
    print("=== Part 1: Reading and Exploring Data ===")
    # Step 1: Read the movie_data.csv file
    movies = read_csv_file("movie_data.csv")
    print(f"Total movies in dataset: {len(movies)}")
    # Step 2: Print the total number of movies
    print_movie_info(movies,200)

if __name__ == "__main__":
    main()
