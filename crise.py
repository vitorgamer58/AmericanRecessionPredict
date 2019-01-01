#python 2.7
#criado por vitorgamer58
from fredapi import Fred 
fred = Fred(api_key='sua api key aqui')
taxa3 = fred.get_series_latest_release('DTB3')
taxa10 = fred.get_series_latest_release('DGS10')
taxa30 = fred.get_series_latest_release('DGS30')
var1 = (taxa3[-1])
var2 = (taxa10[-1])
var3 = (taxa30[-1])

if(var1>=var2):
	print 'Ground Control to Major Tom'
	print 'Your circuits dead, theres something wrong'
	print 'Can you hear me, Major Tom?'
	print ''
	print 'A chapa esta esquentando'
	print ''
	print 'taxas de juros:'
	print '3 Anos:', var1
	print '10 Anos:', var2

if(var1>=var3):
	print 'agora fudeu'
	print 'segundo a teoria devemos esperar por uma recessao em 6 ou 12 meses'
	print ''
	print 'taxas de juros:'
	print '3 Anos:', var1
	print '30 Anos: ', var3

if(var1<=var3):
	print 'por enquanto esta tudo tranquilo'
	print ''
	print 'taxas de juros:'
	print '3 Anos:', var1
	print '10 Anos:', var2
	print '30 Anos: ', var3
