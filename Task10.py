class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_gender(self):
        print("Person")


class Male(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_gender(self):
        print("The gender of person is male")


class Female(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_gender(self):
        print("The gender of the person is female")


if __name__ == '__main__':
    female = Female("Arooj", "Gohar")
    female.get_gender()

    male = Male("Usman", "Ali")
    male.get_gender()

    person = Person("Sohail", "Ali")
    person.get_gender()
