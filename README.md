# Example_manipulation_with_database_in_Python

1. O trabalho consiste em desenvolver uma aplicação em Python que
faça uma ligação entre um Banco de Dados e arquivos de texto.
Obs.: Toda manipulação dos dados no banco deverão ser feitas via
código.

2. Pontos principais do trabalho:
* Criar um Banco de Dados com as seguintes tabelas:

	> Pessoa 
 
	|      CPF      | Primeiro nome | Nome do meio  |    Sobrenome  |    Idade     |     Conta     |
	| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
	|     ...       |      ...      |      ...      |      ...      |     ...      |      ...      |     


	> Conta

	|   Agência     |    Número     |     Saldo     |    Gerente    |    Idade     |    Titular    |
	| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
	|     ...       |      ...      |      ...      |      ...      |     ...      |      ...      | 


* Preencher as tabelas a partir de um arquivo .txt
	- Os arquivos nome e conta estarão disponibilizados.
	- O programa terá de substituir os espaços por vírgulas.
* Permitir adição, remoção e edição de qualquer linha do banco.
* Realizar consultas no banco de dados e guardar o resultado em
novos arquivos de texto.
o Organizar as consultas por tipo em pastas diferentes (ex.:
consulta por nome, por saldo, por idade, etc.).
o Caso a pasta não exista, criar uma nova.
* ler e imprimir os resultados das consultas através dos
arquivos criados.
