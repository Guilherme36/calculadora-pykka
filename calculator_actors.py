import pykka
import uuid
from dataclasses import dataclass

@dataclass
class CalculationMessage:
    operation: str
    a: float
    b: float
    request_id: str

class CalculatorActor(pykka.ThreadingActor):
    def on_receive(self, message: CalculationMessage):
        if message.operation == "soma":
            result = message.a + message.b
        elif message.operation == "subtracao":
            result = message.a - message.b
        elif message.operation == "multiplicacao":
            result = message.a * message.b
        elif message.operation == "divisao":
            if message.b == 0:
                return {"error": "Divisão por zero não permitida", "request_id": message.request_id}
            result = message.a / message.b
        else:
            return {"error": "Operação inválida", "request_id": message.request_id}
        
        return {"result": result, "request_id": message.request_id}

class CalculatorSystem:
    def __init__(self):
        self.calculator_actor = None
    
    def start(self):
        self.calculator_actor = CalculatorActor.start()
    
    def calculate(self, operation: str, a: float, b: float) -> dict:
        request_id = str(uuid.uuid4())
        message = CalculationMessage(operation, a, b, request_id)
        try:
            return self.calculator_actor.ask(message, timeout=1.0)
        except Exception as e:
            return {"error": f"Calculation failed: {str(e)}", "request_id": request_id}
    
    def stop(self):
        if self.calculator_actor:
            self.calculator_actor.stop()
        pykka.ActorRegistry.stop_all()