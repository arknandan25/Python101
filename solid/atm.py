# Bottom UP approch
# Smallest Component  ->  Largest Components
from abc import ABC, abstractmethod


class InvalidException(Exception):
    pass

class Address:
    def __init__(self, street, city, country, eir):
        self.street = street
        self.city = city
        self.country = country
        self.eir = eir


class Card:
    name: str
    card_no: int
    expiry_date: str
    # pin as part of card and withdrawal limit, but these should be associated w/ account not card
    # or assume for simpicity
    pin: int
    withdrawal_limit: int

class CardReader:
    def __init__(self, card):
        self.card = card
        self.aunthenticate_card()


    # CardReader must authenticate is the card(hardware is correct or not)
    # Ask interviewer
    def aunthenticate_card(self) -> bool:
        """
        Verify if the card is a bank ATm card or not
        An ATm allows transactions via cards from different banks (associated banks)
        But you need to verify if the user inserted a tesco gift
        :return:
        :raise: InvalidCard Exception
        """
        pass
        # raise InavalidCard("Invalid card  inserted by user")

    def get_card_details(self) -> Card:
        pass


class Screen:
    def print_ouput(self) -> str:
        pass


class Keypad:
    def get_input(self):
        pass


class Account:
    def __init__(self, account_number, card_number, balance, acc_holder_name, date_created):
        pass

class Customer:
    name: str
    account: Account
    card: Card

from enum import Enum
class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BALANCE = "balance"

class TransactionStatus(Enum):
    STARTED = "STARTED"; SUCCESS = "success"; CANCELLED = "cancelled"; PENDING = "pending"; ERROR = "error";


class Transaction(ABC):
    t_id: int
    t_type: TransactionType
    t_date: str
    t_amt: float
    t_status: TransactionStatus

    @abstractmethod
    def execute(self):
        pass

class BalanceInquiry(Transaction):
    def execute(self):
        pass

class Deposit(Transaction):
    # amt: float

class Withdraw(Transaction):
    # amt: float

class Transfer(Transaction):
    # use init here to add super
    # since we take one new args here, we will need to take all transaction args in this class
    # then use super().__init(all transaction args)
    # thats the only way
    def __init__(self, dest_account: int):
        super().__init__()
    dest_account: int
    amt: float

class CashDispenser:
    pass

class ATM:
    def __init__(self, atm_id: int,
                 atm_location: Address,
                 card_reader: CardReader,
                 screen: Screen,
                 keypad: Keypad,
                 ):
        self.atm_id = atm_id
        self.atm_location = atm_location
        # self.card = card is card is taken as input, what will you do w/ self.card_reader to get card detials
        # so better card reader takes the card, and we use the card reader to get card detials
        self.card_reader = card_reader
        self.screen = screen
        self.keypad = keypad

    # def find_user(self, card_number):
    #     """
    #     Return an object of user account
    #     :param card_number:
    #     :return:
    #     """
    #     pass

    def authenticate_user(self, card: Card):
        # authenticates if the pin is correct or  not for this particular customer
        pass


    def execute_transaction(self, customer: Customer, transaction: Transaction):
        """
        Remember the driving force would not be within this schema,
        means someone(driver) will have to provide us with Transaction
        better way is to use open-close principle for Transaction as abstract class
        and transaction will either be BalanceInquiry, Deposit, WIthdrawal, Transfer
        :param customer:
        :param transaction:
        :return:
        """
        pass


class Bank:
    name: str
    atm_list: list[ATM]
    account_list: list[Account]

