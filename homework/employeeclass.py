class employee:


    def work(self, name, type_of_work):
        self.emp_name = name
        self.emp_wage = 0.00
        self.emp_type_of_work = type_of_work

        print(self.emp_name, "is working as a ", self.emp_type_of_work)

    def attendance(self, name, no_of_days_work, no_of_days_work_for_1month):
        self.emp_no_of_days_work = no_of_days_work
        self.total_no_of_days = no_of_days_work_for_1month
        print(self.emp_name,"is worked for",self.emp_no_of_days_work,"out of" ,self.total_no_of_days)

    def wages(self, name, no_of_days_work, no_of_days_work_for_1month,pay):
        days = float(input("no of days worked"))
        days = float(days)
        hours = float(input("no of hours worked"))
        hours = float(hours)
        rate = float(input("enter pay rate"))
        rate = float(rate)
        pay = days * hours * rate
        self.emp_no_of_days_work = no_of_days_work
        self.total_no_of_days = no_of_days_work_for_1month
        self.emp_salary = pay
        print(self.emp_name,"is worked for",self.emp_no_of_days_work,"out of ",self.total_no_of_days,"salary is " ,  self.emp_salary)



obj = employee()
obj.work("padmaja", "programmer")
obj.attendance("padmaja","15 days","20 days")
obj.wages("padmaja","15 days", "20 days","salary")
