from environs import Env
from sanic import Sanic
from app.routes import setup_routes
from databases import Database
from environs import Env
from app.settings import Settings

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
    setup_routes(app)

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
