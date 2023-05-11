SELECT title FROM movies WHERE id IN (
SELECT movie_id FROM stars
JOIN people ON stars.person_id = people.id
WHERE people.name = 'Johnny Depp' AND movie_id IN (
SELECT movie_id FROM stars
JOIN people ON stars.person_id = people.id
WHERE people.name = 'Helena Bonham Carter'
));
-- Acima: Pega os títulos dos IDs onde o nome corresponde a JD e os IDs estejam numa lista de filmes da HBC.

--Alternativa: Buscar os filmes de ambos os atores, agrupar os títulos contando os que aparece o título 2x
--SELECT movies.title FROM stars
--JOIN movies ON stars.movie_id = movies.id
--JOIN people ON stars.person_id = people.id
--WHERE people.name IN ('Johnny Depp', 'Helena Bonham Carter')
--GROUP BY movies.title
--HAVING COUNT(movies.title) = 2;