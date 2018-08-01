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
CREATE TABLE character (
	                                        id integer PRIMARY KEY,
	                                        name text NOT NULL,
	                                        hp interger NOT NULL,
	                                        atk interger NOT NULL,
	                                        def interger NOT NULL,
	                                        disc text
	                                    );
INSERT INTO `character` VALUES (1,'IVXX',200,15,1,'1st character');
CREATE TABLE "adv1_map" (
	`id`	integer,
	`name`	text NOT NULL,
	`geoidy`	interger NOT NULL,
	`geoidx`	interger NOT NULL,
	`geoidz`	INTEGER NOT NULL,
	`disc`	text NOT NULL,
	`mobden`	interger NOT NULL,
	PRIMARY KEY(id)
);
INSERT INTO `adv1_map` VALUES (1,'North Room',0,1,0,'This is the North Room',35);
INSERT INTO `adv1_map` VALUES (2,'South Room',0,-1,0,'This is the South Room',1);
INSERT INTO `adv1_map` VALUES (3,'East Room',1,0,0,'This is the East Room',1);
INSERT INTO `adv1_map` VALUES (4,'West Room',-1,0,0,'This is the West Room',15);
INSERT INTO `adv1_map` VALUES (5,'Northeast Room',1,1,0,'This is the Northeast Room',35);
INSERT INTO `adv1_map` VALUES (6,'Southeast Room',1,-1,0,'This is the Southeast Room',1);
INSERT INTO `adv1_map` VALUES (7,'Northwest Room',-1,1,0,'This is the Northwest Room',1);
INSERT INTO `adv1_map` VALUES (8,'Southwest Room',-1,-1,0,'This is the Southwest Room',15);
INSERT INTO `adv1_map` VALUES (9,'BaseCamp',0,0,0,'This is the BaseCamp',15);
INSERT INTO `adv1_map` VALUES (10,'Northeast Passage',2,1,0,'New Northeast Passage',1);
COMMIT;
