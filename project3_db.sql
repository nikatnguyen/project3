CREATE TABLE "tax_rate_df" (
	"Country" VARCHAR NOT NULL PRIMARY KEY,
	"Life Expectancy" FLOAT NOT NULL,
	"Total Tax Rate (%)" FLOAT NOT NULL
);

CREATE TABLE "ForestedAreas"(
	"Country" VARCHAR NOT NULL PRIMARY KEY,
	"Forested Area (%)" FLOAT NOT NULL,
	"Life Expectancy (years)" FLOAT NOT NULL
);

CREATE TABLE "OutOfPocket" (
	"Country" VARCHAR NOT NULL PRIMARY KEY,
	"Life expectancy" FLOAT NOT NULL,
	"Out of pocket health expenditure" FLOAT NOT NULL
);

SELECT *
FROM "ForestedAreas";

SELECT *
FROM "OutOfPocket";

SELECT *
FROM "tax_rate_df";
