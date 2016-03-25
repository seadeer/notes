""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all(self):
        query = "SELECT * FROM notes"
        return self.db.query_db(query)
    
    def add_note(self, info):
        query = "INSERT into notes (title, created_at, updated_at) VALUES('{}', NOW(), NOW())".format(info['title'])
        print ("!")*50, query
        self.db.query_db(query)

    def upd_note(self, info, id):
        data = [info['content'], id]
        query = "UPDATE notes SET content=%s, updated_at=NOW() WHERE id=%s"
        self.db.query_db(query, data)

    def destroy(self, id):
        data = [id]
        query = "DELETE FROM notes WHERE id=%s"
        self.db.query_db(query, data)