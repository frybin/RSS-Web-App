from app import app, db
from app.models import Feed

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Feed': Feed}

if __name__ == '__main__':
    app.run()