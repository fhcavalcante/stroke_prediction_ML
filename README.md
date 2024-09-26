MVP - Qualidade de Software, Segurança e Sistemas Inteligentes

Projeto: ML Stroke Prediction

Predição de infartos com uso de Machine Learning

Este projeto foi desenvolvido por Flávio Cavalcante e faz parte do trabalho de conclusão do módulo de Qualidade de Software, Segurança e Sistemas Inteligentes da Pós-Graduação em Engenharia de Software da Puc-Rio.

O sistema é um terminal de predição desenvolvido com uso de modelos de Machine Learning, onde o usuário pode realizar predições de infarto. Um frontend se comunica com um serviço de respostas, que utilizando um modelo treinado reponde com a prediçao
e gera um histórico.

Como executar

Frontend: Fazer o download do projeto e abrir o arquivo index.html no seu browser.

Backend:
1 - Habilite um ambiente virtual (recomendado).

2 - Instale as bibliotecas listadas no arquivo 'requirements.txt' com o seguinte comando:

(env)$ pip install -r requirements.txt

3 - Execute a API com o comando:

(env)$ flask run --host 0.0.0.0 --port 5000
