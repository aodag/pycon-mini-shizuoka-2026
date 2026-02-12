from dataclasses import dataclass

@dataclass
class Deposit:
    amount: int


@dataclass
class Withdraw:
    amount: int

Message = Deposit | Withdraw

def bankaccount(probe: Generator[None, int|str, None], balance: int=0) -> Generator[int, Message, None]:
    try:
        while True:
            probe.send(balance)
            msg = yield
            match msg:
                case Deposit(amount):
                    balance += amount
                case Withdraw(amount):
                    balance -= amount
    except GeneratorExit:
        probe.send("shutdown bankaccount")
        return balance

def print_probe() -> Generator[None, int|str, None]:
    while True:
        m = yield
        print(m)

def history() -> Generator[None, int|str, None]:
    h = []
    try:
        while True:
            m = yield
            match m:
                case int(m):
                    h.append(m)
                case _:
                    pass
    except GeneratorExit:
        print(f"history: {h}")


pa = print_probe()
pa.send(None)
ha = history()
ha.send(None)
ba = bankaccount(ha)
ba.send(None)
ba.send(Deposit(10))
ba.send(Deposit(13))
ba.send(Withdraw(9))

ba.close()
pa.close()
ha.close()
