class ModelIO:
    @classmethod
    def to_json(cls, plan):
        raise NotImplementedError()

    @classmethod
    def validate(cls, data):
        raise NotImplementedError()
