SET ROLE issue_tracker;

BEGIN;

DROP TABLE "tags_issues";
DROP TABLE "tags";
DROP TABLE "issues";
DROP TABLE "users";
DROP TABLE "groups";

COMMIT;
