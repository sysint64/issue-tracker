import aiopg.sa
import sqlalchemy as sa

__all__ = ['question', 'choice']

meta = sa.MetaData()

question = sa.Table(
    "question", meta,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("text", sa.String(200), nullable=False),
    sa.Column("pub_date", sa.Date, nullable=False),

    # Indexes
    sa.PrimaryKeyConstraint("id", name="question_id_pkey")
)

choice = sa.Table(
    "choice", meta,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("question_id", sa.Integer, nullable=False),
    sa.Column("choice_text", sa.String(200), nullable=False),
    sa.Column("votes", sa.Integer, server_default="0", nullable=False),

    # Indexes
    sa.PrimaryKeyConstraint('id', name='choice_id_pkey'),
    sa.ForeignKeyConstraint(["question_id"], [question.c.id],
                            name="choice_question_id_fkey",
                            ondelete="CASCADE")
)


async def init_pg(app):
    c = app['config']['postgres']
    dsn = f"dbname={c['database']} user={c['user']} password={c['password']} host={c['host']}"

    app['db'] = await aiopg.create_pool(dsn)

    # engine = await aiopg.sa.create_engine(
    #     database=conf['database'],
    #     user=conf['user'],
    #     password=conf['password'],
    #     host=conf['host'],
    #     port=conf['port'],
    #     minsize=conf['minsize'],
    #     maxsize=conf['maxsize'],
    #     loop=app.loop
    # )
    # app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def get_question(conn, question_id):
    result = await conn.execute(
        question
            .select()
            .where(question.c.id == question_id)
    )

    question_record = await result.first()

    if not question_record:
        msg = "Question with id: {} does not exists"
        raise RecordNotFound(msg.format(question_id))

    result = await conn.execute(
        choice
            .select()
            .where(choice.c.question_id == question_id)
            .order_by(choice.c.id)
    )

    choice_records = await result.fetchall()
    return question_record, choice_records
