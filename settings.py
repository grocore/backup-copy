class Config(object):
    TESTING = False

class DevelopmentConfig(Config):
    SOURCE_FOLDER = r'\\ua-test01\backup'
    BACKUP_FOLDER = r'\\ua-hv01\Backups\ua-db01'
    BACKUP_FILENAME = r'db-top-1_backup*.bak'

class ProductionConfig(Config):
    SOURCE_FOLDER = r'\\ua-db01\d$\Microsoft SQL Server\Backup'
    BACKUP_FOLDER = r'\\UA-fs01\Backups\UA-DB01'
    BACKUP_FILENAME = r'db-top-1_backup*.bak'

class TestingConfig(Config):
    TESTING = True
