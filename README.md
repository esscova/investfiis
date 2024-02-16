<a id="readme-top"></a>
![preview](/assets/img/preview.gif)

# Invest.fiis

>Nesta aplicação, foi desenvolvido um dashboard que analisa dados sobre *DY* (Dividend Yield) e Categorias de fundos imobiliários listados na B3.
>
>Utilizando Scraping os dados são coletados, tratados e preparados para consumo da aplicação que, através de filtros, irá gerar análises personalizadas dos fundos imobiliários listados. 
>
>Por fim disponibilizo os dados para download em formato `csv`.

Mas, você sabia que é possível viver com a renda de aluguéis sem ter que comprar um imóvel ou se preocupar com condomínio, reformas e IPTU? Aprenda e comece a investir em Fundos Imobiliários (FIIs).

## O que são fundos imobiliários?

Um fundo imobiliário é uma espécie de “condomínio” de investidores, que reúnem seus recursos para que sejam aplicados em conjunto no mercado imobiliário. A dinâmica mais tradicional é que o dinheiro seja usado na construção ou na aquisição de imóveis, que depois sejam locados ou arrendados. Os ganhos obtidos com essas operações são divididos entre os participantes, na proporção em que cada um aplicou.

_Fonte_: [Infomoney](https://www.infomoney.com.br/guias/fundos-imobiliarios/)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Funcionalidades

- **Insights**: Com a utilização dos filtros de `categoria` e `DY`.
- **Database**: É possível baixar o dataset gerado para suas próprias aplicações.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Estrutura do projeto

- `/assets`: Estilização do projeto.
- `/assets/img`: Imagens utilizadas no projeto.
- `/assets/styles`: Estilização de componentes.
- `/services`: Responsável por coletar os dados e prepará-los para a dashboard.
- `/src/components`: Contém os componenentes do layout.
- `/src/dados`: Datasets gerados durante o desenvolvimento no Jupyter.
- `/src/notebooks`: Notebooks utilizados durante a fase inicial do projeto. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Tecnologias utilizadas

- Python
- Visual Studio Code e Jupyter Notebook
- CSS
- BeautifulSoup 
- Requests
- Pandas
- Dash e Plotly
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Aprendizado

A ideia inicial era apenas coletar os dados do site [fiis.com.br](https://fiis.com.br/lista-de-fundos-imobiliarios/) para minhas análises pessoais de investimento, porém eu sabia que havia como fazer scraping, mas nunca tinha feito antes, tive dificuldades iniciais na coleta e preparação dos dados, e isso é bom, me forçou a aprender mais sobre `pandas` e ler bastante sobre scraping, porém quando concluído, senti a necessidade de um painel para visualizar os dados que antes nos notebooks precisava ficar scrollando, entre tantas opções me forcei ao `dash` para mais um aprendizado, um framework muito versátil que me consume bastante leitura de documentação diária, como busco soluções opensource fiquei bastante satisfeito com esse projeto inicial.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contribua

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou fazer pull requests.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contatos

Autor: [Wellington Moreira Santos](https://www.linkedin.com/in/wellington-moreira-santos/)

Email: wsantos08@hotmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>
