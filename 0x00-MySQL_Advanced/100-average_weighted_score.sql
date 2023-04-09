-- store average 
-- With an input with user_id

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE weighted_score FLOAT DEFAULT 0;
    DECLARE num_projects INT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;
    
    SELECT COUNT(*) INTO num_projects FROM projects;
    
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
    
    SELECT 
        SUM(CASE project_id WHEN @project_c THEN score ELSE 0 END) as c_score,
        SUM(CASE project_id WHEN @project_py THEN score ELSE 0 END) as py_score
    FROM corrections
    WHERE user_id = user_id;
    
    SET weighted_score = (c_score * 0.6) + (py_score * 0.4);
    SET total_weight = num_projects * 100;
    
    IF total_weight > 0 THEN
        SET avg_weighted_score = (weighted_score / total_weight) * 100;
    END IF;
    
    UPDATE users SET average_score = avg_weighted_score WHERE id = user_id;
END $$
DELIMITER ;
