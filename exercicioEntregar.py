alunos = []
alunos.append(
    {'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1': 8})
alunos.append(
    {'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 06', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 07', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 08', 'curso': 'Ciências da Computação', 'AV1': 10})
alunos.append(
    {'nome': 'Aluno 09', 'curso': 'Ciências da Computação', 'AV1': 10})
alunos.append(
    {'nome': 'Aluno 10', 'curso': 'Ciências da Computação', 'AV1': 4})
alunos.append(
    {'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 5})
alunos.append(
    {'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 5})
alunos.append(
    {'nome': 'Aluno 12', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 13', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 14', 'curso': 'Ciências da Computação', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 15', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 16', 'curso': 'Ciências da Computação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 17', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 8})
alunos.append(
    {'nome': 'Aluno 18', 'curso': 'Ciências da Computação', 'AV1': 4})
alunos.append(
    {'nome': 'Aluno 19', 'curso': 'Sistemas de Informação', 'AV1': 2})
alunos.append(
    {'nome': 'Aluno 20', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})

cursos = {}
listNotas = []

for aluno in alunos:

    # print('--------------------------')

    for key, value in aluno.items():
        # print(key, value)
        if key == 'curso':
            cursos.update({value: listNotas})
            # print(cursos)
for curso in cursos:
    listNotas = []
    for aluno in alunos:
        for key, value in aluno.items():
            if value == curso:
                print('aqui', curso)
                listNotas.append(aluno.get('AV1'))
                print(listNotas)
    cursos.update({curso: listNotas})
    # print(cursos)
for curso in cursos:
  notaDeUmCurso = cursos.get(curso)
  tamanho = len(notaDeUmCurso)
  media = 0 
  print('Curso...: ',curso)
  print(notaDeUmCurso)

  maior = menor = notaDeUmCurso[0]
  for i in range(0, tamanho):
    media += notaDeUmCurso[i]
    if notaDeUmCurso[i] > maior:
      maior = notaDeUmCurso[i]
    if notaDeUmCurso[i] < menor:  
      menor = notaDeUmCurso[i]
      mediaPorDiciplina = media / tamanho

  print('A MENOR nota é: ', menor)
  print('A MAIOR nota é: ', maior)
  print(f'A Média: {mediaPorDiciplina :.2f}')
  print('--------------------------')
