BEGIN TRANSACTION;
CREATE TABLE "character" (
	`id`	integer,
	`name`	text NOT NULL,
	`hp`	interger NOT NULL,
	`atk`	interger NOT NULL,
	`def`	interger NOT NULL,
	`disc`	text NOT NULL,
	`XP`	INTEGER NOT NULL,
	PRIMARY KEY(id)
);
INSERT INTO `character` VALUES (1,'IVXX',200,15,1,'1st character',1);
COMMIT;
