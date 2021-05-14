from projeto import db#, login_manager


#@login_manager.user_loader
#def load_user(id_usuario):
#    return User.query.get(int(user_id))

def inserir_usuario(email,senha):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO usuario(email,senha) VALUES (%s,%s)",(email,senha))
    db.connection.commit()
    cur.close()

#def inserir_conversa(gravacao):
#   cur = db.connector.cursor()
#    cur.execute("INSERT INTO usuario(email,senha) VALUES (%s,%s)",(email,senha))
#    db.connection.commit()
#    cur.close()
#   INSERT INTO gravando ('id_audio', 'gravador') VALUES (1, 'teste de gravação'), (2, 'teste de gravação 2'),
#   (3, 'teste de gravação 3');  
# ''')