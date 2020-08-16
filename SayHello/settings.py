import os
from app import app

'''配置文件'''


def Key():
    import uuid, random
    key = ''.join(random.sample(''.join(str(uuid.uuid4()).split('-')) + str(hash(uuid.uuid4())), 32))
    return key


SECRET_KEY = Key()
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

