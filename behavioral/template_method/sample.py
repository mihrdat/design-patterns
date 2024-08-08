from abc import ABC, abstractmethod


class AuditTrail:
    def record(self):
        print("Audit")


class Task(ABC):
    def __init__(self):
        self.audit_trail = AuditTrail()

    @abstractmethod
    def _do_execute(self): ...

    def execute(self):
        self.audit_trail.record()
        self._do_execute()


class TransferMoneyTask(Task):
    def _do_execute(self):
        print("Transfer Money")


class LoanRequestTask(Task):
    def _do_execute(self):
        print("Loan Request")


task = TransferMoneyTask()
task.execute()
