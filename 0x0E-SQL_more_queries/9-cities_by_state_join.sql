-- Join cities and states
SELECT c.id , c.name , s.name FROM cities as c
INNER JOIN states as s ON c.state_id = s.id ORDER BY c.id;

