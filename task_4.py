class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours == None and self.rest_days is not None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours
    
    def get_email(self):
        if self.email == None:
            self.email = f"{self.name}@email.com"
        return self.email
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
    
    def salary(self):
        hours = self.get_hours()
        if hours is not None:
            return hours * self.hourly_payment
        else:
            return 0