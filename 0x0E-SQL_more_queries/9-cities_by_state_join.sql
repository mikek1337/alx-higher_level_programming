-- Join cities and states
SELECT c.id , c.name , s.name FROM states as s
INNER JOIN cities as c ON s.id = c.state_id ORDER BY c.id;

