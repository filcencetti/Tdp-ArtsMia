import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo creato. Il grafo contiene {self._model.getNumNodes()} nodi "
                    f"e {self._model.getNumEdges()} archi."))
        self._view.update_page()


    def handleCompConnessa(self,e):
        txtInput = self._view._txtIdOggetto.value
        if txtInput == "" or txtInput is None:
            self._view.txt_result.controls.clear()
            self._view.create_alert(f"Inserire un valore valido")
            self._view.update_page()
            return

        try:
            idInput = int(txtInput)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.create_alert(f"Il valore inserito non è un numero")
            self._view.update_page()
            return

        if not self._model.hasNode(idInput):
            self._view.txt_result.controls.clear()
            self._view.create_alert(f"L'id inserito non corrisponde a un oggetto del database")
            self._view.update_page()
            return


        infoConnessa = self._model.getInfoConnessa(idInput)




