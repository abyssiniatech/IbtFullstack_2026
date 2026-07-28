class BankConfig:
    """
    Singleton Pattern

    Only one BankConfig object
    exists throughout the application.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            # Global bank settings
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance