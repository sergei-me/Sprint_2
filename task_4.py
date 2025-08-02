class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        if rest_days is not None:
            return cls(name, (7 - rest_days) * 8, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        return cls(name, hours, rest_days, f"{name}@email.com")
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
    
    def salary(self):
        hours = self.get_hours()
        if hours is not None:
            return hours * self.hourly_payment
        else:
            return 0