import pandas as pd

file = "resources/cities.csv"
cities_df = pd.read_csv(file)
cities_html = cities_df.to_html()
html_file = open('templates/data1.html', 'w')
html_file = html_file.write(cities_html)