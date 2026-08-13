# Autor: Leticya Danielly
# Data : 12/08/2026
### Script de regressão para o projeto ###
#!/bin/bash

# Define cores para saída do terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # Sem Cor

echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}   INICIANDO SUÍTE DE TESTES DE REGRESSÃO (POM)     ${NC}"
echo -e "${BLUE}====================================================${NC}"

# 1. Limpa relatórios antigos ou cria a pasta de resultados
mkdir -p reports

# 2. Executa a suíte completa com Pytest e gera o relatório HTML
echo -e "\n${GREEN}[1/2] Executando testes dos Níveis 1, 2 e 3...${NC}\n"

pytest --html=reports/relatorio_regressao.html --self-contained-html -v

# 3. Captura o status da execução
STATUS=$?

if [ $STATUS -eq 0 ]; then
    echo -e "\n${GREEN}====================================================${NC}"
    echo -e "${GREEN}   SUCESSO! Todos os testes passaram.               ${NC}"
    echo -e "${GREEN}   Relatório gerado em: reports/relatorio_regressao.html${NC}"
    echo -e "${GREEN}====================================================${NC}"
else
    echo -e "\n${RED}====================================================${NC}"
    echo -e "${RED}   ATENÇÃO! Falhas encontradas na regressão.        ${NC}"
    echo -e "${RED}   Verifique o relatório: reports/relatorio_regressao.html${NC}"
    echo -e "${RED}====================================================${NC}"
fi

exit $STATUS