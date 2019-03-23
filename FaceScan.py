#!/usr/bin/env python
import os, time, requests
import webbrowser
def frase():
    print("""
  █████▒ ██████  ▄████▄   ▄▄▄       ███▄    █ 
▓██   ▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
▒████ ░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▒  ░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒█░   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░     ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░   ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
             ░  ░ ░            ░  ░         ░                             
""")

frase()

print("""
*--------------*    
  Escolha
*--------------*

 *--------------*
 * [1] SCAN     *
 * [2] HELP     *
 *--------------*

""")
try:
    escolha = int(input('>>> '))
    while escolha != 1 and escolha != 2 and escolha != 3:
        escolha = int(input('>>> '))
    if escolha == 1:
        time.sleep(2)
        id_ = str(input('[ID] '))
        if len(id_) == 15:
            arq = input('[+]Nome do arquivo : ')
            if '.txt' not in arq:
                print('[!] Faltando .TXT ')
                exit()
            print('[!]O scan sera salvo no arquivo %s '%(arq))
            time.sleep(3)
            scan = open(arq,'w')
            scan.write('   [!]LIKE[!]  '+'\n')
            scan.write('       [.]Fotos curtidas por ele(a) :  https://www.facebook.com/search/'+id_+'/photos-liked/'+'\n')
            scan.write('       [.]Vídeos curtidos por ele(a) :  https://www.facebook.com/search/'+id_+'/videos-liked/intersect'+'\n')
            scan.write('       [.]Post curtido  : https://www.facebook.com/search/'+id_+'/stories-liked/intersect/'+'\n')
            scan.write('   [!]AMIGOS/FAMILIA[!] '+'\n')
            scan.write('       [.]Amigos dele (a) : https://www.facebook.com/search/'+id_+'/friends/'+'\n')
            scan.write('       [.]Família : https://www.facebook.com/search/'+id_+'/relatives/intersect/'+'\n')
            scan.write('   [!]COMENTÁRIO[!]  '+'\n')
            scan.write('       [.]Fotos comentadas por ele(a) : https://www.facebook.com/search/'+id_+'/photos-commented/intersect/    '+'\n')
            scan.write('   [!]PERFIL[!] '+'\n')
            scan.write('       [.]Grupos dele(a) : https://www.facebook.com/search/'+id_+'/groups/ '+'\n')
            scan.write('       [.]Fotos dele(a) : https://www.facebook.com/search/'+id_+'/photos-by/  '+'\n')
            scan.write('       [.]Videos dele(a) : https://www.facebook.com/search/'+id_+'/videos-by/'+'\n')
            scan.write('       [.]Post : https://www.facebook.com/search/'+id_+'/stories-by/'+'\n')
            scan.write('   [!]INTERESSE[!] '+'\n')
            scan.write('       [.]Páginas : https://www.facebook.com/search/'+id_+'/pages-liked/intersect/'+'\n')
            scan.write('       [.]Locais Visitados : https://www.facebook.com/search/'+id_+'/places-visited/'+'\n')
            scan.write('       [.]Música : https://www.facebook.com/search/'+id_+'/photos-liked/musician/pages/intersect/'+'\n')
            scan.write('       [.]Fotos comentadas por ele(a) : https://www.facebook.com/search/'+id_+'/photos-commented/'+'\n')
            scan.write('   [!]MARCAÇÕES[!] '+'\n')
            scan.write('       [.]Fotos que foi marcado : https://www.facebook.com/search/'+id_+'/photos-of/intersect/'+'\n')
            scan.write('       [.]Videos que foi marcado: https://www.facebook.com/search/'+id_+'/videos-of/intersect/'+'\n')
            time.sleep(2)
            print('\n')
            print('[+]SALVO EM : ',os.getcwd())
            print('[+]SCAN FINALIZADO...')
            time.sleep(0.8)
            print('ABRINDO ...')
            try:
                webbrowser.open(arq)
            except:
                print('[-]Erro ao abrir')
                exit()

        else:
            print('[-]Verifique o ID novamente.')
    elif escolha == 2:
        print("""\n
********************************************************
*-------------------------HELP-------------------------*
********************************************************

- O script funciona na base de ID, sem requisiçoes, apenas link.
- Como pegar um ID?
-  [1] Entre em uma url de um perfil.
-  [2] Abra uma imagem de perfil do alvo.
-  [3] Voce verá varias cadeias de números.
-  [4] A última cadeia é o ID
-  https://www.facebook.com/photo.php?fbid=325192194604475&set=a.133996233724073.1073741827.xxxxxxxxxxxxxxx&type=3&theater
-  => O 'x' é o ID
- O id é composto por 15 números.

********************************************************
*-------------------------HELP-------------------------*
********************************************************
""")
except KeyboardInterrupt:
    print('\n[-]Saindo..')
except ValueError:
    print('\n[-]Insira um valor correto.')
    









