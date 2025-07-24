# Automatizador de Mensagens WhatsApp Web

Este script Python foi desenvolvido para automatizar o envio de mensagens via WhatsApp Web. Ele lê uma planilha Excel contendo nomes e números de telefone, e então utiliza esses dados para enviar mensagens personalizadas para cada contato.

---

## Linguagens e Tecnologias Utilizadas

- **Python:** A linguagem de programação principal utilizada para desenvolver o script de automação.
- **openpyxl:** Biblioteca Python para leitura e escrita de arquivos Excel (`.xlsx`).
- **PyAutoGUI:** Biblioteca Python para automação de GUI, permitindo controlar o mouse e o teclado para interagir com o WhatsApp Web.

---

## Funcionalidades

- **Leitura de Planilha Excel:** Processa arquivos `.xlsx` para extrair dados de nome e telefone.
- **Envio de Mensagens Automatizado:** Utiliza a interface do WhatsApp Web para localizar contatos e enviar mensagens pré-definidas ou personalizadas.
- **Personalização de Mensagens:** Permite a inclusão do nome do contato na mensagem para um toque mais pessoal.

---

## Pré-requisitos

Para executar este script, você precisará ter o **Python instalado (versão 3.x recomendada)** e as seguintes bibliotecas Python.

### Instalação das Dependências

É altamente recomendado criar um **ambiente virtual** para isolar as dependências do seu projeto.

1.  **Instale as bibliotecas necessárias:**

no seu terminal (com o ambiente virtual ativado), execute:

    ```bash
    pip install -r requirements.txt
    ```

---

## Como Usar

1.  **Prepare sua Planilha Excel:**

    - Crie um arquivo Excel (`.xlsx`) com duas colunas principais: uma para o **nome** do contato e outra para o **número de telefone**.
    - Certifique-se de que os números de telefone estejam no formato correto, incluindo o código do país (ex: `55DDNNNNNNNNN` para Brasil, onde `55` é o código do país, `DD` é o DDD e `NNNNNNNNN` é o número).
    - Nomeie o arquivo da planilha e a aba conforme o script espera, ou ajuste o script para o nome da sua planilha/aba.

2.  **Configure o Script:**

    - Abra o arquivo principal do script Python (`app.py`).
    - Ajuste as variáveis conforme necessário, como o nome do arquivo Excel, o nome da aba, e a **mensagem que você deseja enviar**.
    - Pode ser necessário configurar atrasos (`time.sleep()`) no script, dependendo da velocidade da sua internet e do seu computador, para garantir que os elementos do WhatsApp Web sejam carregados antes que o script tente interagir com eles.

3.  **Execute o Script:**

    - Abra seu terminal ou prompt de comando.
    - Navegue até a pasta onde o script está salvo.
    - Certifique-se de que seu ambiente virtual esteja ativado (`(venv)` deve aparecer no prompt).
    - Execute o script:

      ```bash
      python app.py
      ```

4.  **Acompanhe a Automação:**
    - O script abrirá automaticamente o navegador e navegará até o WhatsApp Web.
    - **Mantenha o navegador aberto e ativo.** Não interaja com o mouse ou teclado enquanto o script estiver rodando, a menos que seja instruído a fazê-lo.
    - O script tentará localizar os contatos e enviar as mensagens.

---

## Considerações Importantes

- **Configuração do WhatsApp Web:** Certifique-se de que você está **logado no WhatsApp Web** no seu navegador antes de executar o script. Mantenha a sessão ativa.
- **Velocidade da Internet:** Uma conexão de internet estável é crucial para o bom funcionamento do WhatsApp Web e para a detecção correta dos elementos pelo script.
- **Limites de Mensagens:** Tenha cuidado ao enviar um grande volume de mensagens em pouco tempo para evitar ser sinalizado como spam pelo WhatsApp. **Use esta ferramenta com responsabilidade.**
- **Atualizações do WhatsApp Web:** O WhatsApp Web pode ser atualizado periodicamente, o que pode alterar a interface e, consequentemente, quebrar a automação. Se o script parar de funcionar, pode ser necessário ajustar as coordenadas de cliques ou a lógica de busca de elementos no seu código Python.
- \*\* siga o padrão nome na primeira coluna e telefone na segunda coluna do excel.
