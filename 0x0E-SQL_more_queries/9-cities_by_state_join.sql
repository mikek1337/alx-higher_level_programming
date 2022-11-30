-- Join cities and states
SELECT cities.id, cities.name, states.name FROM states 
inner join cities ON states.id = cities.state_id;

