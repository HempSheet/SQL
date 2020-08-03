from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger,\
   BOOLEAN, TIME, Text, SMALLINT, ForeignKey

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
   Column('created_date', TIME),
   Column('expired_date', TIME),
   Column('data', Text),
   Column('ip', String(50)),
   Column('user_agent', String(50)),
)
Transaction = Table(
   'transaction', meta,
   Column('id', Integer, primary_key=True),
   Column('created_date', TIME),
   Column('type_transaction', SMALLINT),
   Column('amount', BigInteger),
   Column('user_id', Integer, ForeignKey('users.id')),
)
meta.create_all(engine)

ins = users.insert()
ins = users.insert().values(username='Ron', password='12345', balance=222)
conn = engine.connect()
result = conn.execute(ins)

ins = Session.insert()
ins = Session.insert().values(id=1, user_id=1, created_date='22:07:20',
                              expired_date='23:07:20', data='today',
                              ip='22.22.222.222', user_agent='1')

ins = Transaction.insert()
ins = Transaction.insert().values(id='2', created_date='22:07:20', type_transaction='2',
                                  amount=222, user_id=1)
conn = engine.connect()
result = conn.execute(ins)
