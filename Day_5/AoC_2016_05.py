##AoC_2016_05.py
# def main():
# 	import hashlib
# 	code = 'ffykfhsq'
# 	password = []
# 	index = 0
# 	m=hashlib.md5()
# 	#print code + str(index)
# 	while (len(password)<8):
# 		if hashlib.md5(code+str(index)).hexdigest()[0:5] == '00000': 
# 			password.append(hashlib.md5(code+str(index)).hexdigest()[5])
# 			index += 1
# 		else: 
# 			index += 1
# 	print password
# main()

def main():
	import hashlib
	code = 'ffykfhsq'
	password = ['$'] * 8
	index = 0
	while '$' in password:
		if hashlib.md5(code+str(index)).hexdigest()[0:5] == '00000': 
			hashed = hashlib.md5(code+str(index)).hexdigest()
			if (hashed[5].isdigit() and int(hashed[5])<8 and password[int(hashed[5])] == '$'):
				password[int(hashed[5])] = hashed[6]
			index += 1
		else: 
			index += 1
	print password
main()