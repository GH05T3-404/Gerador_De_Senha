import random

# Caracteres usados para formar senhas #
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '#@$%&*-=+/.'

# Agrupa todos os caracteres #
all = lower + upper + numbers + symbols

# Define tamanho da senha #
length = int(input("""quantas características ? (limite 73)
-> """))

# Gera senha #
password = "".join(random.sample(all, length))

# Mostra resultado #
print(f"\n{password}")