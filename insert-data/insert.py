from faker import Faker
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",       
    database="clientes"  
)

cursor = conn.cursor()

fake = Faker()

#qts de vezes q vai rodar
quantidade = 10

for _ in range(quantidade):
    nome = fake.name()  
    sql = "INSERT INTO nomes (nome) VALUES (%s)"  
    cursor.execute(sql, (nome,))


conn.commit()

print(f"{quantidade} nomes inseridos com sucesso!")


cursor.close()
conn.close()
