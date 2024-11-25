from models.registered import Register

def create_register(form, db):
    new_course = Register(
        name=form.name,
        phone_num=form.phone_num
    )
    db.add(new_course)
    db.commit()


def update(form, register_id, db):
    db.query(Register).filter(Register.id == register_id).update({
        Register.name: form.name,
        Register.phone_num: form.phone_num
    })
    db.commit()



def delete(db, register_id):
    db.query(Register).filter(Register.id == register_id).delete()
    db.commit()
