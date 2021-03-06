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

-- Tags
CREATE TABLE "tags" (
  "id" SERIAL NOT NULL PRIMARY KEY,
  "name" VARCHAR(60) NOT NULL UNIQUE
);

-- Issues
CREATE TABLE "issues" (
  "id" SERIAL NOT NULL PRIMARY KEY,
  "author_user_id" INTEGER NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
  "name" VARCHAR(60) NOT NULL,
  "pub_date" TIMESTAMP WITH TIME ZONE NOT NULL
);

-- Many to Many
CREATE TABLE "tags_issues" (
  tag_id INTEGER REFERENCES "tags" (id) ON UPDATE CASCADE ON DELETE CASCADE,
  issues_id INTEGER REFERENCES "issues" (id) ON UPDATE CASCADE,
  CONSTRAINT tags_issues_pk PRIMARY KEY (tag_id, issues_id)
);

COMMIT;
