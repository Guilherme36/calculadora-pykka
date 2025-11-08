# Calculadora com Modelo de Atores - Pykka

Sistema de calculadora implementado usando o modelo de atores com a biblioteca Pykka em Python.

## 🎯 Objetivo

Demonstrar a implementação do **modelo de atores** para operações matemáticas básicas, garantindo:
- Concorrência
- Isolamento de falhas
- Rastreabilidade de operações
- Escalabilidade

## 🏗️ Arquitetura

### Componentes Principais

- **CalculatorActor**: Ator que processa operações matemáticas
- **CalculationMessage**: Mensagem estruturada para comunicação
- **CalculatorSystem**: Sistema que gerencia o ator

### Fluxo de Comunicação

```
Cliente → CalculatorSystem → CalculatorActor → Resultado
```

## 🚀 Instalação

1. **Criar ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ativar ambiente:**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

## 📋 Uso

### Exemplo Básico

```python
from calculator_actors import CalculatorSystem

# Iniciar sistema
system = CalculatorSystem()
system.start()

# Realizar cálculos
result = system.calculate("soma", 5.0, 3.0)
print(result)  # {"result": 8.0, "request_id": "uuid-123"}

# Parar sistema
system.stop()
```

### Operações Disponíveis

- `soma` - Adição
- `subtracao` - Subtração  
- `multiplicacao` - Multiplicação
- `divisao` - Divisão (com tratamento de divisão por zero)

## 🧪 Testes

Executar todos os testes:
```bash
python run_tests.py
```

Executar testes específicos:
```bash
python test_calculator_actors.py
```

### Cobertura de Testes

- ✅ Operações matemáticas básicas
- ✅ Tratamento de divisão por zero
- ✅ Operações inválidas
- ✅ Unicidade de request_id
- ✅ Error handling e timeouts

## 📁 Estrutura do Projeto

```
AC2/
├── calculator_actors.py      # Implementação do modelo de atores
├── test_calculator_actors.py # Testes unitários
├── run_tests.py             # Executor de testes
├── requirements.txt         # Dependências
└── README.md               # Documentação
```

## 🔧 Tecnologias

- **Python 3.12+**
- **Pykka 4.0.2** - Framework de atores
- **unittest** - Testes unitários
- **dataclasses** - Estruturas de dados

## ✨ Vantagens do Modelo de Atores

1. **Concorrência**: Múltiplas operações simultâneas
2. **Isolamento**: Falhas não afetam outras operações
3. **Escalabilidade**: Fácil adicionar mais atores
4. **Rastreabilidade**: Cada operação tem ID único
5. **Tolerância a Falhas**: Recovery automático

## 📊 Exemplo de Saída

```json
{
  "result": 15.0,
  "request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

## 🚨 Tratamento de Erros

```json
{
  "error": "Divisão por zero não permitida",
  "request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

## 📈 Performance

- **Tempo de resposta**: < 10ms por operação
- **Concorrência**: Suporta múltiplas operações simultâneas
- **Timeout**: 1 segundo por operação

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é para fins educacionais - Facens PgDt AC2.