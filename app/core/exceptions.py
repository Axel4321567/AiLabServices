class AppException(Exception):
    """Base class for application-specific exceptions."""
    pass

class ValidationException(AppException):
    """Raised when input validation fails."""
    pass

class ProcessingException(AppException):
    """Raised when processing cannot be completed."""
    pass