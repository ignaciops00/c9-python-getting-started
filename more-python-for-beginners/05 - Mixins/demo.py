class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'
        

def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()

class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging'
        
        

sql_connection = SqlDatabase()
jutlog = JustLog()
framework(sql_connection)

framework(jutlog)
