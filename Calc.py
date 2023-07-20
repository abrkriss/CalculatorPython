from CalculatorModel import CalculatorModel
from CalculatorView import CalculatorView
from CalculatorPresenter import CalculatorPresenter


model = CalculatorModel()
view = CalculatorView()
presenter = CalculatorPresenter(model, view)


presenter.calculate()