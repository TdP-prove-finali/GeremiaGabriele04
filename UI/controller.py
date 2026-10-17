import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._choiceCountry = None
        self._choiceCustomer = None

    def fillDDCountry(self):
        allCountry = self._model.getAllCountry()
        for c in allCountry:
            self._view._ddCountry.options.append(
                ft.dropdown.Option(data=c, key=c, on_click=self._choiceDDCountry))

    def _choiceDDCountry(self, e):
        self._choiceCountry = e.control.data
        print(f"hai selezionato {self._choiceCountry}")

    def handleCreaGrafo(self, e):
        pass

    def handleTop5Clienti(self, e):
        pass

    def handleTop5Canzoni(self, e):
        pass

    def handleRankEmployee(self, e):
        pass

    def handleCammino(self, e):
        pass