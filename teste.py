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
    INSERT INTO public."Tb_Tree" (nome,especie,altura,longitude,latitude) VALUES ("Pinheiro", "Pinheiro");
    """
    
    # Executando a query
    cursor.execute(create_table_query)
    conn.commit()  # Confirmar a transação

    print("Insert na Tb_Tree feito!")

except Exception as e:
    print("Erro ao criar a tabela:", e)

finally:
    # Fechar cursor e conexão
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")
