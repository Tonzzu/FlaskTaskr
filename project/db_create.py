from views import db
from models import Task
from datetime import date

# crate the database and the table
db.create_all()

# insert data
#db.session.add(Task("Finish this tutorial", date(2019, 9, 22), 10, 1))
#db.session.add(Task("Finish Real Python", date(2119, 10, 3), 10, 1))

# commit changes
db.session.commit()
