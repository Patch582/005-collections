import urllib.request
from collections import namedtuple, Counter
from collections import defaultdict
import csv

movie = namedtuple('movie','title year score')

def print_header():
    print('------------------------------------------')
    print('             CSV Parser App')
    print('------------------------------------------')
    print()


def get_movies_by_director(data):
    directors = defaultdict(list)

    with open(data, 'r', encoding='utf-8') as f:
    # with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                title = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
                # print('Score: {}'.format(score))
            except ValueError as ve:
                print('Error: {}'.format(ve))
                continue

            m = movie(title=title, year=year, score=score)
            print('movie: {}'.format(m))
            directors[director].append(m)

    return directors


def main():
    print_header()

    # TODO: get movie data

    movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
    movies_csv = 'movies.csv'
    urllib.request.urlretrieve(movie_data, movies_csv)

    # TODO: parse data into defaultdict
    directors = get_movies_by_director(movies_csv)
    # print('Directors & Movies {}'.format(directors))

    # TODO: list movies for a (director)
    director_name = input('Grab a movie list for which Director? ')
    print('Movies for {}: {}'.format(director_name, directors[director_name]))

    # TODO: top (n) directors - based on number of movies
    number_directors = int(input('The top [n] directors? '))

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print('Most common directors: {}'.format(cnt.most_common(number_directors)))

if __name__ == '__main__':
    main()
