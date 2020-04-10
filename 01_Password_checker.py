import requests #allows us to make a request-API
import hashlib #built-in module (namesto SHA1 Hashing)
import sys


def request_api_data(query_char):
	url="http://api.pwnedpasswords.com/range/"+query_char#"60DE8"-hashing (SHA1 generator), želimo anonimnost [GDPR :)]
	res=requests.get(url)  
	if res.status_code!=200: #We want the response 200 or less (400 not ok)
		raise RuntimeError(f'Error fetching:{res.status_code}, check the api and try again') # raise Error:'prisilimo' da vrne to napako
	return res #V primeru, da ni napake in je OK, vrnemo 

def get_password_leaks_count(hashes,hash_to_check):
	hashes=(line.split(':') for line in hashes.text.splitlines()) #dobimo vse kombinacije, ki se ujemajo z našimi prvimi petimi znaki
	for h,count in hashes:
		if h==hash_to_check: #v resnici mi iščemo točno določeno kombinacijo-enolično geslo
			return count #kolikokrat je bilo naše geslo izrabljeno
	return 0 #če se nič ne ujema, naj vrne 0

def pwned_api_check(password):
	#check password if it exists in API response

	#hash our password
	#print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper()) #vrne nam generirano šifro
	sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  #hexdigest mi bo vrnil kodo, ki jo rabim+želim velike tiskane in številke (upper)
	#brez hexdigest dobim samo objekt
	first5_char,tail=sha1password[:5],sha1password[5:]
	response=request_api_data(first5_char) #send it to API, we need only first 5 char.
	#print(first5_char, tail)
	#print(response)
	return get_password_leaks_count(response,tail)
#request_api_data('60DE8') #it must be a string

def main(args):
	for password in args:
		count=pwned_api_check(password)
		if count:
			print(f'{password} was found {count}times...you should probably change your password!')
		else:
			print(f'{password} was NOT found. Carry on!')
	return 'done!'

if __name__=='__main__':
	sys.exit(main(sys.argv[1:])) #exit zagotovino,da gremo 
	#iz procesa; pridemo do done!
