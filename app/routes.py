from sanic.response import json

from app.tables import comment, post, section

"""
Возможно переписать на Вьюху
"""

def setup_routes(app):

    @app.route('/sections')
    async def sections_list(request):
        """
        нужно уметь создавать/редактировать/удалять раздел
        должен быть функциональность листинга с пагинацией
        """
        query = section.select()
        rows = await request.app.db.fetch_all(query)

        return json(
            {'sections': [{row['theme']: row['description']} for row in rows]},
        )

    @app.route('/posts')
    async def posts_list(request):
        """
        В разделе нужно создавать/редактировать/удалять посты
        должен быть функциональность листинга с пагинацией
        при возвращении конкретного поста, возвращаются все комментарии
        """
        query = post.select()
        rows = await request.app.db.fetch_all(query)

        return json(
            {'posts': [{row['theme']: row['description']} for row in rows]},
        )

    @app.route('/comments')
    async def comments_list(request):
        """
        на каждый комментарий можно оставить комментарий, вложенность не ограничена
        должна быть возможность поиска по названию разделов и постов
        """
        query = comment.select()
        rows = await request.app.db.fetch_all(query)

        return json(
            {'comments': [row['text'] for row in rows]},
        )
