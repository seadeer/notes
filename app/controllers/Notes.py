"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')
       
    def index(self):
        notes = self.models['Note'].get_all()
        print notes
        return self.load_view('index.html', notes=notes)

    def index_json(self):
        notes=self.models['Note'].get_all()
        return jsonify(notes=notes)

    def index_html(self):
        notes = self.models['Note'].get_all()
        return self.load_view('index.html', notes=notes)

    def ajax_showform(self, id):    
        notes=self.models['Note'].get_all()
        for i in notes:
            if i['id'] == int(id):
                note = i
        return self.load_view('/partials/form.html', note=note)

    def create(self):
        info = {
            'title': request.form['title'],
        }
        self.models['Note'].add_note(info)
        return redirect('/')

    def update(self, id):
        info = {
            'content': request.form['content']
        }
        self.models['Note'].upd_note(info, id)
        note = info
        print ("%")*50, "Updating note content"
        return self.load_view('/partials/notes.html', note=note)

    def destroy(self, id):
        self.models['Note'].destroy(id)
        return redirect('/')




