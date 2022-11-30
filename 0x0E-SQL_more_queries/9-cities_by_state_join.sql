-- Join cities and states
SELECT cities.id as id, cities.name as name, states.name as name FROM states 
inner join cities ON states.id = cities.state_id ORDER BY cities.id;

