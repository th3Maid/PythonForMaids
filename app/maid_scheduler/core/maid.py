from core.maid_base import Maid

class MaidChild(Maid):

    def __init__(self, maid_nick: str, maid_name: str, maid_job: str, maid_schedule: dict):
        self.maid_nick = maid_nick
        self.maid_name = maid_name
        self.maid_job  = maid_job
        self.maid_schedule = maid_schedule

    def schedule(self):
        return self.maid_schedule

    def f_schedule(self):
        for key in self.maid_schedule.keys():
            print(f'Dia {key} | Schedule {self.maid_schedule[key]}')
