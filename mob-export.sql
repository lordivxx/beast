BEGIN TRANSACTION;
CREATE TABLE mob (
	                                        id integer PRIMARY KEY,
	                                        name text NOT NULL,
	                                        hp interger NOT NULL,
	                                        atk interger NOT NULL,
	                                        def interger NOT NULL,
	                                        disc text
		                                );
INSERT INTO `mob` VALUES (1,'Raptor',50,2,1,NULL);
INSERT INTO `mob` VALUES (2,'Tauren',100,2,1,NULL);
INSERT INTO `mob` VALUES (3,'Cat',75,15,1,NULL);
INSERT INTO `mob` VALUES (4,'Dragon',200,2,15,NULL);
COMMIT;
