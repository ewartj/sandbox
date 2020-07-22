BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `test` (
	`Name`	TEXT,
	`Number`	NUMERIC,
	`Letter`	TEXT,
	PRIMARY KEY(`Name`)
);
INSERT INTO `test` VALUES ('Me',1100,'a');
INSERT INTO `test` VALUES ('cheese',5,'z');
COMMIT;
