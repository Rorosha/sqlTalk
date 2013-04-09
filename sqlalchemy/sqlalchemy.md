<!SLIDE bullets incremental transition=uncover>

# SQLAlchemy

  SQLAlchemy provides all the things you could want for dealing with a 
  database. 

  SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that 
  gives application developers the full power and flexibility of SQL.


<!SLIDE bullets incremental transition=uncover>

## SQLAlchemy Parts

* _Core_

  "The Core is itself a fully featured SQL abstraction toolkit, providing a smooth layer of abstraction over a wide variety of DBAPI implementations"

* _ORM_

  "The Object Relational Mapper is then an optional package which builds upon the Core"
 
<!SLIDE code monospace transition=wipe>

    @@@ python
      from sqlalchemy.ext.declarative 
        import declarative_base
      from sqlalchemy import Column, 
        Integer, String

      Base = declarative_base()

      class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)

