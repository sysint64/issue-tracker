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

-- Insert issues
INSERT INTO "issues" (author_user_id, name, pub_date, tags)
VALUES (1, 'План 1', now(), 'security,performance');

INSERT INTO "issues" (author_user_id, name, pub_date, tags)
VALUES (2, 'План 2', now(), 'documents');

INSERT INTO "issues" (author_user_id, name, pub_date, tags)
VALUES (2, 'План 3', now(), 'server');

COMMIT;
