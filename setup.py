from setuptools import setup, find_packages

setup(
    name="flask-salad-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "Flask-RESTful==0.3.10",
        "Flask-SQLAlchemy==3.0.5",
        "psycopg2-binary==2.9.7",
        "python-dotenv==1.0.0",
        "gunicorn==21.2.0",
        "mysqlclient==2.2.0",
    ],
)