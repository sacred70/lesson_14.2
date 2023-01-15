# coding: utf8
from flask import Flask, render_template
from function import search_title
from function import search_year
from function import search_rating
from function import search_genre


app = Flask(__name__)


# show_id text
# type text
# title text
# director text
# cast text
# country text
# date_added datetime
# release_year int
# rating text
# duration int
# duration_type text
# listed_in text
# description text

@app.route("/movie/<title>")
def search_name(title):
    return search_title(title)


@app.route("/movie/<int:year_from>/to/<int:year_to>")
def search_release_year(year_from, year_to):
    return search_year(year_from, year_to)


@app.route("/rating/<inquiry>")
def search_rating_(inquiry):
    inquiry = str(inquiry)
    return search_rating(inquiry)


@app.route("/genre/<genre>")
def search_genre_10(genre):
    return search_genre(genre)


app.run()
