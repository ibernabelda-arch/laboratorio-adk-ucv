from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str):

    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "python": "Python es un lenguaje de programación.",
        "github": "GitHub permite almacenar código.",
        "ia": "La inteligencia artificial permite que las máquinas aprendan."
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }

root_agent = Agent(
    model="gemini-2.5-flash",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    """,
    tools=[explicar_concepto]
)