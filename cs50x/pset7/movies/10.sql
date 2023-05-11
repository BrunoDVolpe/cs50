SELECT name FROM people WHERE id IN (SELECT DISTINCT(people.id) FROM people
JOIN directors ON directors.person_id = people.id
JOIN movies ON directors.movie_id = movies.id
JOIN ratings ON ratings.movie_id = movies.id
WHERE rating >= 9);