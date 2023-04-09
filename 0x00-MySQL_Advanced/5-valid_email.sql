-- Reset the attribute valid_email 
-- Only when the email is changed

DELIMITER $$ ;
CREATE TRIGGER email_trig
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END $$
DELIMITER ;