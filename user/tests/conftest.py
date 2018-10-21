import os
import pytest
import tempfile
from user.src.main import app, db

@pytest.fixture
def client():
    db_fd, database = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(database)
    app.config['TESTING'] = True

    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(database)
