## Nº 1
#f = open('texto.txt', 'w')
#f.write("Hello World!")
#
#f.close()

## Nº 2
#f = open('texto.txt', 'r')
#print(f.read())
#
#f.close()

## Nº 3
#counter = 0
#f = open('texto.txt', 'r')
#
#for l in f.readlines():
#    counter = counter + 1
#
#print(counter)

## Nº 4
#f = open('texto.txt', 'r')
#fc = open('copia.txt', 'w')
#fc.writelines(f.readlines())
#fc = open('textocopy.txt', 'r')
#print(fc.read())

## Nº 5
#f = open('texto.txt', 'r')
#fc = open('copia.txt', 'r')
#fcom = open('combinado.txt', 'w')
#fcom.writelines(f.readlines() + fc.readlines())
#fcom = open('combinado.txt', 'r')
#print(fcom.read())

## Nº 6
#f = open('texto.txt', 'r')
#fr = f.read()
#
#words = fr.split()
#word_count = len(words)   
#print(word_count)

## Nº 7
#for i in words:
#    if i == "World":
#        i = "Python"
#
#a = " ".join(words)
#m = open('modificado.txt', 'w')
#m = m.writelines(a)
#m = open('modificado.txt', 'r')
#print(m.read())

## Nº 8
#f = open('texto.txt', 'a')
#f.write("\nIsso é incrível!")
#f.close()

## Nº 9
#f = open('texto.txt', 'r')
#content = f.read()
#f.close()
#
#letters = [c for c in content if c.isalpha()]
#print("Total de letras:", len(letters))

## Nº 10
#f = open('numeros.txt', 'r')
#nums = f.read().split(",")
#f.close()
#
#soma = sum(int(n) for n in nums)
#print("Soma:", soma)

## Nº 11
#def is_valid_ip(ip):
#    parts = ip.split(".")
#    if len(parts) != 4:
#        return False
#    for p in parts:
#        if not p.isdigit():
#            return False
#        n = int(p)
#        if n < 0 or n > 255:
#            return False
#    return True
#
#f = open('ips.txt', 'r')
#ips = [line.strip() for line in f.readlines()]
#f.close()
#
#validos = [ip for ip in ips if is_valid_ip(ip)]
#invalidos = [ip for ip in ips if not is_valid_ip(ip)]
#
#out = open('relatorio_ips.txt', 'w')
#out.write("[Endereços válidos:]\n")
#out.writelines(ip + "\n" for ip in validos)
#out.write("\n[Endereços inválidos:]\n")
#out.writelines(ip + "\n" for ip in invalidos)
#out.close()

## Nº 12
#def bytes_to_mb(b):
#    return b / (1024 * 1024)
#
#def percent(part, total):
#    return (part / total) * 100
#
#f = open('usuarios.txt', 'r')
#users = []
#for line in f:
#    name = line[:15].strip()
#    size = int(line[15:].strip())
#    users.append((name, size))
#f.close()
#
#total = sum(s for _, s in users)
#report = []
#for i, (name, size) in enumerate(users, start=1):
#    mb = bytes_to_mb(size)
#    perc = percent(size, total)
#    report.append(f"{i:<4} {name:<15} {mb:10.2f} MB {perc:10.2f}%")
#
#out = open('relatorio.txt', 'w')
#out.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
#out.write("------------------------------------------------------------------------\n")
#out.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")
#out.write("\n".join(report))
#out.write(f"\n\nEspaço total ocupado: {bytes_to_mb(total):.2f} MB")
#out.write(f"\nEspaço médio ocupado: {bytes_to_mb(total/len(users)):.2f} MB")
#out.close()

## Nº 13
#MAX_LINE = 76
#MAX_PAGE = 60
#
#filename = "texto.txt"
#f = open(filename, "r")
#lines = f.readlines()
#f.close()
#
#out = open("paginado.txt", "w")
#page = 1
#count = 0
#
#for line in lines:
#    while len(line) > MAX_LINE:
#        out.write(line[:MAX_LINE] + "\n")
#        line = line[MAX_LINE:]
#        count += 1
#        if count == MAX_PAGE:
#            out.write(f"\nPágina {page} - {filename}\n\n")
#            page += 1
#            count = 0
#    out.write(line)
#    count += 1
#    if count == MAX_PAGE:
#        out.write(f"\nPágina {page} - {filename}\n\n")
#        page += 1
#        count = 0
#
#if count > 0:
#    out.write(f"\nPágina {page} - {filename}\n")
#out.close()

## Nº 14
#import re
#
#f = open('texto.txt', 'r')
#lines = f.readlines()
#f.close()
#
#new_lines = []
#prev_blank = False
#for line in lines:
#    # remove múltiplos espaços
#    line = re.sub(r'\s+', ' ', line).strip()
#    if line == "":
#        if prev_blank:
#            continue
#        prev_blank = True
#    else:
#        prev_blank = False
#    new_lines.append(line + "\n")
#
#out = open('limpo.txt', 'w')
#out.writelines(new_lines)
#out.close()
