import asyncio


class PostgresqlRepository:
    def __init__(self, app):
        self.app = app
        self.conn_context = self.app['db'].acquire()

    @asyncio.coroutine
    async def __aenter__(self):
        self.conn = await self.conn_context.__aenter__()
        self.cursor_context = self.conn.cursor()
        self.cursor = await self.cursor_context.__aenter__()
        return self

    @asyncio.coroutine
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cursor_context.__aexit__(exc_type, exc_val, exc_tb)
        await self.conn_context.__aexit__(exc_type, exc_val, exc_tb)
