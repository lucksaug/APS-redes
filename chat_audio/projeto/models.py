from projeto import db, login_manager
from projeto import db


@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(user_id))

def funcao():
    cur =db.connection.cursor()
    cur.execute('''
        INSERT INTO cadastro ('email', 'senha') VALUES ('lucas@gmail.com', '123'), ('gabriel@gmail.com', '123'),
    ('gustavo@gmail.com', '123');

    INSERT INTO gravando ('id_audio', 'gravador') VALUES (1, 'teste de gravação'), (2, 'teste de gravação 2'),
    (3, 'teste de gravação 3');
        
        ''')