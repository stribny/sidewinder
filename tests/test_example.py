from appname.core.models import User


def test_create_user_username(db):
    user = User.objects.create_user("Mark")
    assert user.username == "Mark"
