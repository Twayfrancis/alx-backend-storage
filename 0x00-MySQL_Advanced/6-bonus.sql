-- script creates a stored procedure ADDBonus that adds a new correction for a student
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a user_id value
-- project_name, a new or already exists projects
-- score, the score valeu for the correction

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
	INSERT INTO projects(name) SELECT project_name FROM DUAL
	WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name LIMIT 1);

	INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;

//

DELIMITER ;
