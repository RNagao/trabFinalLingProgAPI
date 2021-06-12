from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgres://ysefkhnhdyxsjl:f5560af554c1350621b22b26f75e05b922924457e1a42b8979b77d6589ce09f2@ec2-54-224-194-214.compute-1.amazonaws.com:5432/d3s9k15u6pqorm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False