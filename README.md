# Laboratorio ADK UCV

## Descripción

Proyecto desarrollado con Google ADK para la creación de un agente académico capaz de explicar conceptos tecnológicos básicos.

## Tecnologías utilizadas

- Python 3.11
- Google ADK
- Poetry
- Pytest
- GitHub Actions
- GitHub

## Funcionalidades

- Explicación de conceptos tecnológicos.
- Integración con Google ADK.
- Pruebas unitarias automatizadas.
- Integración continua mediante GitHub Actions.

## Estructura del proyecto

```text
laboratorio-adk-ucv/
│
├── agente_ucv/
│   ├── __init__.py
│   └── agent.py
│
├── tests/
│   └── test_agent.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pyproject.toml
├── poetry.lock
└── README.md