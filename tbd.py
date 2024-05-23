import psycopg2 
import json
conn = psycopg2.connect(dbname='product', user='postgres', password='postgres', host='localhost' , port='5432')

curcor = conn.cursor()

fi = open('MOCK_DATA (1).json' , 'r')
d = json.load(fi)
for i in range(1234567890123456789009876543)
    for i in d:
        print(i)
        add = f"INSERT INTO PRODUCTS (name, price, category) VALUES ('{i.get('name')}', {i.get('price')}, '{i.get('category')}')"
        curcor.execute(add) 
        
        
        conn.commit()
fi.close()