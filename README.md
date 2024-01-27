# Exemplo de Uso da API do Google Sheets

## Introdução

O projeto é basicamente uma automação de uma planilha do google sheets com intuito de atualizar as situações dos alunos em uma escola calculando automaticamente suas médias, porcentagem de faltas e classificando a situação que estejam, sejam elas: Reprovado por Nota, Exame Final, Aprovado ou Reprovado por faltas. Os métodos utilizados no projeto são de escrita e leitura de dados da planilha.

## Exemplo Utilizado

Nesse exemplo utilizarei a planilha [Engenharia de Software](https://docs.google.com/spreadsheets/d/1TZwVaYCUX_JtLQWNzr-PXib2xQZKzltdCejzr8io4k0/edit?usp=sharing). Copie a planilha e salve em alguma pasta na conta de seu google drive para que possa executar o projeto. Lembre-se de deixá-la pública, para isso clique em compartilhar e mudo o acesso para qualquer pessoas com link possa editar no arquivo.

- A planilha provavelmente aparecerá desta maneira:

<div style="display: flex; justify-content: center;">
    <img src="./img/spreadsheet.png" alt="Imagem do Hinata" height=400 style="">
</div>

## Configuração e Instalação




Para que consiga executar o projeto utilize os comandos:

- `pip install pandas`
- `pip install gspread`

Além dessas foram utilizadas as bibliotecas : `os` e `math` que são built-in.

Depois de instalar as biblioteca, já é possível fazer requisições GET, no entanto para fazer requisições POST é preciso de um token específico gerado [Console Google Cloud](https://console.cloud.google.com/welcome?project=velvety-column-412417) em sua conta. Para isso siga os passos a seguir:

### 1. Abra a Página do [Console Google Cloud](https://console.cloud.google.com/welcome?project=velvety-column-412417):

<div style="display: flex; justify-content: center;">
    <img src="./img/passo-1.jpeg" alt="Imagem do Hinata" height=400 style="">
</div>

### 2. Crie um projeto:

<div style="display: flex; justify-content: center;">
    <img src="./img/passo-2.jpeg" alt="Imagem do Hinata" height=400 style="">
</div>


### 3. Ative o IAM e Admin do projeto:

<div style="display: flex; justify-content: center;">
    <img src="./img/passo-3.jpeg" alt="Imagem do Hinata" height=400 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-4.jpeg" alt="Imagem do Hinata" height=400 style="">
</div>



### 4. Crie uma conta de serviço:

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-5.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-6.jpeg" alt="Imagem do Hinata" height=500 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-7.jpeg" alt="Imagem do Hinata" height=500 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-8.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>

### 5. Gere um token para sua conta:


<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-9.jpeg" alt="Imagem do Hinata" height=200 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-10.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>



<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-11.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-12.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>

<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-13.jpeg" alt="Imagem do Hinata" height=300 style="">
</div>


### 6. Salve o arquivo json com o nome `service_account.json` e coloque na pasta do projeto.
<div style="display: flex; justify-content: center; margin-top:50px">
    <img src="./img/passo-14.jpeg" alt="Imagem do Hinata" height="150" style="">
</div>

### 7. Por fim substitua esses valores no arquivo `main.py` pelos seus:

<div style="display: flex; justify-content: center;">
    <img src="./img/passo-15.png" alt="Imagem do Hinata" height="200" style="">
</div>

- WORKSHEET_NAME é o nome da página da planilha usada, nesse se encontra no canto inferior esquerdo da planilha.
- SPREAD_SHEET_ID é o ID da planilha usada, ele se encontra na URL da planilha logo após `/d/id-da-planilha`.
- json_keyfile_path é o caminho em que se encontra o arquivo `service_account.json` baixado.


### 8. Rodando o projeto

Ao rodar o projeto, se deparará com uma planilha atualizada com a situação de cada aluno e a Nota para Aprovação final:

<div style="display: flex; justify-content: center;">
    <img src="./img/final-spreadsheet.png" alt="Imagem do Hinata" height="400" style="">
</div>

### Observações

Para saber mais sobre como funcionam as bibliotecas sugiro a leitura:

- [Documentação pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Documentação gspread](https://docs.gspread.org/en/latest/user-guide.html#updating-cells)
- [Documentação math](https://docs.python.org/3/library/math.html)