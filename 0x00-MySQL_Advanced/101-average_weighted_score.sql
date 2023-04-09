-- create a stored procedure
-- compute and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DROP TEMPORARY TABLE IF EXISTS temp_weights;
    CREATE TEMPORARY TABLE temp_weights (
        user_id int,
        weighted_score float
    );

    -- calculate the weights
    INSERT INTO temp_weights (user_id, weighted_score)
    SELECT user_id, SUM(score) / COUNT(*) AS weighted_score
    FROM corrections
    GROUP BY user_id;

    -- Update the avarage score 
    UPDATE users
   	SET average_score=(SELECT AVG(weighted_score) FROM temp_weights)
	WHERE id IN (SELECT user_id FROM temp_weights);
    
    -- Drop temporary
    DROP TABLE temp_weights;


END;$$
DELIMITER ;
