SET ROLE issue_tracker;

BEGIN;

INSERT INTO "groups" (name) VALUES ('super admin');
INSERT INTO "groups" (name, parent_group_id) VALUES ('admin', 2);
INSERT INTO "groups" (name, parent_group_id) VALUES ('user', 3);

INSERT INTO "users" ("email", "passwd", "group_id", "first_name", "last_name")
VALUES ('andrey@kabylin.ru', crypt('123321', gen_salt('bf', 8)), 1, 'Andrey', 'Kabylin');

INSERT INTO "users" ("email", "passwd", "group_id", "first_name", "last_name")
VALUES ('swstr_master@rambler.ru', crypt('qwerty', gen_salt('bf', 8)), 1, 'Yara', 'Stafievskaya');

SELECT * FROM users WHERE email = 'andrey@kabylin.ru' AND passwd = crypt('123321', passwd);

-- Insert tags
INSERT INTO "tags" (name) VALUES ('security');
INSERT INTO "tags" (name) VALUES ('performance');
INSERT INTO "tags" (name) VALUES ('documents');
INSERT INTO "tags" (name) VALUES ('server');
INSERT INTO "tags" (name) VALUES ('cryptography');

-- Insert issues
INSERT INTO "issues" (author_user_id, name, pub_date)
VALUES (1, 'План 1', now());

INSERT INTO "issues" (author_user_id, name, pub_date)
VALUES (2, 'План 2', now());

INSERT INTO "issues" (author_user_id, name, pub_date)
VALUES (2, 'План 3', now());

-- Relations
INSERT INTO "tags_issues" (tag_id, issues_id) VALUES (1, 1);
INSERT INTO "tags_issues" (tag_id, issues_id) VALUES (2, 1);
INSERT INTO "tags_issues" (tag_id, issues_id) VALUES (3, 2);
INSERT INTO "tags_issues" (tag_id, issues_id) VALUES (4, 3);

COMMIT;
