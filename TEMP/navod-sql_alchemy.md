Here's how you can achieve the same tasks using `flask_sqlalchemy`:

1. **Install `flask_sqlalchemy`**:
   If you haven't already, you need to install `flask_sqlalchemy`. You can do this using pip:
   ```sh
   pip install flask_sqlalchemy
   ```

2. **Set Up the Flask Application with SQLAlchemy**:
   Here's a complete example:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Step 1: Create a Flask application
app = Flask(__name__)

# Step 2: Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Step 3: Create an SQLAlchemy instance
db = SQLAlchemy(app)

# Step 4: Define the User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Step 5: Create the database and table
with app.app_context():
    db.create_all()

# Step 6: Create a Flask route to add data
@app.route('/add')
def add_users():
    with app.app_context():
        new_user1 = User(name='Alice', age=30)
        new_user2 = User(name='Bob', age=25)

        db.session.add(new_user1)
        db.session.add(new_user2)
        db.session.commit()

        return 'Users added successfully!'

# Step 7: Create a Flask route to query and display data
@app.route('/users')
def get_users():
    with app.app_context():
        users = User.query.all()
        result = ''
        for user in users:
            result += f'ID: {user.id}, Name: {user.name}, Age: {user.age}<br>'
        return result

# Step 8: Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

1. **Create a Flask Application**:
   ```python
   app = Flask(__name__)
   ```
   This line creates a Flask application instance.

2. **Configure the Database URI**:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   ```
   These lines configure the database URI and disable modification tracking.

3. **Create an SQLAlchemy Instance**:
   ```python
   db = SQLAlchemy(app)
   ```
   This line creates an SQLAlchemy instance bound to the Flask application.

4. **Define the User Model**:
   ```python
   class User(db.Model):
       __tablename__ = 'users'
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String, nullable=False)
       age = db.Column(db.Integer, nullable=False)
   ```
   This defines the `User` model, which maps to the `users` table in the database.

5. **Create the Database and Table**:
   ```python
   with app.app_context():
       db.create_all()
   ```
   This line creates the `users` table in the database.

6. **Create a Flask Route to Add Data**:
   ```python
   @app.route('/add')
   def add_users():
       with app.app_context():
           new_user1 = User(name='Alice', age=30)
           new_user2 = User(name='Bob', age=25)

           db.session.add(new_user1)
           db.session.add(new_user2)
           db.session.commit()

           return 'Users added successfully!'
   ```
   This defines a route `/add` that adds two users to the database when accessed.

7. **Create a Flask Route to Query and Display Data**:
   ```python
   @app.route('/users')
   def get_users():
       with app.app_context():
           users = User.query.all()
           result = ''
           for user in users:
               result += f'ID: {user.id}, Name: {user.name}, Age: {user.age}<br>'
           return result
   ```
   This defines a route `/users` that queries all users from the database and displays them.

8. **Run the Flask Application**:
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```
   This runs the Flask application in debug mode.

### Running the Application:

1. **Add Users**:
   Open your web browser and navigate to `http://127.0.0.1:5000/add`. This will add the users to the database.

2. **View Users**:
   Open your web browser and navigate to `http://127.0.0.1:5000/users`. This will display the list of users from the database.

Using `flask_sqlalchemy` simplifies the integration of SQLAlchemy with Flask, providing convenient methods and configurations tailored for Flask applications.
