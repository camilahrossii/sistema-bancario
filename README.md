#### Desafio 01 - Bootcamp Dio - Ciências de Dados com Python

# Sistema Bancário

O sistema inclui as operações: sacar, depositar e visualizar extrato.

➡ Depósito: é possível depositar valores positivos para a conta bancária, todos os depósitos foram armazenados em uma variável e exibidos na operação "extrato".

➡ Saque: o sistema permite realizar até 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema exibe uma mensagem informando o saldo insuficiente em conta. Todos os saques são armazenados em uma variável e exibidos na operação de "extrato".

➡ Extrato: essa operação lista todos os depósitos e saques realizados na conta. Ao final da listagem é exibido o saldo atual da conta com a formatação de moeda real.

# Otimizando o Sistema Bancário com Funções

### Criar funções: sacar, depositar e visualizar histórico

➡ Saque: receber os argumentos apenas por nome (keyword only). 
    - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
    - Sugestão de retorno: saldo e extrato

➡ Depósito: receber os argumentos apenas por posição (positional only)
    - Sugestão de argumentos: saldo, valor, extrato.
    - Sugestão de retorno: saldo e extrato

➡  Visualizar_extrato: receber os argumentos por posição e nome (positional only e keyword only).
    - Argumentos posicionais: saldo, argumentos nomeados: extrato.

### Criar mais duas funções: criar usuário e criar conta corrente (vincular com usuário)


➡  Criar_usuario: O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
    - Endereço: string com formato: logradouro, nro - bairro - cidade/sigla estado.
    - Deve ser armazenado somento os números do CPF. 
    - Não podemos cadastrar dois usuários com o mesmo CPF.

➡ Criar_conta_corrente: O programa deve armazenar contas em uma lista, uma conta é composta pot agêcia, número da conta e usuário. 
  - O número da conta é sequencial, iniciado em 1.
  - O número da agência é fixo: "0001".
  - O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.
  
#### Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
