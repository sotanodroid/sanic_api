from datetime import datetime

from sanic.response import json
from sanic.views import HTTPMethodView

from app.tables import comment, post, section


class SectionView(HTTPMethodView):

    async def get(self, request, section_id=None):
        if section_id:
            query = section.select().where(section.c.id == section_id)
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

    async def post(self, request):
        """
        POST:
        {
            "theme": "New section",
            "description": "New description"
        }
        """
        query = section.insert()
        values = request.json.copy()
        values['date_created'] = str(datetime.now())
        values['date_modified'] = str(datetime.now())
        await request.app.db.execute(query=query, values=values)

        return json({'ok': 'Created'})

    async def put(self, request, section_id):
        query = section.update().where(section.c.id == section_id)
        values = request.json.copy()
        await request.app.db.execute(query=query, values=values)

        return json({'ok': f'updated section {section_id}'})

    async def delete(self, request, section_id):
        query = section.delete().where(section.c.id == section_id)
        await request.app.db.execute(query=query)

        return json({'ok': f'deleted section {section_id}'})


class PostView(HTTPMethodView):

    async def get(self, request, post_id=None):
        if post_id:
            query = post.select().where(post.c.id == post_id)
        else:
            query = post.select()
        rows = await request.app.db.fetch_all(query=query)

        return json({'posts': [
            {
                'theme': row['theme'],
                'description': row['description'],
                'date_created': row['date_created'],
                'date_modified': row['date_modified'],
                'text': row['text'],
                'comment_id': row['comment_id'],
            } for row in rows
        ]}) 

    async def post(self, request):
        query = post.insert()
        values = request.json.copy()
        values['date_created'] = str(datetime.now())
        values['date_modified'] = str(datetime.now())
        await request.app.db.execute(query=query, values=values)

        return json({'ok': 'Created'})

    async def put(self, request, post_id):
        query = post.update().where(post.c.id == post_id)
        values = request.json.copy()
        await request.app.db.execute(query=query, values=values)

        return json({'ok': f'updated post {post_id}'})

    async def delete(self, request, post_id):
        query = post.delete().where(post.c.id == post_id)
        await request.app.db.execute(query=query)

        return json({'ok': f'deleted post {post_id}'})


class CommentView(HTTPMethodView):

    async def get(self, request, comment_id=None):
        if comment_id:
            query = comment.select().where(comment.c.id == comment_id)
        else:
            query = comment.select()
        rows = await request.app.db.fetch_all(query=query)

        return json({'comments': [
            {
                'text': row['text'],
                'date_created': row['date_created'],
            } for row in rows
        ]}) 

    async def post(self, request):
        query = comment.insert()
        values = request.json.copy()
        values['date_created'] = str(datetime.now())
        await request.app.db.execute(query=query, values=values)

        return json({'ok': 'Created'})

    async def delete(self, request, comment_id):
        query = comment.delete().where(post.c.id == comment_id)
        await request.app.db.execute(query=query)

        return json({'ok': f'deleted post {comment_id}'})
