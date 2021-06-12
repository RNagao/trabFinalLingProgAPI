from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql://kjfrwnumsjmoag:7df4619e359664e94ef9ef2c87ee3965f7e8652beb670eda88371d2c50afb41c@ec2-52-4-111-46.compute-1.amazonaws.com:5432/dbrnn3p390ffq4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False