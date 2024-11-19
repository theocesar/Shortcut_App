import sqlite3

def connect():
    try:
        conn = sqlite3.connect("shortcuts.db")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


def create_table():
    try:
        sql = '''
                CREATE TABLE IF NOT EXISTS shortcuts (
                    name TEXT NOT NULL,
                    path TEXT NOT NULL
                )
            '''

        connection = connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        #print('Tabela criada com sucesso')

    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def delete(short_name): 
    try:
        sql = '''DELETE FROM shortcuts WHERE name = ?'''

        connection = connect()
        cursor = connection.cursor()  
        cursor.execute(sql, [short_name])
        connection.commit()
        #print("Registro removido com sucesso")

    except sqlite3.Error as e:
        print(f"Erro ao remover do banco de dados: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def insert(short_name, path_short): 
    try:
        sql = '''INSERT INTO shortcuts(name, path)
            VALUES (?, ?)'''

        connection = connect()
        cursor = connection.cursor()  # Corrigido
        cursor.execute(sql, [short_name, path_short])
        connection.commit()
        print("Inserção feita com sucesso")

    except sqlite3.Error as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def read_all():
    try:
        sql = '''SELECT * FROM shortcuts'''

        connection = connect()
        cursor = connection.cursor()
        cursor.execute(sql)

        # rows são todos os meus registros
        rows = cursor.fetchall()

        return rows

    except sqlite3.Error as e:
        print(f"Erro ao ler dados do banco de dados: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
