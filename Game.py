##Jo Ken Po

import random
import time
import os

atopc = ['PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK']
vitoria = []
derrota = []
empate = []
partidas = []
 

def ranking():

    ranking_vitoria = sum(vitoria)
    ranking_derrota = sum(derrota)
    ranking_empate = sum(empate)
    partidas_totais = ranking_vitoria + ranking_derrota + ranking_empate
    os.system('cls')
    print ('Calculando as suas partidas')
    time.sleep(2)
    print ('\nO Placar atual é: Vitorias:', (ranking_vitoria), 'Derrotas:', (ranking_derrota), 'Empates:', (ranking_empate))
    time.sleep(1)
    print ('\nTotal de partidas:', (partidas_totais))
    time.sleep(1)

    salvar = str(input('\nGostaria de salvar o seu Ranking?'
    '\n\n[1] - Sim'
    '\n\n[2] - Não'
    '\n\nSelecione a sua opção: '))
    
    
    if (salvar == '1'):
      arquivo = open('Ranking.txt', 'w')
      print ('\nO Placar atual é: Vitorias:', (ranking_vitoria), 'Derrotas:', (ranking_derrota), 'Empates:', (ranking_empate), file = arquivo)
      print ('\nTotal de partidas:', (partidas_totais), file = arquivo)
      print ('\nSalvando seu Ranking')
      time.sleep(1)
      print ('\nSeu Ranking esta salvo')
      arquivo.close()
      time.sleep(1)
      print ('\nVoltando ao menu')
      time.sleep(2)
      os.system('cls')
      menu()
 
    elif (salvar == '2'):
        print ('\nVoltando ao menu')
        menu()
    else:
        print ('\nOpção inválida...Voltando ao menu')
        menu()


def menu():
    continuar = str(input('\nO que gostaria de fazer?'
    '\n\n[1] - Continuar'
    '\n\n[2] - Ranking parcial'    
    '\n\n[99] - Sair'
    '\n\nInforme a sua opção '))    
    if (continuar == '1'):
        jogar()
    elif (continuar == '2'):
        ranking()
    elif (continuar == '99'):
        print ("Saindo...")    
    else:
        print ('Opção inválida...tente novamente')
        menu()
        
        
def ajuda():
    os.system('cls')
    titulo = ('Como Jogar')
    linha = '-' * 80
    nome_do_jogo = ('Pedra, Papel, Tesoura, Lagarto ou Spock')
    instrucaoI = ('\nO Jogador deverá escolher, entre Pedra, Papel, Tesoura, Lagarto ou Spock.')
    instrucaoII = ('\nApós o jogador, o computador fará sua escolha entre as opções acima.')
    instrucaoIII = ('\nSerão comparadas as escolhas do Jogador e do Computador.')
    instrucaoIV = ('\nCada escolha possui vantagens e desvatagens.')
    instrucaoV = ('\nO vencedor é aquele com a opção que tenha vantagem sob o seu adversário.')
    instrucaoVI = ('\nCaso a opção do Jogador e do Computador sejam iguais, será declarado Empate.')
    
    regrasI = ('Pedra GANHA de Tesoura e Lagarto')
    regrasII = ('Pedra PERDE de Papel e Spock')
    regrasIII = ('Papel GANHA de Pedra e Spock')
    regrasIV = ('Papel PERDE de Tesoura e Lagarto')
    regrasV = ('Tesoura GANHA de Papel e Lagarto')
    regrasVI = ('Tesoura PERDE de Pedra e Spock')
    regrasVII = ('Lagarto GANHA de Papel e Spock')
    regrasVIII = ('Lagarto PERDE de Pedra e Tesoura')
    regrasIX = ('Spock GANHA de Pedra e Tesoura')
    regrasX = ('Spock PERDE de Papel e Lagarto')

    print (titulo.center(80))
    print ('')
    print (nome_do_jogo.center(80))
    print (linha.center(80))
    print (instrucaoI)
    print (instrucaoII)
    print (instrucaoIII) 
    print (instrucaoIV)
    print (instrucaoV)
    print (instrucaoVI)
    print ('')
    print (linha)
    print (regrasI.center(80))
    print (regrasII.center(80))
    print (linha)
    print (regrasIII.center(80))
    print (regrasIV.center(80))
    print (linha)
    print (regrasV.center(80))
    print (regrasVI.center(80))
    print (linha)
    print (regrasVII.center(80))
    print (regrasVIII.center(80))
    print (linha)    
    print (regrasIX.center(80))
    print (regrasX.center(80))
    print (linha)
    
    menu_ajuda = str(input('\nO que gostaria de fazer?'
                           '\n\n[1] - Retornar ao menu inicial'
                           '\n\n[2] - Sair'
                           '\n\nQual a opção desejada? '))
    if (menu_ajuda == '1'):
        print ('Voltando ao menu...')
        time.sleep(2)
        bem_Vindo()
    
    elif (menu_ajuda == '2'):    
        print ('Saindo...')     
    
    else:
        print ('Opção inválida...Voltando ao menu')
        time.sleep(2)
        bem_Vindo()

def bem_Vindo():
    os.system('cls')
    print ('Pedra, Papel, Tesoura, Lagarto ou Spock')
    iniciar = str(input('\nBem vindo!' 
    '\n\n[1] - Jogar'
    '\n\n[2] - Ranking'
    '\n\n[3] - Ajuda'
    '\n\n[99] - Sair'
    '\n\nQual a opção desejada? '))
    
    if (iniciar == '1'):
        jogar()
    elif (iniciar == '2'):
        ranking()
    elif (iniciar == '3'):
        ajuda()
    elif (iniciar == '99'):
        print ('Saindo...')
    else:
        print ('Opção inválida...tente novamente')
        bem_Vindo()

def jogar():
   os.system('cls') 
   ato = str(input('\nQual a sua Jogada?'
   '\n\n[1] - Pedra'
   '\n\n[2] - Papel'
   '\n\n[3] - Tesoura'
   '\n\n[4] - Lagarto'
   '\n\n[5] - Spock'
   '\n\n[99] - Sair'
   '\n\nInforme a sua opção: '))
   
   if (ato == '1'):
        print ('\nSua Jogada é: Pedra')
        print ('\nHora do computador escolher')
        time.sleep(2)
        jogadapcI = (random.choice(atopc))
        print ('\nO computador escolheu')
        time.sleep(1)
        print ('\nVamos lá')
        time.sleep(1)
        print ('\nJo')
        time.sleep(1)
        print ('\nken')
        time.sleep(1)
        print ('\nPo')
        time.sleep(1)
        print ('\nO computador escolheu:', (jogadapcI))
        
        if (jogadapcI == ('PEDRA')):
            print ('\nDeu empate')
            empate.append(1)
            menu()
    
        elif (jogadapcI == ('PAPEL')):
            print ('\nVocê perdeu')
            derrota.append(1)
            menu()
        
        elif (jogadapcI == ('TESOURA')):
            print ('\nVocê Ganhou')
            vitoria.append(1)
            menu()
        
        elif (jogadapcI == ('LAGARTO')):
            print ('\nVocê Ganhou')
            vitoria.append(1)
            menu()
        
        elif (jogadapcI == ('SPOCK')):
            print ('\nvocê Perdeu')
            derrota.append(1)
            menu()
            
   elif (ato == '2'):
        print ('\nSua Jogada é: Papel')
        print ('\nHora do computador escolher')
        time.sleep(2)
        jogadapcI = (random.choice(atopc))
        print ('\nO computador escolheu')
        time.sleep(1)
        print ('\nVamos lá')
        time.sleep(1)
        print ('\nJo')
        time.sleep(1)
        print ('\nken')
        time.sleep(1)
        print ('\nPo')
        time.sleep(1)
        print ('\nO computador escolheu:', (jogadapcI))
      
        if (jogadapcI == ('PEDRA')):
             print ('\nVocê Ganhou')
             vitoria.append(1)
             menu()
         
        elif (jogadapcI == ('PAPEL')):
             print ('\nDeu empate')
             empate.append(1)
             menu()
         
        elif (jogadapcI == ('TESOURA')):
             print ('\nvocê Perdeu')
             derrota.append(1)
             menu()  
         
        elif (jogadapcI == ('LAGARTO')):
             print ('\nvocê Perdeu')
             derrota.append(1)
             menu()  
         
        elif (jogadapcI == ('SPOCK')):
             print ('\nVocê Ganhou')
             vitoria.append(1)
             menu()
    
   elif (ato == '3'):
      print ('\nSua Jogada é: Tesoura')
      print ('\nHora do computador escolher')
      time.sleep(2)
      jogadapcI = (random.choice(atopc))
      print ('\nO computador escolheu')
      time.sleep(1)
      print ('\nVamos lá')
      time.sleep(1)
      print ('\nJo')
      time.sleep(1)
      print ('\nken')
      time.sleep(1)
      print ('\nPo')
      time.sleep(1)
      print ('\nO computador escolheu:', (jogadapcI))
      
      if (jogadapcI == ('PEDRA')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
       
      elif (jogadapcI == ('PAPEL')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()
       
      elif (jogadapcI == ('TESOURA')):
           print ('\nDeu empate')
           empate.append(1)
           menu()
       
      elif (jogadapcI == ('LAGARTO')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()  
       
      elif (jogadapcI == ('SPOCK')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
    
   elif (ato == '4'):
      print ('\nSua Jogada é: Lagarto')
      print ('\nHora do computador escolher')
      time.sleep(2)
      jogadapcI = (random.choice(atopc))
      print ('\nO computador escolheu')
      time.sleep(1)
      print ('\nVamos lá')
      time.sleep(1)
      print ('\nJo')
      time.sleep(1)
      print ('\nken')
      time.sleep(1)
      print ('\nPo')
      time.sleep(1)
      print ('\nO computador escolheu:', (jogadapcI))
      
      if (jogadapcI == ('PEDRA')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
       
      elif (jogadapcI == ('PAPEL')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()
       
      elif (jogadapcI == ('TESOURA')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
       
      elif (jogadapcI == ('LAGARTO')):
           print ('\nDeu empate')
           empate.append(1)
           menu() 
       
      elif (jogadapcI == ('SPOCK')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()
    
   elif (ato == '5'):
      print ('\nSua Jogada é: Spock')
      print ('\nHora do computador escolher')
      time.sleep(2)
      jogadapcI = (random.choice(atopc))
      print ('\nO computador escolheu')
      time.sleep(1)
      print ('\nVamos lá')
      time.sleep(1)
      print ('\nJo')
      time.sleep(1)
      print ('\nken')
      time.sleep(1)
      print ('\nPo')
      time.sleep(1)
      print ('\nO computador escolheu:', (jogadapcI))
      
      if (jogadapcI == ('PEDRA')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()
       
      elif (jogadapcI == ('PAPEL')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
       
      elif (jogadapcI == ('TESOURA')):
           print ('\nVocê Ganhou')
           vitoria.append(1)
           menu()
       
      elif (jogadapcI == ('LAGARTO')):
           print ('\nvocê Perdeu')
           derrota.append(1)
           menu()  
       
      elif (jogadapcI == ('SPOCK')):
           print ('\nDeu empate')
           empate.append(1)
           menu() 
    
   elif (ato == '99'):
        print('Saindo...')
    
   else:
       print('Opção inválida...tente novamente')
       jogar()



bem_Vindo()