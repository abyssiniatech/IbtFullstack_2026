class BankConfig:
    """
    Singleton Pattern

    Only one configuration object
    exists in the whole application.

    Stores:
    - Interest rate
    - Overdraft limit
    """


    _instance = None



    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)


            # Default bank settings

            cls._instance.interest_rate = 0.05

            cls._instance.overdraft_limit = 1000



        return cls._instance