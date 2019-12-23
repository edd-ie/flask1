class Development():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secret@127.0.0.1:5432/sales_demo'
    SECRET_KEY = '80445a717e76a537ef9722986ac2a074'
    DEBUG = True


class Production():
    SQLALCHEMY_DATABASE_URI = 'postgres://rycipishxbaqec:9f93edfd69965d870ff65bcf0170ed1f0c3c985b426c3db9683d9b2ca2ffbf9a@ec2-54-247-177-254.eu-west-1.compute.amazonaws.com:5432/d4ojr2pqhiarvt'
    SECRET_KEY = '80445a717e76a537ef9722986ac2a074'
    DEBUG = False
