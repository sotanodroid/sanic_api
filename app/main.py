from databases import Database
from environs import Env
from sanic import Sanic

from app.settings import Settings
from app.views import CommentView, PostView, SectionView

app = Sanic(__name__)


def setup_database():
    app.db = Database(app.config.DATABASE_URL)

    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()


def init():
    env = Env()
    env.read_env()

    app.config.from_object(Settings)

    setup_database()
    app.add_route(CommentView.as_view(), '/comments')
    app.add_route(CommentView.as_view(), '/comments/<comment_id:int>')
    app.add_route(PostView.as_view(), '/posts')
    app.add_route(PostView.as_view(), '/posts/<post_id:int>')
    app.add_route(SectionView.as_view(), '/sections')
    app.add_route(SectionView.as_view(), '/sections/<section_id:int>')

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
