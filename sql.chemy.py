from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, BOOLEAN, Date, Text, \
   SMALLINT, ForeignKey

engine = create_engine("mysql+pymysql://root:Rootpass12345@localhost/dbname", echo=True)
meta = MetaData()

users = Table(
   'users', meta,
   Column('id', Integer, primary_key=True),
   Column('username', String(50)),
   Column('password', String(255)),
   Column('is_active', BOOLEAN),
   Column('balance', BigInteger),
)

Session = Table(
   'session', meta,
   Column('id', String(50), primary_key=True),
   Column('user_id', Integer, ForeignKey('users.id')),
   Column('created_date', Date),
   Column('expired_date', Date),
   Column('data', Text),
   Column('ip', String(50)),
   Column('user_agent', String(50)),
)
Transaction = Table(
   'transaction', meta,
   Column('id', Integer, primary_key=True),
   Column('created_date', Date),
   Column('type_transaction', SMALLINT),
   Column('amount', BigInteger),
   Column('user_id', Integer, ForeignKey('users.id')),
)
meta.create_all(engine)
