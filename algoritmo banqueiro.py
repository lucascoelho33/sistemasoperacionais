def main():
	E = [4, 2, 3, 1]
	disponiveis = [2, 1, 0, 0]

	processos = [
					{"finalizado" : False, "alocados" : [0, 0, 1, 0], "requisitados" : [2, 0, 0, 1]},
					{"finalizado" : False, "alocados" : [2, 0, 0, 1], "requisitados" : [1, 0, 0, 0]},
					{"finalizado" : False, "alocados" : [0, 1, 2, 0], "requisitados" : [2, 1, 0, 1]}
				]

	dead = False
	tamanho = len(E)
	while not dead:
		dead = True
		for processo in processos:
			inDead = False

			if processo["finalizado"] == True:
				continue

			for i in range(tamanho):
				if (processo['requisitados'][i] > disponiveis[i]):
					inDead = True
					break

			if not inDead:
				disponiveis = [disponiveis[j] + processo["alocados"][j] for j in range(tamanho)]
				processo["finalizado"] = True
				dead = False

	for i in range(len(processos)):
		if processos[i]["finalizado"] == True:
			print ("Processo%d: finalizado." % (i+1))
		else:
			print ("Processo%d: DeadLock." % (i+1))


if __name__ == '__main__':
	main()
