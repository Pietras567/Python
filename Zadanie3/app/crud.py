from .models import session, WineData

class KlasaCRUD:
    @staticmethod
    def create(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality):
        """Create new record"""
        new_record = WineData(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid, residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, quality=quality)
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
        return session.query(WineData).all()

    @staticmethod
    def read_by_id(record_id):
        """Read record by ID"""
        record = session.query(WineData).filter_by(id=record_id).first()
        if not record:
            return None
        return record

    @staticmethod
    def update(record_id, fixed_acidity=None, volatile_acidity=None, citric_acid=None, residual_sugar=None, chlorides=None, free_sulfur_dioxide=None, total_sulfur_dioxide=None, density=None, pH=None, sulphates=None, alcohol=None, quality=None):
        """Updating record"""
        record = session.query(WineData).filter_by(id=record_id).first()

        if record:
            if fixed_acidity is not None:
                record.fixed_acidity = fixed_acidity
            if volatile_acidity is not None:
                record.volatile_acidity = volatile_acidity
            if citric_acid is not None:
                record.citric_acid = citric_acid
            if residual_sugar is not None:
                record.residual_sugar = residual_sugar
            if chlorides is not None:
                record.chlorides = chlorides
            if free_sulfur_dioxide is not None:
                record.free_sulfur_dioxide = free_sulfur_dioxide
            if total_sulfur_dioxide is not None:
                record.total_sulfur_dioxide = total_sulfur_dioxide
            if density is not None:
                record.density = density
            if pH is not None:
                record.pH = pH
            if sulphates is not None:
                record.sulphates = sulphates
            if alcohol is not None:
                record.alcohol = alcohol
            if quality is not None:
                record.quality = quality
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
        record = session.query(WineData).filter_by(id=record_id).first()
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
