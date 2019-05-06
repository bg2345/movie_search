from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import SubmitForm, ShowDirector, GetDirectorLink
from app.models import Movie, Director
import requests

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():


    url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=bbb0e77b94b09193e6f32d5fac7a3b9c&language=en-US&page=1&region=GR'
    movies_json = requests.get(url).json()


    movies = []
    ids = []
    cast_urls = []
    directors = []
    dir_url = []

    for i, result in enumerate(movies_json['results']):
        row = {}
        row['id'] = result['id']
        row['title'] = result['title']
        row['description'] = result['overview']
        row['original_title'] = result['original_title']
        row['poster_path'] = result['poster_path']


        movies.append(row)
        ids.append(row['id'])

    for id in ids:
        url2 = 'https://api.themoviedb.org/3/movie/{}?api_key=bbb0e77b94b09193e6f32d5fac7a3b9c&append_to_response=credits'.format(id)
        cast_urls.append(url2)

        directors_json = requests.get(url2).json()

        dir_title = directors_json['title']

        for result in directors_json['credits']['crew']:
            if result['job'] == 'Director':
                row = {}
                row['id'] = result['id']
                row['name'] = result['name']
                dir_profile = 'https://api.themoviedb.org/3/person/{}?api_key=bbb0e77b94b09193e6f32d5fac7a3b9c&language=en-US'.format(result['id'])
                row['imdb'] = dir_title
                # dir_url.append(dir_profile)

                # url_json = requests.get(dir_profile).json()
                # print(url_json['imdb_id'])
                row['profile'] = dir_profile

                directors.append(row)

    for movie in movies:
        movie = Movie(
            id = movie['id'],
            title = movie['title'],
            description = movie['description'],
            original_title = movie['original_title']
            )

        # db.session.add(movie)
        # db.session.commit()

    for director in directors:
        director = Director(
            id = director['id'],
            name = director['name'],
            imdb = director['imdb'],
            profile = director['profile']
        )

        # db.session.add(director)
        # db.session.commit()


    return render_template('index.html', title='Home', movies=movies, directors=directors)
