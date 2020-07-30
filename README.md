# AmericanRecessionPredict
Código em Python para prever uma recessão nos Estados Unidos da América.

Baseado em um [artigo](https://mises.org.br/Article.aspx?id=2971) do Instituto Mises, criei este código que serve para analisar as taxas de juros do tesouro americano (3 meses, 2 anos, 10 anos e 30 anos) e avisar se esta havendo uma [inversão da curva de juros](https://www.investopedia.com/terms/i/invertedyieldcurve.asp).

![Gráfico das Taxas de Juros e sua correlação com recessões](https://fred.stlouisfed.org/graph/fredgraph.png?g=morW)

## Requisitos
Python 3.x


fredapi - https://pypi.org/project/fredapi/
```
pip install fredapi
```

Api Key válida - [St Louis Fed](https://fred.stlouisfed.org/)
Obtenha a Api Key no site fazendo seu cadastro, depois vá em My Account > Api Keys

## Uso

Edite o Código e coloque sua Api Key entre aspas ('54465855') no código e então inicie
```
python crise.py
```
