from flaskblog import app, db
from flaskblog.models import User, Post


@app.shell_contect_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
