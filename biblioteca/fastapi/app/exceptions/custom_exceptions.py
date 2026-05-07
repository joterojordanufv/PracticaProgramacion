class DuplicateEmailError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class BookNotAvailableError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class LoanNotFoundError(Exception):
    pass


class LoanAlreadyReturnedError(Exception):
    pass
