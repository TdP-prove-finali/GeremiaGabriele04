from dataclasses import dataclass
from datetime import datetime


@dataclass
class Employee:
    EmployeeId: int
    LastName: str
    FirstName: str
    Title: str
    ReportsTo: int
    BirthDate: datetime
    HireDate: datetime
    Address: str
    City: str
    State: str
    Country: str
    PostalCode: str
    Phone: str
    Fax: str
    Email: str

    def __eq__(self, other):
        return self.EmployeeId == other.EmployeeId

    def __hash__(self):
        return hash(self.EmployeeId)

    def __str__(self):
        return f"{self.LastName} {self.FirstName} [ID:{self.EmployeeId}]"

    def stampa(self):
        return (f"**Cognome:** {self.LastName}  \n"
                f"**Nome:** {self.FirstName}  \n"
                f"*ID Impiegato:* {self.EmployeeId}  \n"
                f"*Ruolo:* {self.Title}  \n"
                f"*Numero di telefono:* {self.Phone}  \n"
                f"*Email:* {self.Email}")