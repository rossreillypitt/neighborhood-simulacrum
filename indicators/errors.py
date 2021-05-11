from indicators.utils import ErrorLevel, ErrorResponse


class DataRetrievalError(Exception):
    """ Base class for errors that prevent data retrieval. """
    message: str
    level: ErrorLevel = ErrorLevel.ERROR

    def __init__(self, message, level=None):
        self.message = message
        if level: self.level = level

    @property
    def error_response(self):
        return ErrorResponse(level=self.level, message=self.message)


class AggregationError(DataRetrievalError):
    level = ErrorLevel.EMPTY


class MissingSourceError(DataRetrievalError):
    level = ErrorLevel.ERROR
