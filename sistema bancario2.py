
def menu():
  menu = '''
-------Banco LTDA----------
       [v] saldo
       [d] depositar
       [s] sacar
       [e] extrato
       [n] criar usuario
       [nc] nova conta
       [lc] listar contas
       [q] sair
       [r] resetar dia
---------------------------       
  ''' 
  return input(menu)
  
def saque(valor_saque):
  global saldo
  global numero_saques

  if numero_saques <= LIMITE_SAQUES and valor_saque <= saldo and valor_saque <= limite_diario and valor_saque > 0:
    saldo = saldo - valor_saque
    numero_saques = numero_saques + 1
    extrato.append('saque de R$: ')
    extrato.append(valor_saque)
    print('saque realizado')
    print('seu saldo é R$ ', saldo )
  
  if numero_saques > LIMITE_SAQUES:
    print('NÂO AUTORIZADO !!!!, seu limite de saques diarios foi atigido')
      
  if valor_saque > saldo:
    print('Operação falhou,voce não tem saldo suficiente')
    print('seu saldo é R$ ',saldo)
   
  if valor_saque > limite_diario:
    print('Operação falhou,voce só pode sacar este valor por vez R$ ', limite_diario) 
  
  return saldo

def depositar(deposito):
  global saldo

  if deposito > 0:
   saldo = saldo + deposito
   print('----------deposito realizado com sucesso---------' )
   extrato.append('deposito de R$: ')
   extrato.append(deposito)

  elif deposito <= 0:
   print('voce nao pode depositar um valor negativo')

  return saldo
 
def mostrar_extrato():
  print('Extrato ')
  for n in extrato:
   print(n)

def sistema():
  while True:
    opcao = menu()

    if opcao == 'v':
      print('seu saldo é R$',saldo)
    
    elif opcao == 'd':
      print('Depósito ')
      deposito = int(input('quanto voce quer depositar?'))
      depositar(deposito)
    
    elif opcao == 'nc':
      print('Nova conta')
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      if conta:
        contas.append(conta)

    elif opcao == 'lc':
      print('listar contas')
      listar_contas(contas)

    elif opcao == 's':
      print(' Saque ')
      valor_saque = int(input('quanto deseja sacar?'))
      saque(valor_saque)

    elif opcao == 'e':
      mostrar_extrato()

    elif opcao == 'n':
      print('criar usuario')
      criar_usuario(usuarios)

    elif opcao == 'q':
      print('Sair ')  
      break

    elif opcao == 'r':
      print('dia resetado,esta e uma opcao que reseta a variavel: numero_saques')
      numero_saques = 0

    else:
     print('opção invalida,por favor digite uma opção valida')

def criar_usuario(usuarios):
  cpf = input('digite seu cpf(somente numeros)')
  usuario = filtrar_usuario(cpf,usuarios)

  if usuario:
    print('ja existe usuario com este CPF')
    return

  nome = input('informe o nome completo:')
  data_nascimento = input('informe a data de nascimento (dd\mm\aaaa):')
  endereco = input('informe o endereço (logradouro, nro - bairro - cidade\sigla estado):')
  usuarios.append({'nome': nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereço':endereco})
  print('usuario criado com sucesso')

def filtrar_usuario(cpf,usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
  cpf = input('digite seu cpf(somente numeros)')
  usuario = filtrar_usuario(cpf,usuarios)

  if usuario:
    print('-------usuario criado com sucesso------------')
    return {'agencia':AGENCIA, 'numero_conta':numero_conta, 'usuario':usuario}

  print('usuari não encontrado, fluxo de criação de conta encerrado')

def listar_contas(contas):
  for conta in contas:
    linha = f'''
    agencia: {conta['agencia']}
    C/C:     {conta['numero_conta']}
    Titular: {conta['usuario']['nome']}
    '''
   
    print(linha)


AGENCIA = '0001'
saldo = 0
limite_diario = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []
usuarios = []
contas = []

sistema()

print('-------obrigado por usar o BANCO LTDA !!!!-----------')

      
 

  

