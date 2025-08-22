import os
import sys
import time

def type_text(text, delay=0.03, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_enter(msg="\n[ENTER] continuar..."):
    input(msg)

def splash():
    clear_screen()
    print(r"""
                       __________                                 
                     .'----------`.                              
                     | .--------. |                             
                     | |########| |       __________              
                     | |########| |      /__________\             
            .--------| `--------' |------|    --=-- |-------------.
            |        `----,-.-----'      |o ======  |             | 
            |       ______|_|_______     |__________|             | 
            |      /  %%%%%%%%%%%%  \                             | 
            |     /  %%%%%%%%%%%%%%  \                            | 
            |     ^^^^^^^^^^^^^^^^^^^^                            | 
            +-----------------------------------------------------+
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """)
    print('\n')
    print(r"""
  ___ ___  __     _ ___ _____ ___     __  ___ _    _____   ___  __  _  _ 
 | _ \ _ \/  \ _ | | __|_   _/ _ \   /  \| _ ) |  |_ _\ \ / / |/  \| \| |
 |  _/   / () | || | _|  | || (_) | | () | _ \ |__ | | \ V /| | () | .` |
 |_| |_|_\\__/ \__/|___| |_| \___/   \__/|___/____|___| \_/ |_|\__/|_|\_|
    """)
    print('\n')
    wait_enter("Pressione ENTER para iniciar...")
    clear_screen()


######################################################################################################################################################################
def dia1():

    print(r""" 
      _____ _____            __ 
     |  __ \_   _|   /\     /_ |
     | |  | || |    /  \     | |
     | |  | || |   / /\ \    | |
     | |__| || |_ / ____ \   | |
     |_____/_____/_/    \_\  |_| """)
    time.sleep(2)
    clear_screen()

    type_text("[Dia 1] Sanidade: 100% | Anotações: 0", 0.02)
    print()
    time.sleep(0.5)

    type_text("Você acorda no seu quarto, a cabeça latejando.", 0.03)
    time.sleep(1)
    type_text("A tela do monitor pisca, iluminando o escuro.", 0.03)
    time.sleep(1)
    type_text("Uma nova mensagem aparece...", 0.03)
    time.sleep(1.2)
    wait_enter()
    clear_screen()

    # Chefe
    print(r"""    
                                                 .------.------.    
  +-------------+                     ___        |      |      |    
  |             |                     \ /]       |      |      |    
  |             |        _           _(_)        |      |      |    
  |             |     ___))         [  | \___    |      |      |    
  |             |     ) //o          | |     \   |      |      |    
  |             |  _ (_    >         | |      ]  |      |      |    
  |          __ | (O)  \__<          | | ____/   '------'------'    
  |         /  o| [/] /   \)        [__|/_                          
  |             | [\]|  ( \         __/___\_____                    
  |             | [/]|   \ \__  ___|            |                   
  |             | [\]|    \___%/%%/|____________|_____              
  |             | [/]|=====__   (_____________________)             
  |             | [\] \_____ \    |                  |              
  |             | [/========\ |   |                  |              
  |             | [\]     []| |   |                  |              
  |             | [/]     []| |_  |                  |              
  |             | [\]     []|___) |                  |             
====================================================================""")

    type_text("\nChefe: >>> Funcionário 023923_A, aqui é seu chefe.", 0.02); time.sleep(0.9)
    type_text("Chefe: >>> Você tem 7 dias para entregar o sistema de monitoramento definitivo.", 0.02); time.sleep(0.9)
    type_text("Chefe: >>> Quero o envio do relatório HOJE! Nada de desculpas, entendeu?", 0.02); time.sleep(0.9)
    type_text("Chefe: >>> Seu trabalho é simples: observar, registrar e me enviar tudo.", 0.02); time.sleep(1.0)
    wait_enter()
    clear_screen()

    # Câmeras do dia
    print(r"""     
              ,---------------------------,            
              |  /---------------------\  |            
              | |                       | |            
              | |                       | |
              | |                       | |            
              | |                       | |            
              | |                       | |            
              |  \_____________________/  |            
              |___________________________|            
            ,---\_____     []     _______/------,      
          /         /______________\           /|      
        /___________________________________ /  | ___  
        |                                   |   |    ) 
        |  _ _ _                 [-------]  |   |   (  
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/ 
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /            
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)

    type_text("\n[Câmeras disponíveis hoje: Recepção, Corredor 1, Sala TI]", 0.03)
    time.sleep(1)

    # --- Escolha da primeira câmera ---
    print("\nQual câmera você deseja observar?")
    print("(1) Recepção")
    print("(2) Corredor 1")
    print("(3) Sala TI")
    primeira = input("Escolha (1/2/3): ").strip()

    # Mostrar eventos da primeira câmera
    if primeira == "1":
        type_text("\n[Recepção]", 0.03)
        type_text("08:03 — Funcionário entra atrasado, crachá não reconhecido.", 0.02); time.sleep(0.8)
        type_text("08:15 — Visitante aguarda sozinho por 12 minutos. Nenhum registro.", 0.02); time.sleep(0.8)
        type_text("08:27 — A câmera sofre uma leve interferência estática.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) Funcionário atrasado")
        print("(2) Visitante sem registro")
        print("(3) Interferência estática")
        evento1 = input("Qual evento você quer anotar? ").strip()

    elif primeira == "2":
        type_text("\n[Corredor 1]", 0.03)
        type_text("15:14 — Lâmpada pisca 3 vezes antes de estabilizar.", 0.02); time.sleep(0.8)
        type_text("15:16 — Uma sombra atravessa o corredor, mas não há ninguém.", 0.02); time.sleep(0.8)
        type_text("15:20 — Som ambiente capta passos… mas o corredor está vazio.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) Oscilação de lâmpada")
        print("(2) Sombra misteriosa")
        print("(3) Passos sem origem")
        evento1 = input("Qual evento você quer anotar? ").strip()

    elif primeira == "3":
        type_text("\n[Sala TI]", 0.03)
        type_text("10:22 — PC-03 aparece ligado sem login de usuário.", 0.02); time.sleep(0.8)
        type_text("10:25 — O teclado do PC-03 pressiona teclas sozinho.", 0.02); time.sleep(0.8)
        type_text("10:30 — Tela mostra: 'VOCÊ ESTÁ VENDO?' e desliga.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) PC ligado sem login")
        print("(2) Teclas pressionadas sozinhas")
        print("(3) Mensagem estranha na tela")
        evento1 = input("Qual evento você quer anotar? ").strip()

    else:
        type_text("Opção inválida. Você perdeu tempo e não anotou nada.", 0.02)
        evento1 = None

    # --- Escolha da segunda câmera ---
    print("\nAgora escolha outra câmera para observar:")
    if primeira != "1":
        print("(1) Recepção")
    if primeira != "2":
        print("(2) Corredor 1")
    if primeira != "3":
        print("(3) Sala TI")

    segunda = input("Escolha: ").strip()

    # Mostrar eventos da segunda câmera
    if segunda == "1" and primeira != "1":
        type_text("\n[Recepção]", 0.03)
        type_text("08:03 — Funcionário entra atrasado, crachá não reconhecido.", 0.02); time.sleep(0.8)
        type_text("08:15 — Visitante aguarda sozinho por 12 minutos. Nenhum registro.", 0.02); time.sleep(0.8)
        type_text("08:27 — A câmera sofre uma leve interferência estática.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) Funcionário atrasado")
        print("(2) Visitante sem registro")
        print("(3) Interferência estática")
        evento2 = input("Qual evento você quer anotar? ").strip()

    elif segunda == "2" and primeira != "2":
        type_text("\n[Corredor 1]", 0.03)
        type_text("15:14 — Lâmpada pisca 3 vezes antes de estabilizar.", 0.02); time.sleep(0.8)
        type_text("15:16 — Uma sombra atravessa o corredor, mas não há ninguém.", 0.02); time.sleep(0.8)
        type_text("15:20 — Som ambiente capta passos… mas o corredor está vazio.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) Oscilação de lâmpada")
        print("(2) Sombra misteriosa")
        print("(3) Passos sem origem")
        evento2 = input("Qual evento você quer anotar? ").strip()

    elif segunda == "3" and primeira != "3":
        type_text("\n[Sala TI]", 0.03)
        type_text("10:22 — PC-03 aparece ligado sem login de usuário.", 0.02); time.sleep(0.8)
        type_text("10:25 — O teclado do PC-03 pressiona teclas sozinho.", 0.02); time.sleep(0.8)
        type_text("10:30 — Tela mostra: 'VOCÊ ESTÁ VENDO?' e desliga.", 0.02); time.sleep(0.8)
        print("\nEventos para anotar:")
        print("(1) PC ligado sem login")
        print("(2) Teclas pressionadas sozinhas")
        print("(3) Mensagem estranha na tela")
        evento2 = input("Qual evento você quer anotar? ").strip()

    else:
        type_text("Opção inválida. Você perdeu tempo e não anotou nada.", 0.02)
        evento2 = None

    # --- Relatório final ---
    type_text("\nAgora você deve fazer o relatório com os eventos anotados.", 0.03)
    print(f"✔ Primeiro evento anotado: {evento1}")
    print(f"✔ Segundo evento anotado: {evento2}")

    wait_enter()
    clear_screen()

    # === Depois vem a fala do chefe ===
    type_text("\nChefe: Muito bem... vamos analisar essas informações.", 0.03)

    # --- Noite ---
    type_text("Pouco antes de enviar o relatório, o telefone toca.", 0.03); time.sleep(0.8)
    clear_screen()
    
    type_text("Chefe: >>> O sensor do Corredor 1 está com falha. Vá AGORA e conserte pessoalmente.", 0.03); time.sleep(0.9)
    clear_screen()

    type_text("Você veste o casaco e sai de casa...", 0.03); time.sleep(0.8)
    type_text("Ao chegar à empresa, o corredor parece… mais longo do que deveria.", 0.03); time.sleep(0.9)
    type_text("As lâmpadas piscam enquanto você caminha, e uma porta no fundo se abre sozinha.", 0.03); time.sleep(1.0)

    wait_enter()
    clear_screen()

######################################################################################################################################################################
def dia2():


    print(r""" 
      _____ _____            ___  
     |  __ \_   _|   /\     |__ \ 
     | |  | || |    /  \       ) |
     | |  | || |   / /\ \     / / 
     | |__| || |_ / ____ \   / /_ 
     |_____/_____/_/    \_\ |____|""")
    time.sleep(2)
    clear_screen()

    type_text("[Dia 2] Sanidade: 90% | Anotações: 0", 0.02)
    print()
    time.sleep(0.5)

    type_text("Chefe: Primeiro dia foi fraco.", 0.02); time.sleep(0.6)
    type_text("Chefe: O cliente quer DETALHE. Capture tudo.", 0.02); time.sleep(0.6)
    type_text("Chefe: Se falhar, você vem de noite.", 0.02); time.sleep(0.8)
    wait_enter(); clear_screen()

    type_text("[Corredor 2]", 0.03)
    type_text("02:41 — Porta do Depósito abre (sem acesso registrado).", 0.02); time.sleep(0.8)
    type_text("02:41 — Ruído metálico contínuo por 17s.", 0.02); time.sleep(0.8)

    type_text("\nVocê tem que escolher o que registrar no relatório:", 0.03)
    print("\n1 - Registrar a porta abrindo sozinha.")
    print("2 - Registrar apenas o ruído metálico.")
    print("3 - Registrar ambos os eventos.")
    escolha1 = input("\nSua escolha: ")

    if escolha1 == "1":
        anotacao = "Você registra apenas a porta abrindo."
    elif escolha1 == "2":
        anotacao = "Você registra apenas o ruído metálico."
    elif escolha1 == "3":
        anotacao = "Você registra ambos os eventos (mais completo)."
    else:
        anotacao = "Confuso, você escreve um relatório malfeito."
    type_text(f"\n{anotacao}", 0.02)
    wait_enter(); clear_screen()

    type_text("[Escritório Norte]", 0.03)
    type_text("11:08 — Cadeira gira sozinha.", 0.02); time.sleep(0.8)
    type_text("11:09 — Monitor fica preto e pisca: 'ALGUÉM AÍ?' por 1s.", 0.02); time.sleep(0.8)

    type_text("\nVocê reage como?", 0.03)
    print("\n1 - Se aproxima da cadeira e do monitor.")
    print("2 - Apenas registra o evento e mantém distância.")
    print("3 - Desliga a câmera imediatamente.")
    escolha2 = input("\nSua escolha: ")

    if escolha2 == "1":
        evento2 = "Ao se aproximar, você sente o monitor quente, como se algo estivesse ali segundos atrás."
    elif escolha2 == "2":
        evento2 = "Você mantém distância, mas o monitor continua piscando 'ALGUÉM AÍ?' lentamente."
    elif escolha2 == "3":
        evento2 = "Você desliga a câmera, mas ao religá-la... a cadeira está virada para a tela."
    else:
        evento2 = "Você hesita demais, e a gravação falha sozinha."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    type_text("[Depósito]", 0.03)
    type_text("Time-lapse mostra uma caixa mudando de posição ao longo de 2h, sem ninguém.", 0.02); time.sleep(0.8)
    type_text("Pontos brancos aparecem na lente (poeira? olhos?).", 0.02); time.sleep(0.8)

    type_text("\nComo você interpreta os pontos brancos?", 0.03)
    print("\n1 - Poeira comum, nada estranho.")
    print("2 - Reflexo de alguma coisa.")
    print("3 - Olhos observando você.")
    escolha3 = input("\nSua escolha: ")

    if escolha3 == "1":
        interpretacao = "Você anota: 'anomalia descartada, poeira'."
    elif escolha3 == "2":
        interpretacao = "Você escreve: 'possível reflexo, precisa de revisão técnica'."
    elif escolha3 == "3":
        interpretacao = "Você registra: 'possível presença... múltiplos olhos'."
    else:
        interpretacao = "Você não escreve nada, apenas observa em silêncio."
    type_text(f"\n{interpretacao}", 0.02)
    wait_enter(); clear_screen()

    type_text("\nVocê envia o relatório do Dia 2.", 0.02); time.sleep(0.6)
    type_text("Mais tarde…", 0.03); time.sleep(0.8)
    type_text("No depósito, o ar é mais frio.", 0.03); time.sleep(0.6)
    type_text("As câmeras te mostram… de costas.", 0.03); time.sleep(0.6)
    type_text("Mas você está de frente.", 0.03)
    wait_enter(); clear_screen()

######################################################################################################################################################################
def dia3():

    print(r""" 
      _____ _____            ____  
     |  __ \_   _|   /\     |___ \ 
     | |  | || |    /  \      __) |
     | |  | || |   / /\ \    |__ \ 
     | |__| || |_ / ____ \   ___) |
     |_____/_____/_/    \_\ |____/ 
                               
                               """)
    time.sleep(2)
    clear_screen()

    type_text("[Dia 3] Sanidade: 85% | Anotações: 0", 0.02); print(); time.sleep(0.5)

    type_text("Chefe: O cliente gostou do 'tom realista'. Mantenha.", 0.02); time.sleep(0.6)
    type_text("Chefe: E pare de inventar sombra. Eu vejo tudo.", 0.02); time.sleep(0.8)
    wait_enter(); clear_screen()

    # --- Recepção ---
    type_text("[Recepção]", 0.03)
    type_text("12:00 — Telefone toca 3 vezes (sem chamada no log).", 0.02); time.sleep(0.8)
    type_text("Relógio da parede para por 8 minutos.", 0.02); time.sleep(0.8)

    type_text("\nVocê deve escolher o que registrar:", 0.03)
    print("\n1 - Registrar as 3 chamadas sem log.")
    print("2 - Registrar a parada do relógio por 8 minutos.")
    print("3 - Registrar ambos os eventos.")
    escolha1 = input("\nSua escolha: ").strip()

    if escolha1 == "1":
        evento1 = "Relatei: chamadas sem log (3 toques)."
    elif escolha1 == "2":
        evento1 = "Relatei: relógio parado por 8 minutos."
    elif escolha1 == "3":
        evento1 = "Relatei ambos os eventos com timestamps."
    else:
        evento1 = "Relatório inconsistente: escolha inválida."
    type_text(f"\n{evento1}", 0.02)
    wait_enter(); clear_screen()

    # --- Corredor 3 ---
    type_text("[Corredor 3]", 0.03)
    type_text("00:19 — Figura de terno parada no final do corredor.", 0.02); time.sleep(0.8)
    type_text("00:20 — A figura desaparece entre quadros.", 0.02); time.sleep(0.8)

    type_text("\nComo proceder?", 0.03)
    print("\n1 - Voltar o vídeo quadro a quadro.")
    print("2 - Aplicar zoom no fundo do corredor.")
    print("3 - Ignorar a imagem e focar no áudio ambiente.")
    escolha2 = input("\nSua escolha: ").strip()

    if escolha2 == "1":
        evento2 = "Revendo quadro a quadro: a figura some sem motion blur, como recorte limpo."
    elif escolha2 == "2":
        evento2 = "Com zoom, nota-se um crachá invertido pendendo do terno."
    elif escolha2 == "3":
        evento2 = "Focando no áudio: ruído de tecido e um sussurro abafado dizendo 'atrás'."
    else:
        evento2 = "Hesitação demais: a câmera entra em loop por 5 segundos."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    # --- Sala de Reunião ---
    type_text("[Sala de Reunião]", 0.03)
    type_text("Microfone capta sussurro: 'sete'.", 0.02); time.sleep(0.8)
    type_text("Projetor liga sozinho e projeta apenas uma moldura vazia.", 0.02); time.sleep(0.8)

    type_text("\nQual interpretação/ação você registra?", 0.03)
    print("\n1 - 'Sete' é ruído; descartar.")
    print("2 - Interferência elétrica entre microfone e projetor.")
    print("3 - Possível mensagem; anotar a palavra 'sete'.")
    print("4 - Perguntar em voz alta: 'sete o quê?' (teste de resposta).")
    escolha3 = input("\nSua escolha: ").strip()

    if escolha3 == "1":
        evento3 = "Marcado como ruído; o projetor apaga lentamente."
    elif escolha3 == "2":
        evento3 = "Anotado 'interferência potencial'; o projetor pisca duas vezes e fixa a moldura."
    elif escolha3 == "3":
        evento3 = "Registrado 'sussurro: sete'; o relógio marca 00:07 por 60s antes de voltar."
    elif escolha3 == "4":
        evento3 = "Após a pergunta, o microfone devolve sua respiração com 7 segundos de atraso."
    else:
        evento3 = "Sem ação; a moldura permanece até o auto-off."
    type_text(f"\n{evento3}", 0.02)
    wait_enter(); clear_screen()

    # --- Consolidação do Dia 3 ---
    type_text("\nVocê consolida o relatório do Dia 3.", 0.02); time.sleep(0.5)
    print(f"✔ Registro 1: {evento1}")
    print(f"✔ Registro 2: {evento2}")
    print(f"✔ Registro 3: {evento3}")

    wait_enter()
    clear_screen()

    # --- Noite ---
    type_text("\nNoite: Microfones reproduzem sua respiração antes de você chegar na sala.", 0.03); time.sleep(0.8)
    type_text("Você confere o VU do áudio ao vivo... ele se move sozinho, no seu padrão.", 0.03)
    wait_enter(); clear_screen()

######################################################################################################################################################################
def dia4():

    print(r""" 
       _____ _____            _  _   
     |  __ \_   _|   /\     | || |  
     | |  | || |    /  \    | || |_ 
     | |  | || |   / /\ \   |__   _|
     | |__| || |_ / ____ \     | |  
     |_____/_____/_/    \_\    |_|""")
    time.sleep(2)
    clear_screen()

    type_text("[Dia 4] Sanidade: 80% | Anotações: 0", 0.02); print(); time.sleep(0.5)

    type_text("Chefe: Atrasos no relatório irritam o cliente.", 0.02); time.sleep(0.6)
    type_text("Chefe: Quero timestamps precisos. Se faltar UMA linha, é noite.", 0.02); time.sleep(0.8)
    wait_enter(); clear_screen()

    # --- Corredor Principal ---
    type_text("[Corredor Principal]", 0.03)
    type_text("Silhueta refletida no piso sem corpo correspondente.", 0.02); time.sleep(0.8)
    type_text("Pisadas invertidas: começam onde deveriam terminar.", 0.02); time.sleep(0.8)

    type_text("\nO que você registra?", 0.03)
    print("\n1 - Somente a silhueta sem corpo.")
    print("2 - Somente as pegadas invertidas.")
    print("3 - Ambos com marcação de posição no mapa.")
    escolha1 = input("\nSua escolha: ").strip()

    if escolha1 == "1":
        evento1 = "Relatei a silhueta sem corpo; piso limpo e sem reflexos óbvios."
    elif escolha1 == "2":
        evento1 = "Relatei as pegadas invertidas; início e fim contraditórios."
    elif escolha1 == "3":
        evento1 = "Relatei ambos os fenômenos com croqui do corredor."
    else:
        evento1 = "Registro ambíguo; informação incompleta."
    type_text(f"\n{evento1}", 0.02)
    wait_enter(); clear_screen()

    # --- Sala TI ---
    type_text("[Sala TI]", 0.03)
    type_text("04:06 — Seu usuário aparece logado (você estava dormindo?).", 0.02); time.sleep(0.8)
    type_text("Terminal exibe: 'VOCÊ ESTÁ ME VENDO'.", 0.02); time.sleep(0.8)

    type_text("\nAção no terminal:", 0.03)
    print("\n1 - Deslogar imediatamente.")
    print("2 - Escrever 'Quem é você?'")
    print("3 - Desligar o PC pelo botão físico.")
    escolha2 = input("\nSua escolha: ").strip()

    if escolha2 == "1":
        evento2 = "Você tenta deslogar; sessão reaparece em 3s, sem senha."
    elif escolha2 == "2":
        evento2 = "Resposta no terminal: 'EU SEMPRE ESTIVE AQUI'."
    elif escolha2 == "3":
        evento2 = "Você desliga no botão; o monitor liga sozinho, já na tela de terminal."
    else:
        evento2 = "Sem ação; a mensagem permanece pulsando na tela."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    # --- Depósito ---
    type_text("[Depósito]", 0.03)
    type_text("Cadeado surge do lado de dentro.", 0.02); time.sleep(0.8)
    type_text("Etiqueta de caixa muda de 'A-13' para 'A-7'.", 0.02); time.sleep(0.8)

    type_text("\nComo você lida com o cadeado e a etiqueta?", 0.03)
    print("\n1 - Fotografar e catalogar a mudança de 'A-13' para 'A-7'.")
    print("2 - Tentar forçar o cadeado.")
    print("3 - Manter distância e apenas registrar o horário.")
    escolha3 = input("\nSua escolha: ").strip()

    if escolha3 == "1":
        evento3 = "Fotos salvas; metadados mostram hora adiantada em 7 minutos."
    elif escolha3 == "2":
        evento3 = "O cadeado 'do lado de dentro' não cede; alguém chacoalha a caixa atrás da câmera."
    elif escolha3 == "3":
        evento3 = "Registro frio; ruído metálico volta a ocorrer por 7 segundos."
    else:
        evento3 = "Anotação falha; câmera perde foco por 7 segundos."
    type_text(f"\n{evento3}", 0.02)
    wait_enter(); clear_screen()

    # --- Consolidação do Dia 4 ---
    type_text("\nVocê consolida o relatório do Dia 4.", 0.02); time.sleep(0.5)
    print(f"✔ Registro 1: {evento1}")
    print(f"✔ Registro 2: {evento2}")
    print(f"✔ Registro 3: {evento3}")

    wait_enter()
    clear_screen()

    # --- Noite ---
    type_text("\nNoite: Os monitores mostram sua mesa, mas há duas cadeiras. Uma vazia, balançando.", 0.03); time.sleep(0.8)
    wait_enter(); clear_screen()

######################################################################################################################################################################
def dia5():

    print(r""" 
       _____ _____            _____ 
     |  __ \_   _|   /\     | ____|
     | |  | || |    /  \    | |__  
     | |  | || |   / /\ \   |___ \ 
     | |__| || |_ / ____ \   ___) |
     |_____/_____/_/    \_\ |____/ """)
    time.sleep(2)
    clear_screen()

    type_text("[Dia 5] Sanidade: 70% | Anotações: 0", 0.02); print(); time.sleep(0.5)

    type_text("Chefe: O cliente quer cross-check com logs.", 0.02); time.sleep(0.6)
    type_text("Chefe: Não me traga mito urbano.", 0.02); time.sleep(0.8)
    wait_enter(); clear_screen()

    # --- Recepção ---
    type_text("[Recepção]", 0.03)
    type_text("Registro marca 07:00, mas a imagem mostra vazio até 07:12.", 0.02); time.sleep(0.8)
    type_text("Planta ao fundo murcha em um time-lapse de 30s.", 0.02); time.sleep(0.8)

    type_text("\nComo registrar o descompasso?", 0.03)
    print("\n1 - Assumir erro de relógio da câmera.")
    print("2 - Concluir adulteração de log.")
    print("3 - Registrar sem hipótese, apenas dados e prints.")
    escolha1 = input("\nSua escolha: ").strip()

    if escolha1 == "1":
        evento1 = "Hipótese: drift de relógio; solicitar NTP audit."
    elif escolha1 == "2":
        evento1 = "Hipótese: adulteração; marcar como incidente de segurança."
    elif escolha1 == "3":
        evento1 = "Registro neutro com evidências; sem conclusão."
    else:
        evento1 = "Relato dúbio; falta de padronização nos horários."
    type_text(f"\n{evento1}", 0.02)
    wait_enter(); clear_screen()

    # --- Escritório Sul ---
    type_text("[Escritório Sul]", 0.03)
    type_text("Teclas digitam: 'NÃO DURMA'.", 0.02); time.sleep(0.8)
    type_text("Webcam liga sem LED.", 0.02); time.sleep(0.8)

    type_text("\nSua resposta à mensagem:", 0.03)
    print("\n1 - Ignorar e apenas gravar as teclas.")
    print("2 - Responder no teclado: 'Quem está aí?'")
    print("3 - Cobrir a webcam e desconectar o cabo.")
    escolha2 = input("\nSua escolha: ").strip()

    if escolha2 == "1":
        evento2 = "A frase se repete 7 vezes; a última linha sai invertida."
    elif escolha2 == "2":
        evento2 = "Resposta: 'VOCÊ'. A webcam acompanha seu movimento sem LED."
    elif escolha2 == "3":
        evento2 = "Webcam coberta; no feed da câmera, você aparece de olhos abertos, sem piscar."
    else:
        evento2 = "Teclas batem sozinhas; o teclado esquenta."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    # --- Corredor 2 ---
    type_text("[Corredor 2]", 0.03)
    type_text("22:22 — Luz estoura (clarão).", 0.02); time.sleep(0.8)
    type_text("A sombra permanece 0,5s depois do clarão.", 0.02); time.sleep(0.8)

    type_text("\nO que priorizar no relatório?", 0.03)
    print("\n1 - Fotogramas antes e depois do clarão.")
    print("2 - Análise do rastro de sombra persistente.")
    print("3 - Captura de áudio sincronizada com o estalo da lâmpada.")
    escolha3 = input("\nSua escolha: ").strip()

    if escolha3 == "1":
        evento3 = "Frames exportados; EXIF perde 2 segundos no pico do clarão."
    elif escolha3 == "2":
        evento3 = "Mede 0,5s de persistência; contorno lembra a sua própria silhueta."
    elif escolha3 == "3":
        evento3 = "Áudio pega estalo + uma respiração longa, fora de compasso."
    else:
        evento3 = "Prioridade indefinida; relatório pouco conclusivo."
    type_text(f"\n{evento3}", 0.02)
    wait_enter(); clear_screen()

    # --- Consolidação do Dia 5 ---
    type_text("\nVocê consolida o relatório do Dia 5.", 0.02); time.sleep(0.5)
    print(f"✔ Registro 1: {evento1}")
    print(f"✔ Registro 2: {evento2}")
    print(f"✔ Registro 3: {evento3}")

    wait_enter()
    clear_screen()

    # --- Noite ---
    type_text("\nNoite: Você confere o Escritório Sul. O teclado ainda está quente.", 0.03); time.sleep(0.8)
    wait_enter(); clear_screen()

######################################################################################################################################################################
def dia6():

    print(r""" 
      _____ _____              __  
     |  __ \_   _|   /\       / /  
     | |  | || |    /  \     / /_  
     | |  | || |   / /\ \   | '_ \ 
     | |__| || |_ / ____ \  | (_) |
     |_____/_____/_/    \_\  \___/ """)
    time.sleep(2)
    clear_screen()

    type_text("[Dia 6] Sanidade: 60% | Anotações: 0", 0.02); print(); time.sleep(0.5)

    type_text("Chefe: Amanhã é a entrega. Hoje, perfeição. Sem falhas.", 0.02); time.sleep(0.9)
    wait_enter(); clear_screen()

    # --- Corredor 1 ---
    type_text("[Corredor 1]", 0.03)
    type_text("01:01 — Porta tranca sozinha.", 0.02); time.sleep(0.8)
    type_text("Câmera vira 3 graus sem comando.", 0.02); time.sleep(0.8)

    type_text("\nAção técnica:", 0.03)
    print("\n1 - Recalibrar a PTZ (pan/tilt/zoom).")
    print("2 - Revisar permissões de controle remoto.")
    print("3 - Desligar a alimentação e religar (ciclo de energia).")
    escolha1 = input("\nSua escolha: ").strip()

    if escolha1 == "1":
        evento1 = "Calibração aceita; minutos depois, a câmera se 'desalinha' para o mesmo ângulo."
    elif escolha1 == "2":
        evento1 = "Permissões ok; log mostra comando vindo do seu próprio usuário."
    elif escolha1 == "3":
        evento1 = "Power cycle feito; a câmera religa já com 3 graus desviada."
    else:
        evento1 = "Sem ação; o desvio se acentua para 7 graus."
    type_text(f"\n{evento1}", 0.02)
    wait_enter(); clear_screen()

    # --- Sala de Reunião ---
    type_text("[Sala de Reunião]", 0.03)
    type_text("Tela projeta 'DIA 7' por 0,7s.", 0.02); time.sleep(0.8)
    type_text("Cadeiras alinhadas formam 'VII'.", 0.02); time.sleep(0.8)

    type_text("\nComo registrar o prenúncio?", 0.03)
    print("\n1 - Fotografar a projeção e as cadeiras, anexar no relatório.")
    print("2 - Reorganizar as cadeiras para quebrar o 'VII'.")
    print("3 - Ficar parado e ver se a projeção se repete.")
    escolha2 = input("\nSua escolha: ").strip()

    if escolha2 == "1":
        evento2 = "Imagens salvas; metadados mostram data do dia seguinte."
    elif escolha2 == "2":
        evento2 = "Você muda as cadeiras; em 10s voltam ao 'VII' sozinhas."
    elif escolha2 == "3":
        evento2 = "A projeção retorna 7 vezes, cada vez mais clara."
    else:
        evento2 = "Sem decisão; a sala mantém um zumbido baixo e constante."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    # --- Depósito ---
    type_text("[Depósito]", 0.03)
    type_text("Caixas formam um corredor estreito (não estavam assim).", 0.02); time.sleep(0.8)
    type_text("Movimento é detectado atrás da câmera.", 0.02); time.sleep(0.8)

    type_text("\nQual procedimento seguir?", 0.03)
    print("\n1 - Percorrer o 'corredor de caixas' lentamente.")
    print("2 - Chamar reforço (mesmo sabendo que não vem).")
    print("3 - Travar a câmera e registrar somente o sensor de movimento.")
    escolha3 = input("\nSua escolha: ").strip()

    if escolha3 == "1":
        evento3 = "Você avança; o corredor parece mais longo do que o espaço físico permite."
    elif escolha3 == "2":
        evento3 = "Sem resposta no rádio; microfone capta passos sincronizados com os seus, mas atrasados 7s."
    elif escolha3 == "3":
        evento3 = "Sensor ativa repetidamente; log salva eventos sem imagem associada."
    else:
        evento3 = "Você congela; a câmera detecta presença exatamente atrás da lente."
    type_text(f"\n{evento3}", 0.02)
    wait_enter(); clear_screen()

    # --- Consolidação do Dia 6 ---
    type_text("\nVocê consolida o relatório do Dia 6.", 0.02); time.sleep(0.5)
    print(f"✔ Registro 1: {evento1}")
    print(f"✔ Registro 2: {evento2}")
    print(f"✔ Registro 3: {evento3}")

    wait_enter()
    clear_screen()

    # --- Noite ---
    type_text("\nNoite: No depósito, o corredor de caixas parece levar para dentro da própria tela.", 0.03); time.sleep(0.8)
    wait_enter(); clear_screen()

######################################################################################################################################################################
def dia7():

    print(r""" 
      _____ _____            ______ 
     |  __ \_   _|   /\     |____  |
     | |  | || |    /  \        / / 
     | |  | || |   / /\ \      / /  
     | |__| || |_ / ____ \    / /   
     |_____/_____/_/    \_\  /_/ """)
    time.sleep(2)
    clear_screen()

    type_text("[Dia 7] Sanidade: 50% | Anotações: 0", 0.02); print(); time.sleep(0.5)

    type_text("Chefe: Último dia. Se não entregar, está fora. Estou assistindo.", 0.02); time.sleep(1.0)
    wait_enter(); clear_screen()

    # --- Todas as Câmeras ---
    type_text("[TODAS AS CÂMERAS]", 0.03)
    type_text("Sua imagem aparece em todas as telas, em ângulos impossíveis.", 0.02); time.sleep(1.0)
    type_text("Texto final surge no centro: 'VOCÊ É O ALVO'.", 0.03); time.sleep(1.0)

    type_text("\nComo proceder diante das telas?", 0.03)
    print("\n1 - Desligar todas as câmeras pelo software.")
    print("2 - Cobrir as telas e respirar fundo.")
    print("3 - Falar em voz alta: 'Isso não é real'.")
    escolha1 = input("\nSua escolha: ").strip()

    if escolha1 == "1":
        evento1 = "As telas apagam... e voltam sozinhas, mostrando você de costas."
    elif escolha1 == "2":
        evento1 = "Mesmo cobertas, você sente olhares; um coro sussurra seu nome."
    elif escolha1 == "3":
        evento1 = "O áudio retorna sua frase com eco de 7 segundos, em vozes diferentes."
    else:
        evento1 = "Sem reação; as imagens se multiplicam, ocupando todos os monitores."
    type_text(f"\n{evento1}", 0.02)
    wait_enter(); clear_screen()

    # --- Sala de Reunião (Clímax) ---
    type_text("[Sala de Reunião]", 0.03)
    type_text("As cadeiras formam 'VII'. A projeção não desliga.", 0.02); time.sleep(0.8)
    type_text("No vidro, reflexos mostram pessoas que você não conhece, todas olhando para você.", 0.02); time.sleep(0.8)

    type_text("\nSua última tentativa de controle:", 0.03)
    print("\n1 - Enviar o relatório final mesmo assim.")
    print("2 - Pedir ajuda ao chefe pelo rádio.")
    print("3 - Rezar em silêncio.")
    escolha2 = input("\nSua escolha: ").strip()

    if escolha2 == "1":
        evento2 = "Você envia; retorno automático: 'RELATÓRIO ACEITO. VOCÊ CONCLUÍU O PROCESSO'."
    elif escolha2 == "2":
        evento2 = "Rádio chia; a voz do chefe responde: 'Se não consegue viver com isso, termine.'"
    elif escolha2 == "3":
        evento2 = "O zumbido cessa por um segundo... e volta mais alto."
    else:
        evento2 = "Sem envio, sem pedido; a sala fica mais fria."
    type_text(f"\n{evento2}", 0.02)
    wait_enter(); clear_screen()

    # --- Encerramento ---
    type_text("\nSeu corpo cede. As vozes encobrem seus próprios pensamentos.", 0.03); time.sleep(0.8)
    type_text("Você caminha até a sala de segurança, trêmulo, e a gravação continua rodando.", 0.03); time.sleep(0.9)
    type_text("As luzes piscam. O sistema registra seu último movimento.", 0.03); time.sleep(1.0)

    # Final trágico (sem detalhes gráficos)
    type_text("\n[Registro Final] Você decide encerrar a dor. A gravação termina ali.", 0.03); time.sleep(1.0)
    type_text("PROCESSO TERMINADO.", 0.04)

    wait_enter("\n[ENTER] encerrar...")
    clear_screen()

def main():
    splash()
    dia1()
    dia2()
    dia3()
    dia4()
    dia5()
    dia6()
    dia7()

if __name__ == "__main__":
    main()