from setuptools import setup


setup(
    name="flaskex",
    extras_require={
        "app": ["Flask", "WTForms", "SQLAlchemy", "bcrypt", "requests", "flask-heroku", "gunicorn"],
        "linter": ["flake8"],
        "test": ["pytest", "Faker"],
    },
)
