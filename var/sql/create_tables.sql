SET ROLE issue_tracker;

BEGIN;

-- Group
CREATE TABLE "groups" (
  "id" SERIAL NOT NULL PRIMARY KEY,
  "name" VARCHAR(200) NOT NULL UNIQUE,
  "parent_group_id" INTEGER REFERENCES "groups" ("id") ON DELETE SET NULL
);

-- User
CREATE TABLE "users" (
  "id" SERIAL NOT NULL PRIMARY KEY,
  "email" VARCHAR(200) NOT NULL UNIQUE,
  "passwd" VARCHAR(400) NOT NULL,
  "group_id" INTEGER REFERENCES "groups" ("id") ON DELETE SET NULL,
  "first_name" VARCHAR(60),
  "last_name" VARCHAR(60)
);

-- Issues
CREATE TABLE "issues" (
  "id" SERIAL NOT NULL PRIMARY KEY,
  "author_user_id" INTEGER NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
  "name" VARCHAR(60) NOT NULL,
  "pub_date" TIMESTAMP WITH TIME ZONE NOT NULL,
  "tags" VARCHAR(400) NOT NULL
);

COMMIT;
