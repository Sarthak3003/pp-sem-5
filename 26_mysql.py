import mysql.connector;

mydb  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pass@123',
    database = 'comder'
);

if mydb:
    print('Succesfully connected to MySQL')

currentObj = mydb.cursor()

# createQuery = f'create table student (rollno int, name varchar(255), city varchar(255), division char(255))'
# currentObj.execute(createQuery)

print('1. Create Table \n2. Display Table \n3. Insert Data \n4. Update Data \n5. Delete Data \n6. Search Data');
choice = int(input('Your Choice: '))

if choice == 1:
    print('Table created')
elif choice == 2:
    tableName = str(input('Enter table name: '))
    query = f'SELECT * FROM {tableName}'
    currentObj.execute(query)
    print(currentObj.fetchall())
elif choice == 3:
    tableName = str(input('Enter table name: '))
    rollno = int(input('Enter roll no: '));
    name = str(input('Enter name: '));
    city = str(input('Enter city: '));
    division = str(input('Enter division: '))
    query = f'INSERT INTO {tableName} (rollno, name, city, division) VALUES (%s, %s, %s, %s)'
    val = (rollno, name, city, division);
    currentObj.execute(query, val);
    mydb.commit();
    print('Record Inserted');
elif choice == 4:
    table = str(input('Enter table name to update in: '));
    rollno = str(input('Enter roll no of record to update: '));
    name = str(input('Enter name: '));
    city = str(input('Enter city: '));
    division = str(input('Enter division: '));
    query = f"UPDATE {table} SET name = '{name}', city = '{city}', division = '{division}' WHERE rollno = {rollno}"
    currentObj.execute(query);
    mydb.commit();
    print('Record Updated');
elif choice == 5:
    table = str(input('Enter table name to delete from: '));
    rollno = str(input('Enter roll no of record to delete: '));
    query = f"DELETE FROM {table} WHERE rollno = {rollno}";
    currentObj.execute(query);
    mydb.commit();
    print('Record Deleted');
elif choice == 6:
    table = str(input('Enter table name to search: '));
    rollno = str(input('Enter roll no of record to search: '));
    query = f'SELECT * FROM {table} WHERE rollno = {rollno}'
    currentObj.execute(query);
    print(currentObj.fetchall())