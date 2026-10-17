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

    def fillDDCustomer(self):
        allCustomer = self._model.getCustomers()
        for a in allCustomer:
            self._view._ddCustomer.options.append(
                ft.dropdown.Option(data=a, key=a.__str__(), on_click=self._choiceDDCustomer))

    def _choiceDDCustomer(self, e):
        self._choiceCustomer = e.control.data
        print(f"hai selezionato {self._choiceCustomer.__str__()}")

    def handleCreaGrafo(self, e):
        if self._choiceCountry is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Per poter procedere, scegliere una nazione.", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(self._choiceCountry)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))
        self.fillDDCustomer()
        self._view.update_page()

    def handleTop5Clienti(self, e):
        pass

    def handleTop5Canzoni(self, e):
        pass

    def handleRankEmployee(self, e):
        pass

    def handleCammino(self, e):
        pass