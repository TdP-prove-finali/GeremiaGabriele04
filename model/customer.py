from dataclasses import dataclass


@dataclass
class Customer:
    CustomerId: int
    FirstName: str
    LastName: str
    Company: str
    Address: str
    City: str
    State: str
    Country: str
    PostalCode: str
    Phone: str
    Fax: str
    Email: str
    SupportRepId: int

    def __eq__(self, other):
        return self.CustomerId == other.CustomerId

    def __hash__(self):
        return hash(self.CustomerId)

    def __str__(self):
        return f"{self.LastName} {self.FirstName} [ID:{self.CustomerId}]"

    def stampa(self):
        return f"Cognome: {self.LastName}\nNome: {self.FirstName}\nIDCliente: {self.CustomerId}\nNumero di telefono: {self.Phone}\nEmail: {self.Email}"