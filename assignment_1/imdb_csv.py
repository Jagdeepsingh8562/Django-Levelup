import csv
from fpdf import FPDF

with open('assignment_1/movies_initial.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = []
    for row in reader:
        rows.append(row)

    def get_movies_by_director(data, director):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=6)
        movies = []
        pdf.cell(200, 10, txt=", ".join(header).encode('utf-8').decode('latin-1'), ln=True,)
        for row in data:
            if director in row[7]:
                movies.append(row)
                pdf.cell(200, 10, txt=", ".join(row).encode('utf-8').decode('latin-1'), ln=True,)
        print(movies)
        pdf.output("assignment_1/output_pdf/movies_by_director.pdf")
        return movies
    
    get_movies_by_director(rows, 'Nolan')

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
    
    # get_movies_by_imdb_rating(rows)