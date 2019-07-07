def read_text():
    quotes = open("/home/mt/python_udacity_notes_and_projects/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()

