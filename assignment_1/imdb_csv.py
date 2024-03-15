import csv
import os
from fpdf import FPDF

# Create a directory to store the output pdf files
if not os.path.exists('assignment_1/output_pdf'):
    os.mkdir('assignment_1/output_pdf')

# Read the csv file and store the data in a list
with open('assignment_1/movies_initial.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    # Selecting only the required columns
    header = [header[1],header[4],header[6],header[7],header[11],header[12],header[16],header[17]]
    

    rows = []
    for row in reader:
         # Selecting only the required columns
        row = [row[1],row[4],row[6],row[7],row[11],row[12],row[16],row[17]]
        rows.append(row)

    # Function to get movies by director
    def get_movies_by_director(data, director):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        movies = []
        pdf.cell(200, 10, txt=", ".join(header).encode('utf-8').decode('latin-1'), ln=True,border=True, align='C')
        for row in data:
            if director in row[3]:
                movies.append(row)
                pdf.cell(200, 10, txt=", ".join(row).encode('utf-8').decode('latin-1'), ln=True,)
        pdf.output("assignment_1/output_pdf/movies_by_director.pdf")
        return movies
    

    
    # Function to get movies by country
    def get_movies_filtered_by_country(data, country):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        movies = []
        pdf.cell(180, 10, txt=", ".join(header).encode('utf-8').decode('latin-1'), ln=True,border=True, align='C')
        movies = []
        for row in data:
            if country in row[7]:
                movies.append(row)
                pdf.cell(150, 10, txt=", ".join(row).encode('utf-8').decode('latin-1'), ln=True,)
        pdf.output("assignment_1/output_pdf/movies_by_country.pdf")
        return movies
    
    
    # Function to get movies by language
    def get_movies_by_language(data, language):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        movies = []
        pdf.cell(180, 10, txt=", ".join(header).encode('utf-8').decode('latin-1'), ln=True,border=True, align='C')
        movies = []
        for row in data:
            if language in row[6]:
                movies.append(row)
                pdf.cell(150, 10, txt=", ".join(row).encode('utf-8').decode('latin-1'), ln=True,)
        pdf.output("assignment_1/output_pdf/movies_by_language.pdf")
        return movies
    


    # Function to get movies by imdb rating and number of votes
    def get_movies_by_imdb_rating(data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        movies = []
        pdf.cell(180, 10, txt=", ".join(header).encode('utf-8').decode('latin-1'), ln=True,border=True, align='C')
        for row in data:
            if row[4] != '' and float(row[4]) > 7 and row[5] != '' and int(row[5]) > 1000:
                movies.append(row)
                pdf.cell(150, 10, txt=", ".join(row).encode('utf-8').decode('latin-1'), ln=True,)
        pdf.output("assignment_1/output_pdf/movies_by_imdb_rating.pdf")
        return movies
    

    
    get_movies_by_imdb_rating(rows)

    get_movies_by_director(rows, 'Nolan')

    get_movies_by_language(rows, 'Hindi')

    get_movies_filtered_by_country(rows, 'India')