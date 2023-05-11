SELECT name FROM people WHERE id IN (
SELECT DISTINCT(person_id) FROM stars
WHERE movie_id IN (SELECT movie_id FROM stars
JOIN people ON stars.person_id = people.id
WHERE name = 'Kevin Bacon' AND birth = 1958) AND
person_id NOT IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958));