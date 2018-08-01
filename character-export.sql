BEGIN TRANSACTION;
CREATE TABLE character (
	                                        id integer PRIMARY KEY,
	                                        name text NOT NULL,
	                                        hp interger NOT NULL,
	                                        atk interger NOT NULL,
	                                        def interger NOT NULL,
	                                        disc text
	                                    );
INSERT INTO `character` VALUES (1,'IVXX',200,15,1,'1st character');
COMMIT;
