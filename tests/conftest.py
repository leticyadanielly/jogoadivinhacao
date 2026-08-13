# Autor: Leticya Danielly
# Data : 12/08/2026
### Configuração do pytest-html para relatórios detalhados ###
import pytest
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Adiciona os detalhes somente na etapa de execução do teste (call)
    if report.when == "call":
        # Captura a docstring do teste
        doc = item.function.__doc__
        
        # Garante a criação da lista de extras
        extra_list = getattr(report, "extras", [])
        
        if doc:
            # Formata o texto da docstring
            texto_descricao = doc.strip()
            # Anexa como bloco de texto visível no HTML
            extra_list.append(extras.text(texto_descricao, name="Descrição / Regra de Negócio"))
        else:
            extra_list.append(extras.text("Nenhuma docstring informada no teste.", name="Descrição / Regra de Negócio"))
            
        report.extras = extra_list


def pytest_html_report_title(report):
    report.title = "Relatório Detalhado de Testes - Jogo da Adivinhação"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><b>Projeto:</b> Jogo da Adivinhação (POM)</p>",
        "<p><b>Framework:</b> Pytest + Pytest-HTML v4</p>"
    ])