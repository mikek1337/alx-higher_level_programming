-- join tv shows and there genres
SELECT ts.title, g.genre_id FROM tv_shows AS ts
INNER JOIN tv_show_genres AS g on ts.id = g.show_id ORDER BY ts.title, g.genre_id
