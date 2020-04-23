dic = {'ratarata': '10.0'}
try:
    print(dic['rata_rata'])
except KeyError:
    print('kunci tidak ditemukan')
except ValueError:
    print('nilai tidak sesuai')

try:
    print(dic['ratarata']/3)
except KeyError:
    print('kunci tida ditemukan')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')

try:
    print('pembulatan rata rata: ', int(dic['ratarata']))
except (ValueError, TypeError) as e:
    print('error: ', e)
