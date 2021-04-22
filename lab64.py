class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    @classmethod
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x, y):
        return x ** y + 2 * y + 5


t1 = Team()
print(t1.all_working_hour())
print(t1.working_hour())
print(Team.member, t1.member, Team.get_member(), t1.get_member())
print(Team.calculate(5, 6))