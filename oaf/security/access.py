class AccessControl:
    LEVELS = {"public", "internal", "confidential"}

    @staticmethod
    def validate(level):
        if level not in AccessControl.LEVELS:
            raise ValueError("Invalid access level")
