from agente_ucv.agent import explicar_concepto

def test_api():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"