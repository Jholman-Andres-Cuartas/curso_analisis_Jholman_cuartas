class offer:
    def __init__(self, id, title, company, salary, workmode, exp_years):
        self.id = id
        self.title = title
        self.company = company
        self.salary = salary
        self. workmode = workmode
        self.exp_yearr = exp_years

    def __str__(self):
        return f"{self.id} {self.title}"
    

    