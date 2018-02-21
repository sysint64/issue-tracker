from issue_tracker.db_repository import PostgresqlRepository


async def items(async_generator):
    return [item async for item in async_generator]


class Repository(PostgresqlRepository):
    async def fetch_tags(self):
        await self.cursor.execute("SELECT name FROM tags")

        async for row in self.cursor:
            yield row[0]

    async def fetch_issues(self):
        await self.cursor.execute("""
            SELECT
              issues.id AS id,
              issues.name AS name,
              issues.pub_date AS pub_date,
              users.id AS author_id,
              concat_ws(' ', users.first_name, users.last_name) AS author_name,
              array_to_string(array_agg(tags.name), ',') AS tags
            FROM issues
              INNER JOIN tags_issues ON issues.id = tags_issues.issues_id
              INNER JOIN tags ON tags_issues.tag_id = tags.id
              INNER JOIN users ON issues.author_user_id = users.id
            GROUP BY issues.id, users.id
            ORDER BY issues.pub_date DESC
        """)

        issues_id, name_id, pub_date_id, author_id, author_name, tags = 0, 1, 2, 3, 4, 5

        async for row in self.cursor:
            yield {
                "id": row[issues_id],
                "name": row[name_id],
                "status": "ok",
                "datetime": row[pub_date_id],
                "author": {
                    "id": row[author_id],
                    "name": row[author_name],
                },
                "tags": row[tags].split(",")
            }
