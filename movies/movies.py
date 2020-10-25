from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import adapters.repository as repo
import utilities.utilities as utilities
import movies.services as services

# from authentication.authentication import login_required


# Configure Blueprint.
movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route('/movies_by_genre', methods=['GET'])
def movies_by_genre():
    movies_per_page = 3

    # Read query parameters.
    genre_name = request.args.get('genre')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        movie_to_show_reviews = -1
    else:
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    movies = services.get_movie_by_genre(genre_name, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        prev_movie_url = url_for('movies_bp.movies_by_genre', tag=genre_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('movies_bp.movies_by_genre', tag=genre_name)

    if cursor + movies_per_page < len(movies):

        next_movie_url = url_for('movies_bp.movies_by_genre', tag=genre_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movies) / movies_per_page)
        if len(movies) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('movies_bp.movies_by_genre', tag=genre_name, cursor=last_cursor)

    for movie in movies:
        movie['view_review_url'] = url_for('movies_by_genre', tag=genre_name, cursor=cursor,
                                           view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('movies_bp.reviews_on_movie', movie=movie['id'])

    return render_template(
        'news/movies.html',
        title='Movies',
        movies_title='Movies tagged by ' + genre_name,
        movies=movies,
        selected_movies=utilities.get_selected_movies(len(movies) * 2),
        genre_urls=utilities.get_genres_and_urls(),
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )


@movies_blueprint.route('/review', methods=['GET', 'POST'])
@login_required
def review_on_movie():
    # Obtain the username of the currently logged in user.
    username = session['username']

    form = ReviewForm()

    if form.validate_on_submit():
        movie_id = int(form.movie_id.data)

        services.add_review(movie_id, form.review.data, username, repo.repo_instance)

        movie = services.get_movie(movie_id, repo.repo_instance)

        return redirect(url_for('movies_bp.movies', title=movie['title'], view_reviews_for=movie_id))

    if request.method == 'GET':

        movie_id = int(request.args.get('movie'))

        form.movie_id.data = movie_id
    else:

        movie_id = int(form.movie_id.data)

    movie = services.get_movie(movie_id, repo.repo_instance)
    return render_template(
        'movies/review_on_movie.html',
        title='Edit article',
        movie=movie,
        form=form,
        handler_url=url_for('movies_bp.review_on_movie'),
        selected_movie=utilities.get_selected_movies(),
        genre_urls=utilities.get_genres_and_urls()
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    movie_id = HiddenField("Movie id")
    submit = SubmitField('Submit')
