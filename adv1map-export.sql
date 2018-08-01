BEGIN TRANSACTION;
CREATE TABLE adv2_map (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        geoidy interger NOT NULL,
                                        geoidx interger NOT NULL,
                                        disc text NOT NULL,
                                        mobden interger NOT NULL
                                        );
INSERT INTO `adv2_map` VALUES (1,'North Room',0,1,'This is the North Room',35);
INSERT INTO `adv2_map` VALUES (2,'South Room',0,-1,'This is the South Room',1);
INSERT INTO `adv2_map` VALUES (3,'East Room',1,0,'This is the East Room',1);
INSERT INTO `adv2_map` VALUES (4,'West Room',-1,0,'This is the West Room',15);
INSERT INTO `adv2_map` VALUES (5,'Northeast Room',1,1,'This is the Northeast Room',35);
INSERT INTO `adv2_map` VALUES (6,'Southeast Room',1,-1,'This is the Southeast Room',1);
INSERT INTO `adv2_map` VALUES (7,'Northwest Room',-1,1,'This is the Northwest Room',1);
INSERT INTO `adv2_map` VALUES (8,'Southwest Room',-1,-1,'This is the Southwest Room',15);
INSERT INTO `adv2_map` VALUES (9,'BaseCamp',0,0,'This is the BaseCamp',15);
COMMIT;
