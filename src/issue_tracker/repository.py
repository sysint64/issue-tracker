from issue_tracker.db_repository import PostgresqlRepository


async def items(async_generator):
    return [item async for item in async_generator]


class Repository(PostgresqlRepository):
    async def fetch_issues(self):
        await self.cursor.execute("SELECT id, name, pub_date FROM issues")

        async for row in self.cursor:
            yield {
                "id": row[0],
                "name": row[1],
                "status": "ok",
                "datetime": row[2],
                "author": {
                    "name": "Andrey Kabylin",
                },
                "tags": [
                    "security",
                    "performance"
                ]
            }
