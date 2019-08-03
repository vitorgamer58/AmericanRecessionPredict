#python 3.x
#criado por vitorgamer58
from fredapi import Fred 
fred = Fred(api_key='sua api key aqui')

#puxa os dados das taxas de juros e armazena na variavel
taxa3month = fred.get_series_latest_release('DTB3')
taxa2years = fred.get_series_latest_release('DGS2')
taxa10years = fred.get_series_latest_release('DGS10')
taxa30years = fred.get_series_latest_release('DGS30')

#armazena na variavel o valor mais recente das taxas de juros
var3month = (taxa3month[-1])
var2years = (taxa2years[-1])
var10years = (taxa10years[-1])
var30years = (taxa30years[-1])

#com base nas taxas de juros da os resultados
if(var3month>=var2years):
	print ('A taxa de juros de 3 meses esta maior que a taxa de 2 anos')

if(var3month>=var10years):
	print ('a taxa de 3 meses esta maior que a taxa de juros de 10 anos, cuidado')

if(var2years>=var10years):
	print ('a taxa de 2 anos esta maior que a taxa de 10 anos')
	print ('sendo assim, tambem e um indicador de recessao')
	print ('porem Anthony P. Geller prefere analisar as taxas de 3 meses e 30 anos')
	if(var3month<=var30years):
		print ('')
		print ('e a taxa de juros de 3 meses ainda nao esta maior que a taxa de 30 anos')
		print ('por enquanto, stay safe')

if(var3month>=var30years):
	print ('agora fudeu')
	print ('segundo a teoria devemos esperar por uma recessao em 6 ou 12 meses')

if(var3month<=var30years):
	print ('por enquanto esta tudo tranquilo com as taxas de 3 meses e 30 anos')

if(var3month>=var30years) or (var2years>=var10years) or (var3month>=var2years):
	print ('')
	print ('Ground Control to Major Tom')
	print ('Your circuits dead, theres something wrong')
	print ('Can you hear me, Major Tom?')
	print ('')
	print ('A chapa esta esquentando')


print ('')
print ('taxas de juros:')
print ('3 Meses:', var3month)
print ('2 Anos: ', var2years)
print ('10 Anos:', var10years)
print ('30 Anos: ', var30years)
