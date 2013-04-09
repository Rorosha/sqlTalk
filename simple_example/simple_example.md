<!SLIDE code transition=toss>
.notes basicDB.py is the file they should be looking at.

# Extremely Simple Example

    @@@ python
      import sqlite3

      class DBInteraction:
      '''Super simple class for 
       dealing with databases.'''
        def create_table(self, table, col):
        def write(self, command):
        def read(self, command):
        def save(self, command):
