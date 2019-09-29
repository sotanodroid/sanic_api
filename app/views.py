from datetime import datetime

from sanic.response import json
from sanic.views import HTTPMethodView

from app.tables import comment, post, section


class SectionView(HTTPMethodView):

    async def get(self, request, section_id=None):
        if section_id:
            query = section.select().where(section.c.id==section_id)
        else:
            query = section.select()

        rows = await request.app.db.fetch_all(query=query)

        return json({'sections': [
            {
                'theme': row['theme'],
                'description': row['description'],
                'date_created': row['date_created'],
                'date_modified': row['date_modified'],
                'posts': row['post_id']
            } for row in rows
        ]}) 

    async def post(self, requset):
        """
        POST:
        {
            "theme": "New section",
            "description": "New description"
        }
        """
        query = section.insert()
        values = requset.json.copy()
        values['date_created'] = str(datetime.now())
        values['date_modified'] = str(datetime.now())

        await requset.app.db.execute(query=query, values=values)

        return json({'ok': 'Created'})

    async def put(self, request):
        pass

    async def delete(self, request, section_id):
        pass


class PostView(HTTPMethodView):

    async def get(self, request, post_id=None):
        query = post.select()
        rows = await request.app.db.fetch_all(query)

        return json(
            {'posts': [{row['theme']: row['description']} for row in rows]},
        )

    async def put(self, request):
        pass

    async def delete(self, request, post_id):
        pass


class CommentView(HTTPMethodView):

    async def get(self, request, comment_id=None):
        query = comment.select()
        rows = await request.app.db.fetch_all(query)

        return json(
            {'comments': [row['text'] for row in rows]},
        )

    async def put(self, request):
        pass

    async def delete(self, request, comment_id):
        pass
