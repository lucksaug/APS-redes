from projeto import db, login_manager


@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(user_id))
