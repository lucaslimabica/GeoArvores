import psycopg2

# Configurações da conexão
DB_CONFIG = {
    'dbname': 'a82451',          
    'user': 'a82451',       
    'password': 'a82451',     
    'host': '193.136.227.136',   
    'port': 8080                 
}

try:
    # Estabelecendo conexão com o banco de dados
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criação da tabela Tb_Tree
    create_table_query = """
    CREATE TABLE IF NOT EXISTS public."Tb_Tree" (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        especie VARCHAR(100) NOT NULL,
        altura FLOAT NOT NULL,
        longitude FLOAT NOT NULL,
        latitude FLOAT NOT NULL
    );
    """
    
    # Executando a query
    cursor.execute(create_table_query)
    conn.commit()  # Confirmar a transação

    print("Tabela 'Tb_Tree' criada com sucesso!")

except Exception as e:
    print("Erro ao criar a tabela:", e)

finally:
    # Fechar cursor e conexão
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")
