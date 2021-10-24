from .models import db

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()
    return instance.id

def get_by_args(model, id):
    return model.query.filter_by(id=id).all()

def commit_changes():
    db.session.commit()