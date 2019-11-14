# sanic_api

            Sanic
    Build Fast. Run Fast.

## Инструкции

#### Установить зависиомти в виртуальное окружение  Pipenv

`pipenv install -e .`

#### Миграция

Миграция с использованием alembic

`alembic upgrade head`

#### Запуск приложения

`python -m app`

## Интерфейсы приложения

Проект реализует три модели: comments, posts и sections.

### Sections [GET, POST, PUT, DELETE]

**POST** `http://localhost:8000/sections`

```json
{
    "theme": "New section",
    "description": "New description"
}
```

Response

```json
{
	"ok":"Created"
}
```

**GET**`http://localhost:8000/sections`

Response

```json
{
    "sections": [
        {
            "theme": "New section",
            "description": "New description",
            "date_created": null,
            "date_modified": null,
            "posts": null
        },
        {
            "theme": "New section",
            "description": "New description",
            "date_created": 1569768194,
            "date_modified": 1569768194,
            "posts": null
        },
        {
            "theme": "New section",
            "description": "New description",
            "date_created": 1573775106,
            "date_modified": 1573775106,
            "posts": null
        }
    ]
}
```

**GET** `http://localhost:8000/sections/{id}`

Response

```json
{
    "sections": [
        {
            "theme": "New section",
            "description": "New description",
            "date_created": null,
            "date_modified": null,
            "posts": null
        }
    ]
}
```

**PUT** `http://localhost:8000/sections/{id}`

```
{
    "theme": "Tottaly section"
}
```

Response

```
{
    "ok": "updated section 1"
}
```

**DELETE** `http://localhost:8000/sections/{id}`

Response

```
{
    "ok": "deleted section 1"
}
```



### Posts [GET, POST, PUT, DELETE]

**POST** `http://localhost:8000/posts`

```json
{
    "theme": "New section",
    "description": "New description",
    "text": "Awesome post"
}
```

Response

```json
{
	"ok":"Created"
}
```

**GET**`http://localhost:8000/posts`

Response

```json
{
    "posts": [
        {
            "theme": "Tottaly section",
            "description": null,
            "date_created": 1573775498,
            "date_modified": 1573775498,
            "text": null,
            "comment_id": null
        }
    ]
}
```

**GET** `http://localhost:8000/posts/{id}`

Response

```json
{
    "posts": [
        {
            "theme": "Tottaly section",
            "description": null,
            "date_created": 1573775498,
            "date_modified": 1573775498,
            "text": null,
            "comment_id": null
        }
    ]
}
```

**PUT** `http://localhost:8000/posts/{id}`

```
{
    "theme": "Tottaly post"
}
```

Response

```
{
    "ok": "updated post 1"
}
```

**DELETE** `http://localhost:8000/posts/{id}`

Response

```
{
    "ok": "deleted post 1"
}
```


### Comments [GET, POST, PUT]

**POST** `http://localhost:8000/comments`

```json
{
    "text": "Awesome text"
}
```

Response

```json
{
	"ok":"Created"
}
```

**GET**`http://localhost:8000/comments`

Response

```json
{
    "comments": [
        {
            "text": "Awesome text",
            "date_created": 1573775706
        }
    ]
}
```

**GET** `http://localhost:8000/comments/{id}`

Response

```json
{
    "comments": [
        {
            "text": "Awesome text",
            "date_created": 1573775706
        }
    ]
}
```

**DELETE** `http://localhost:8000/posts/{id}`

Response

```
{
    "ok": "deleted post 1"
}
```
