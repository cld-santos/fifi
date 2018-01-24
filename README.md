# Fifi

Um cão pode farejar muito bem, porém só uma fofoqueira padrão fifi vai além do boato. xD

É um projeto que bisbilhota noticías de assuntos escolhidos por seu usuário.

Seu mecanismo obtém um tópico e uma url alvo e tenta descobrir tudo sobre aquele tópico neste site alvo procurando pelo assunto e por referências à ele investigando as referências em busca de informações.


## Cenário hipotético que tento resolver

Coletar as informações postadas pelo Governo Brasileiro sobre a Febre Amarela. O tema como dito é "febre amarela" e a fonte de informações que utilizaremos é o site com as ultimas noticias do [Governo Brasileiro](http://www.brasil.gov.br/home-1/ultimas-noticias)


## How to


É importante instalar o geckodriver, pois a pagina é renderizada utilizando JavaScript

	echo https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu

	wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
	tar -xvzf geckodriver*
	sudo mv geckodriver /usr/local/bin/geckodriver
	export PATH=$PATH:/usr/local/bin/geckodriver

em seguida, instale os pacotes disponíveis na pasta requirements:

	usr@fifi/src$ pip install -r requirements/base.txt


Para executar, em:

	usr@fifi/src$ python main.py "febre amarela" "http://www.brasil.gov.br/home-1/ultimas-noticias"


## Disclaimer

Este é um prototótipo que tem o intuito de demonstrar o conhecimento no assunto coleta de dados não normalizados. Pode ser notado algumas práticas que funcionam bem para testes e aprendizados, porém sabemos que o Scrapinghub ou o uso de um WebDriver Remoto pode ser uma solução mais robusta para cenários em produção. Nos restringimos ao uso do webdriver que consome uma instancia do Firefox para facilitar a construção e apresentação dos conceitos
