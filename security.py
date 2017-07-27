from werkzeug.security import safe_str_cmp
from models.user import UserModel

# given a username, see if it is in the database or return None
# if user is not None and the user PW and the provided PW match, return User
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# return the user ID of the payload dict which was passed
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
