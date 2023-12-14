-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
-- Procedure ComputeAverageWeightedScoreForUsers is not taking any input.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS users,
	       (SELECT users.id, SUM(score * weight) / SUM(weight) AS weight_avg
	       FROM users AS users JOIN corrections AS correct ON users.id = correct.user_id
	       JOIN projects AS proj ON correct.project_id = proj.id
	       GROUP BY users.id)

	AS weight
	SET users.average_score = weight.weight_avg
	WHERE users.id = weight.id;
END;

//

DELIMITER ;