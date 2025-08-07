#mostrando opcoes ao usuario
import pyautogui as escolha_opcao
opcao = escolha_opcao.confirm('Clique no botao desejado.', buttons=['Excel', 'word', 'notepad'])  # confirm = emitir mensagem ou alerta

#condicao escolha
if opcao == "Excel":
    # estamos pressionando apertando as teclas windows + r
    escolha_opcao.hotkey('win', 'r')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #digitando a palavra excel
    escolha_opcao.typewrite('excel')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #apertando a tecla enter para abrir o programa
    escolha_opcao.press('enter')

    #aguarda 5 segundos
    escolha_opcao.sleep(5)

    print("Voce escolheu abrir o excel")

elif opcao == "word":
    escolha_opcao.hotkey('win', 'r')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #digitando a palavra word
    escolha_opcao.typewrite('word')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #apertando a tecla enter para abrir o programa
    escolha_opcao.press('enter')

    #aguarda 5 segundos
    escolha_opcao.sleep(5)

    print("Voce escolheu abrir o word")

elif opcao == "notepad":
    escolha_opcao.hotkey('win', 'r')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #digitando a palavra notepad
    escolha_opcao.typewrite('notepad')

    #aguarda dois segundos
    escolha_opcao.sleep(2)

    #apertando a tecla enter para abrir o programa
    escolha_opcao.press('enter')

    #aguarda 5 segundos
    escolha_opcao.sleep(5)

    #aguarda 2 segundos
    escolha_opcao.sleep(2)

    print("Voce escolheu abrir o notepad")