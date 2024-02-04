<h1 align ="center"> Sistema Financeiro DinDin Bank </h1>

<h3 align= "center" > <b> Um gerenciador financeiro pessoal <br> perfeito para as suas principais movimentações do dia a dia </b> </h3>

<br>

O DinDin Bank foi criado no curso de Engenharia de Dados oferecido pelo banco Santander Brasil por meio do programa Santander Coders 2023 (2 Edição) em parceria com a Ada Tech. 

O desafio desse projeto foi criar um sistema de controle financeiro para gerenciar algumas operações dentre elas:

- <u>Criar</u> novos registros:
    - Os tipos de registros são: receita, despesa ou investimento.
        - No caso de <b> receita </b>, o valor foi tratado como numérico e armazenado normalmente.
        - No caso de <b> despesa </b>, o valor foi recebido como positivo, mas armazenado como negativo.
        - No caso de <b> investimento </b>, o valor tem algumas informações adicionais pré-definidas a fim de calcular o montante: o valor que foi investido e a taxa de juros do investimento (juros simples). Sendo o montante (M) para uma dada taxa de juros i após t dias pode ser calculado pela seguinte relação: M = V * (1+i) ** t
- <u>Ler</u> registros: É possível consultar registros por data, tipo ou valor (esses são filtros). Além de poder filtrar todos os registros existentes até então.
- <u>Atualizar</u> registros: Por meio do ID é possível atualizar o registro alterando o seu valor ou tipo. Automaticamente a nova data será a de atualização do registro. 
- <u>Deletar</u> registros: Também por meio do ID é possível deletar o registro.

Para finalizar o desafio, não pude utilizar biblioteca pandas para melhor entendimento de conceitos importantes abordados durante o primeiro módulo do curso. Além disso todos os registros deveriam ser armazenados em algum tipo de arquivo de leitura, sendo ele csv ou json. A minha escolha para esse projeto foi armazenar os registros em arquivo csv. 

 







