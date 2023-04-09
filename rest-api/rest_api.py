'''
This module contains the RestAPI class.
Normally, would implement the API using Flask or Django, or other server,
as the client-server paradigm implementing separation of concerns is a requirement of RESTful APIs 
Normally, a REST API would have some way to persist the data between requests. 
This is because a requirement for REST is that the server be stateless. 
However the tests for this exercise do not require the data to persist between requests, 
and I don't know whether the exercism test runner will allow file access (I would expect not).
'''
import json


class RestAPI:
    def __init__(self, database=None):
        self.users = {}
        if not database:
            return
        init_users = database["users"]
        for user in init_users:
            print(user)
            print(user["name"])
            self.users[user['name']] = User(
                    user["name"],
                    user["owes"],
                    user["owed_by"],
                    user["balance"],
                )

    def get(self, url, payload=None):
        if url == '/users':
            if payload:
                req_users = json.loads(payload)["users"]
                return json.dumps({"users": [self.users[name].to_json() for name in req_users]}, sort_keys=False)
            return json.dumps({"users": [user.to_json() for user in sorted(self.users.values())]}, sort_keys=False)

    def post(self, url, payload=None):
        if url == '/iou' and payload:
            lender, borrower, amount = self.parse_iou_payload(payload)
            lender.lend(borrower.name, amount)
            borrower.borrow(lender.name, amount)
            
            return json.dumps({"users": [user.to_json() for user in sorted([lender, borrower])]}, sort_keys=False)
        if url == '/add':
            new_user = User(json.loads(payload)["user"])
            self.users[new_user.name] = new_user
            return json.dumps(new_user.to_json())

    def parse_iou_payload(self, payload):
        payload = json.loads(payload)
        lender = self.users[payload["lender"]]
        borrower = self.users[payload["borrower"]]
        amount = payload["amount"]
        return lender, borrower, amount



class User:
    def __init__(self, name, owes={}, owed_by={}, balance=0.0):
        self.name = name
        self.ledger = {}
        for user, amount in owes.items():
            self.borrow(user, amount)
        for user, amount in owed_by.items():
            self.lend(user, amount)
        assert self.balance == balance

    def __hash__(self):
        return self.name.__hash__()

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __repr__(self):
        return f"User({self.to_json()})"

    def lend(self, borrower, amount):
        self.ledger[borrower] = self.ledger.get(borrower, 0) + amount

    def borrow(self, lender, amount):
        self.ledger[lender] = self.ledger.get(lender, 0) - amount

# Stole property decorators (and ledger) from cmccandless solution
# https://exercism.org/tracks/python/exercises/rest-api/solutions/cmccandless
    @property
    def owes(self):
        return {user: -amount for user, amount in self.ledger.items() if amount < 0}

    @property
    def owed_by(self):
        return {user: amount for user, amount in self.ledger.items() if amount > 0}

    @property
    def balance(self):
        return sum(self.ledger.values())

    def to_json(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance,
        }



