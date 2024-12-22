from .models import session, Klasa

class KlasaCRUD:
    @staticmethod
    def create(name, x, y):
        """Create new record"""
        new_record = Klasa(name=name, x=x, y=y)
        try:
            session.add(new_record)
            session.commit()
            return new_record
        except Exception as e:
            session.rollback()
            raise e

    @staticmethod
    def read_all():
        """Read all records"""
        return session.query(Klasa).all()

    @staticmethod
    def read_by_id(record_id):
        """Read record by ID"""
        record = session.query(Klasa).filter_by(id=record_id).first()
        if not record:
            return None  # Można rzucić wyjątek lub zwrócić None
        return record

    @staticmethod
    def update(record_id, name=None, x=None, y=None):
        """Updating record"""
        record = session.query(Klasa).filter_by(id=record_id).first()

        if record:
            if name is not None:
                record.name = name
            if x is not None:
                record.x = x
            if y is not None:
                record.y = y
            try:
                session.commit()
                return record
            except Exception as e:
                session.rollback()
                raise e
        else:
            return None

    @staticmethod
    def delete(record_id):
        """Deleting record by ID"""
        record = session.query(Klasa).filter_by(id=record_id).first()
        if record:
            try:
                session.delete(record)
                session.commit()
                return record
            except Exception as e:
                session.rollback()
                raise e
        else:
            return None
