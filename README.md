<h1 align="center">Cyclonet</h1>
<p align="center">🌀 Uma rede neural artificial que utiliza das técnicas de Transfer Learning e Data Augmentation para identificar ciclones tropicais a partir de imagens de oceano tiradas por satélites.</p>

<img src="https://img.shields.io/badge/Python-v3.8.1-yellow"/>

### 🌧 Objetivo

<p>  O Laboratório Oceanográfico e Meteorológico do Atlântico define os Ciclones tropicais (CT 's) como "os sistemas de ar de baixa pressão que se formam sobre os mares tropicais. Em seu centro, há uma grande atividade de tempestades e ventos ciclônicos, e obtém sua energia a partir de diferenças verticais de temperatura, são simétricos e possuem um núcleo quente". Esses sistemas, são considerados os mais catastróficos de que se tem conhecimento no planeta, e por onde passam, causam um grande prejuízo, deixam mortos, feridos e desabrigados.
  No ano de 2017, o dano causado por furacões nos Estados Unidos foi de aproximadamente 265 bilhões de dólares. Já em março de 2019, o ciclone tropical Idai atingiu o leste da África, estimando mais de 1.000 mortes e um prejuízo econômico de 7 milhões de dólares. De acordo com estudos, com as mudanças climáticas, há um aumento global da atividade de ciclones tropicais, e segundo o Quinto Relatório de Avaliação do Painel Intergovernamental sobre Mudanças Climáticas (IPCC), o aquecimento global levará a um aumento da proporção de furacões de maior gravidade. Levando isso em consideração, a temporada de furacões de 2020 no Atlântico Norte chegou a um recorde, registrando a maior quantidade de tempestades de longa duração desde 1878, com o total de 22 ocorrências. Segundo as previsões, 2021 será o sexto ano consecutivo com atividade acima da média no Atlântico Norte, sendo a temporada de furacões mais ativa e perigosa que o normal.
  Através de imagens de satélite, está sendo possível identificar uma tempestade tropical antes do período comum, denominada "Andres", possibilitando que os habitantes de áreas próximas à região de formação desse fenômeno já possam se preparar para os furacões que estão por vir. Dessa forma, com a monitoração constante dos oceanos feita por satélites, o uso de tecnologias que possam ajudar a automatizar e a identificar antecipadamente a formação destes fenômenos poderá ser de grande auxílio, para que medidas de preparo possam ser adotadas, como a evacuação de zonas costeiras, diminuindo o impacto causado pelos ciclones. Portanto, é proposto um modelo que analisa imagens de satélites, e consiga reconhecer e identificar padrões relativos à formação de ciclones tropicais em oceanos, de forma a automatizar a detecção, de forma mais rápida e precisa.</p>

### 🎲 Dataset

<p>Para o modelo foram selecionadas imagens coletadas através da biblioteca "google_images_download", feita na linguagem Python, utilizando algumas palavras-chave para encontrar imagens de furacões e oceanos sem necessariamente a presença deles, como, por exemplo {"tropical cyclone image satellite, tropical cyclone satellite infrared, hurricane satellite data, hurricane formation satellite, hurricane ocean satellite, hurricane storm satellite, hurricane winds satellite delta, tropical storm"}. Foi obtido um total de 1.807 imagens, sendo separadas 386 para a classe de "Oceano", e 701 para a de "Ciclones", estando nos formatos PNG, JPG e JPEG. Os dados foram separados em três conjuntos, sendo 60% das imagens para treino, 20% para validação e 20% para teste. </p>

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Anaconda](https://www.anaconda.com/)
- [google-images-download](https://github.com/hardikvasa/google-images-download)
- [Keras](https://keras.io/)

<footer>
<p>Feito com ❤️ por Fernanda Luna</p>
</footer>

