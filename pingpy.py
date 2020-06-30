import os, re, sys
bons = 0
ruins = 0
ip = input('Digite o IP ou URL: ')
#ip = sys.argv[1] # Digite o IP na frente do comando
tempo = float(input('Digite o tempo ideal de resposta em milissegundos(ms): '))
quant = int(input('Digite a quantidade de ping que deseja: ' ))

print('Verificando conexão...\n')
cmd = 'ping -c' + str(quant) + ' ' + ip
r = '' .join(os.popen(cmd) .readlines())
r = r.split('\n')
ipvx = r[1].split()
#print(len(ipvx))
if len(ipvx) == 8:
    if re.search('64 bytes', r[1]):
        for c in range(1,quant+1):
            #print('Link UP')
            if re.search('64 bytes', r[c]):
                time = r[c].split()
                time2 = time[6].split('=')
                #print(float(time2[1]))
                if float(time2[1]) <= tempo:
                    print('\033[32m{}\033[m'.format(r[c]))
                    bons += 1
                elif float(time2[1]) > tempo:
                    print('\033[31m{}\033[m'.format(r[c]))
                    ruins += 1
                else:
                    print(r[c])
    else:
        print('Link Down')
elif len(ipvx) == 9:
    if re.search('64 bytes', r[1]):
        for c in range(1,quant+1):
            #print('Link UP')
            if re.search('64 bytes', r[c]):
                time = r[c].split()
                time2 = time[7].split('=')
                #print(float(time2[1]))
                if float(time2[1]) <= tempo:
                    print('\033[32m{}\033[m'.format(r[c]))
                    bons += 1
                elif float(time2[1]) > tempo:
                    print('\033[31m{}\033[m'.format(r[c]))
                    ruins += 1
                else:
                    print(r[c])
    else:
        print('Link Down')

print('\nPings abaixo de {}ms = {}'.format(tempo, bons))
print('Pings acima de {}ms = {}'.format(tempo,ruins))
