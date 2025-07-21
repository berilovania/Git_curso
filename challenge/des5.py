frutas = ['maca', 'banana', 'manga', 'uva']
print('Lista de frutas:', frutas)
frutas.insert(2, 'laranja')
frutas.remove('manga')
del frutas[-1]
print('Lista de frutas após modificações:', frutas)
print('Quantidade de frutas na lista:', len(frutas))
print('Primeira fruta:', frutas[0])
print('ultima fruta:', frutas[-1])