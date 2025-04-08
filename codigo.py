# Lista com os valores de vendas realizadas em cada semana do mês
vendas_mensais = [1000, 1000, 200]

# Função que recebe uma lista de valores e retorna a soma total
def calcular_total_vendas(vendas):
    return sum(vendas)  # soma todos os valores da lista e retorna o total

# Função que gera um relatório simples com o total de vendas
def gerar_relatorio():
    total = calcular_total_vendas(vendas_mensais)  # Chama a função para calcular o total
    print("Relatório de vendas - Março")           # Exibe o título do relatório
    print("Total de vendas: R$", total)            # Exibe o valor total calculado

# Chamada da função principal para executar o relatório
gerar_relatorio()
