-- left join shows and genres
SELECT ts.title, g.genre_id FROM tv_shows as ts
LEFT JOIN tv_show_genres as g ON s.id = g.show_id ORDER BY s.title, g.genre_id;
