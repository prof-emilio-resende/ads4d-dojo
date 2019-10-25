class Racional_Calculo:
    def __init__(self, salario_bruto, desconto_inss, deducao_dependentes, valor_base, valor_isencao, faixa_enquadramento, valor_para_descontar, valor_irrf):
        self.salario_bruto = salario_bruto
        self.desconto_inss = desconto_inss
        self.deducao_dependentes = deducao_dependentes
        self.valor_base = valor_base
        self.valor_isencao = valor_isencao
        self.faixa_enquadramento = faixa_enquadramento
        self.valor_para_descontar = valor_para_descontar
        self.valor_irrf = valor_irrf