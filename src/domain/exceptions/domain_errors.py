# domain_errors.py


class PatientNotFoundError(LookupError):
    pass


class DuplicatePatientIdError(RuntimeError):
    pass

