# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input('Qual seu nome?')
total_dias = input ('Quantos dias por semana você estuda?')
total_horas = input ('Quantas horas você estuda por dia?')
curso = input ('Para qual curso você está estudando?')
#tudo isso foi vai ser armazenado em forma de string. Precisamos converter em variável inteira
total_dias = int(total_dias)
total_horas = int (total_horas)
total_semanal = total_dias*total_horas
print (format 'Olá', (nome)', você estuda' total_dias ' por mais ou menos' total_horas 'Isso significa que você estuda' total_semanal ' para o curso de' curso)

