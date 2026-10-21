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
        self._view._ddCustomer.options.clear()
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

        self._view._btnTop5Clienti.disabled = False
        self._view._btnTop5Canzoni.disabled = False
        self._view._btnRankEmployee.disabled = False
        self._view._ddCustomer.disabled = False
        self._view._btnCammino.disabled = False

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!", color="green"))
        self._view.txt_result.controls.append(ft.Text("Selezionare una funzione del sistema."))
        #self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodi()}"))
        #self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))
        self.fillDDCustomer()
        self._view.update_page()

    def handleTop5Customers(self, e):
        lista = self._model.getTop5Customers(self._choiceCountry)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Di seguito i migliori 5 clienti per numero di canzoni acquistate e importo complessivo pagato:"))
        for tupla in lista:
            self._view.txt_result.controls.append(ft.Markdown(
            f"{tupla[0].stampa()}  \n"
            f"**Canzoni acquistate:** **{tupla[1]}**  \n"
            f"**Importo totale:** **{tupla[2]}€**"
            ))
            self._view.txt_result.controls.append(ft.Text(f"\n"))
            self._view.update_page()


    def handleTop5Tracks(self, e):
        lista = self._model.getTop5Tracks(self._choiceCountry)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Di seguito le 5 canzoni più vendute e l'incasso totale ricavato:"))
        for tupla in lista:
            self._view.txt_result.controls.append(ft.Markdown(
                f"{tupla[0].stampa()}  \n"
                f"*Artista:* {tupla[2]}  \n"
                f"*Album:* {tupla[3]}  \n"
                f"*Genere:* {tupla[4]}  \n"
                f"*Costo unitario:* {tupla[0].UnitPrice}  \n"
                f"**Numero di vendite:** **{tupla[1]}**  \n"
                f"**Incasso totale:** **{tupla[1] * tupla[0].UnitPrice}€**"
            ))
            self._view.txt_result.controls.append(ft.Text(f"\n"))
            self._view.update_page()

    def handleRankEmployee(self, e):
        lista = self._model.getRankEmployees(self._choiceCountry)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Di seguito le prestazioni dei dipendenti, in termini di clienti soddisfatti appartenenti alla nazione selezionata, numero di tracce vendute e ricavo ottenuto da tali vendite:"))
        for tupla in lista:
            self._view.txt_result.controls.append(ft.Markdown(
                f"{tupla[0].stampa()}  \n"
                f"**Numero clienti:** {tupla[1]}  \n"
                f"**Numero tracce:** {tupla[2]}  \n"
                f"**Ricavo complessivo:** **{tupla[3]}€**"
            ))
            self._view.txt_result.controls.append(ft.Text(f"\n"))
            self._view.update_page()

    def handleCammino(self, e):
        if self._choiceCustomer is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Per poter procedere con la generazione del piano di Cross-Selling, selezionare un cliente.", color="red"))
            self._view.update_page()
            return

        lista = self._model.getCrossSellingPlan(self._choiceCustomer)
        self._view.txt_result.controls.clear()
        #
        self._view.txt_result.controls.append(ft.Text("Ciao mondo"))
        #
        self._view.update_page()
