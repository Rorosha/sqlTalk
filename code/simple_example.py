import sqlite3

class DBInteraction:
    '''Super simple class for dealing with databases.'''
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()
        
    def create_table(self, table_name, column_names):
        '''Creates a table. 'table_name' is a simple string used to name 
	the table. 'column_names' is a list of tuples [(column_name,
	type), (column_name, type)...] for the columns.
   
            columns = [(name, text), (email, text)]
            myDB.create_table('contacts', columns)
            --> CREATE TABLE contacts (name text, email text);'''
        
        # Create the correct string for input
        column_string = ''
        for tup in column_names:
            column_string += tup[0] + ' '
            column_string += tup[1] + ', '
        
        # Have to strip the trailing ', '
        column_string = column_string[:-2]
        
        
        # Don't do this is production code - I'm being lazy here, huge
	# security issue. This is just to show the basic ideas.
        
        self.cursor.execute('''CREATE TABLE %s (%s)''' % (table_name, column_string))
        self.db.commit()
        
    def write(self, command):
        '''Provides cursor access for executing statements on the
	database. 'command' needs to be a valid SQL statement.'''
        self.cursor.execute(command)
        
    def read(self, table, column, value):
        '''Allows user to run SELECT statements against the database.'''
        return self.cursor.execute("""SELECT * from %s WHERE %s = '%s'""" % (table, column, value)).fetchone()
        
    def save(self):
        '''Commits writes to the database.'''
        self.db.commit()
        
    def cursor_close(self):
        '''Closes the cursor.'''
        self.cursor.close()
        
    def cursor_open(self):
        '''Opens the cursor.'''
        self.cursor = self.db.cursor()

if __name__ =='__main__':

  print "Create the db by instantiating a new DBInteraction() object"

  myDB = DBInteraction('test2.db')

  print "Create the tables in the database..."

  myDB.create_table('people', [('name', 'text'), ('location', 'text'), ('age', 'int')])

  print "Insert some stuff into the database..."

  myDB.write("""INSERT INTO people VALUES ('mike', 'michigan', '34')""")
  myDB.write("""INSERT INTO people VALUES ('john', 'ohio', '51')""")

  print "Save things in the db..."

  myDB.save()
