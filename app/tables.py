import sqlalchemy

from datetime import datetime

metadata = sqlalchemy.MetaData()


comment = sqlalchemy.Table(
    'comments',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True, nullable=False),
    sqlalchemy.Column('text', sqlalchemy.Text()),
    sqlalchemy.Column('date_created', sqlalchemy.DateTime(), default=datetime.now()),
)


post = sqlalchemy.Table(
    'posts',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True, nullable=False),
    sqlalchemy.Column('theme', sqlalchemy.String(length=100)),
    sqlalchemy.Column('description', sqlalchemy.String(length=150)),
    sqlalchemy.Column('date_created', sqlalchemy.DateTime(), default=datetime.now()),
    sqlalchemy.Column('date_modified', sqlalchemy.DateTime(), default=datetime.now()),
    sqlalchemy.Column('text', sqlalchemy.Text()),
    sqlalchemy.Column('comment_id', sqlalchemy.Integer(), sqlalchemy.ForeignKey('comments.id'))
)


section = sqlalchemy.Table(
    'sections',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True, nullable=False),
    sqlalchemy.Column('theme', sqlalchemy.String(length=100)),
    sqlalchemy.Column('description', sqlalchemy.String(length=150)),
    sqlalchemy.Column('date_created', sqlalchemy.DateTime(), default=datetime.now()),
    sqlalchemy.Column('date_modified', sqlalchemy.DateTime(), default=datetime.now()),
    sqlalchemy.Column('post_id', sqlalchemy.Integer(), sqlalchemy.ForeignKey('posts.id'))
)


