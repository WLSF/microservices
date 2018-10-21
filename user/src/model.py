from user.src.main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return 'User {}'.format(self.name)


class UserSerializer(object):
    def __init__(self, data):
        if isinstance(data, User):
            self.data = {'id': data.id, 'name': data.name}
        else:
            self.users = [user.__dict__ for user in data]
            [user.pop('_sa_instance_state') for user in self.users]
            self.data = self.users
