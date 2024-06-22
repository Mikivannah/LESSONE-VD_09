from app import app, db
from app.models import User

with app.app.context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
