USE `convergence2k19`;
DELIMITER $$
CREATE TRIGGER Deleted_Student
	AFTER DELETE ON student_data
    FOR EACH ROW
BEGIN
	INSERT INTO `log__deleted__students` (`STUDENT_KEY`, `FIRSTNAME`, `LASTNAME`, `ENROLLMENT_NO`, `BRANCH`, `SEM`, `COLLEGE`, `EMAIL`, `MOBILE`, `EVENT_1`, `EVENT_2`, `CAMP_ID`, `DELETED_DATE`) VALUES (OLD.STUDENT_KEY, OLD.FIRSTNAME, OLD.LASTNAME, OLD.ENROLLMENT_NO, OLD.BRANCH, OLD.SEM, OLD.COLLEGE, OLD.EMAIL, OLD.MOBILE, OLD.EVENT_1, OLD.EVENT_2, OLD.CAMP_ID,NOW());
END