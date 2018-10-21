from user.src.model import User


class TestController(object):
    def test_list_users(self, client):
        user = {'id': 1, 'name': 'Willian Frantz'}
        User(name='Willian Frantz').save()

        response = client.get('/users/')

        assert response.status_code == 200
        assert response.json == [user]