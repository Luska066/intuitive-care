<div style="padding-bottom: 20px">
  <h1>Teste Intuitive Care</h1>
  <h5>
    Meu nome é Lucas, Espero que gostem =D
    <br>
    Meu Número: 71 9 9739-6256
  </h5>
  
  Tecnologias Usadas :
  <ul>
      <li>IDE: PyCharm</li>
      <li>Versão Python : 3.10</li>
      <li>Versão Docker: 20.0.1</li>
      <li>Versão docker-compose: 1.29.2</li>
      <li>Versão Node: 22.13.1</li>
      <li>Versão Npm: v10.9.2</li>
      <li>Versão Nvm: v0.40.1</li>
      <li>Front End Framework: Quasar Vue</li>
      <li>API: FastAPI</li>
      <li>Sistema Operacional: Ubuntu</li>
  </ul>
  
  Execute os passos abaixo :
  
    ATENÇÃO LEMBRE-SE DE CONFERIR E INSTALAR TODOS PACOTES
    PRESENTES NO ARQUIVO : requirements.txt

    CASO VEJA O ERRO IGNORE-O:
        Failed to import jpype dependencies. Fallback to subprocess.
        No module named 'jpype'

Lembre-se de estar na pasta raiz
     
    Execute PRIMEIRO o WebScrapping:

      - Ele baixará os arquivos do DESAFIO 3 e DESAFIO 1
          * Arquivos baixados ficarão em /Selenium/Downloads  
          * Arquivos gerados/convertidos ficarão em  /Selenium/Archives

      $ python.3.10 MainPrompt.py      
  
    Execute em seguida :
     Esse prompt vai preencher toda a tabela com dados do desafio 3
     Lembrando que o scrapping vai se responsabilizar por baixar e extrair
     os arquivos cidados no 3.1 e 3.2
     
     - O Prompt Abaixo vai realizar as inserções no Banco de Dados
          - ao selecionar a opção você vai inserir todos os dados do arquivo 
            csv sitado no 3.1,então pode ser que demore, mas caso você 
            queira interromper não tem problema, so cancelar
            e executar novamente o script abaixo para subir o container docker!

          - O Container Docker é importante para você ter o Banco de Dados

          - Caso não tenha docker altere no .env as credênciais do DB

     terminal
      $ python.3.10 DatabasePrompt.py
      
       Ao executar, um meno aparecerá:
          Selecione uma opção
          1 - Deseja inserir dados do csv no banco?
          2 - Consultar as 10 operadoras com maiores Despesas (EVENTOS/ SINISTROS CONHECIDOS)
          3 - Consultar as 10 operadoras com maiores Despesas (AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR)
          4 - Consultar as 10 com maiores despesas
          0 - Finalizar
          Seleciona a opção : 1

          SELECIONE A OPÇÃO 1 CASO NÃO TENHA EXECUTADO NENHUMA VEZ!
          CASO JA TENHA SELECIONADO NÃO EXECUTE NOVAMENTE!
          O PROCESSO PODE DEMORAR UM CERTO TEMPO
          
  
<h1>4 - TESTE DE API</h1>
Observação:
     
     1 - Verifique se o CONTAINER mysql esteja rodando
          - Caso não use docker, modifique as credênciais no .ENV
     
Executar API:
     
     Para executar a API, entre na pasta IntuitiveCare/FastApi e execute:
          - Ela rodará na porta 8000

     terminal: 
          $fastapi dev FastApi.py
     
Executar FRONT-END:

     Para rodar o front, entre na pasta IntuitiveCare/intuitive-front
          
          - Certifique-se de estar na versão citada la em cima
          - Node => 22

          - Ela rodará na porta 9000
               
          terminal: 
               $ npm install
               $ npm run dev

EM MINHA DEFESA
    SO NÃO RODEI EM NUVEM, PORQUE O EC2 GRATIS NÃO AGUENTOU, MESMO USANDO MEMÓRIA SWAP
    DECIDI BOTAR TUDO EM UM ARQUIVO PARA FACILITAR PARA VOCÊS =D
</div>
