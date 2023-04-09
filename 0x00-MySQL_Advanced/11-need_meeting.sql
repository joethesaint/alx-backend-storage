-- create  a view
-- lists all students with score under 80

CREATE VIEW need_meeting
AS SELECT *
    FROM students
    WHERE score < 80
    AND (last_meeting = NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));