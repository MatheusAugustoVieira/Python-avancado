from utilidadecev.moeda import moeda
from utilidadecev.dado import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
