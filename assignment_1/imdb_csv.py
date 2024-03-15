import csv

with open('movies_initial.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = []
    for row in reader:
        rows.append(row)

    def get_movies_by_director(data, director):
        movies = []
        for row in data:
            if director in row[7]:
                movies.append(row)
        print(movies)
        return movies
    
    # get_movies_by_director(rows, 'Nolan')

    def get_movies_filtered_by_country(data, country):
        # country is 18 column
        movies = []
        for row in data:
            if country in row[17]:
                movies.append(row)
        print(movies)
        return movies
    
    # get_movies_filtered_by_country(rows, 'India')

    def get_movies_by_language(data, language):
        # language is 17 column
        movies = []
        for row in data:
            if language in row[16]:
                movies.append(row)
        print(movies)
        return movies
    
    # get_movies_by_language(rows, 'Hindi')

# Movies having IMDB rating more greater than 7 and having ratings greater than 1000
    
    def get_movies_by_imdb_rating(data):
        movies = []
        for row in data:
            if row[11] != '' and float(row[11]) > 7 and row[12] != '' and int(row[12]) > 1000:
                movies.append(row)
        print(movies)
        return movies
    
    get_movies_by_imdb_rating(rows)