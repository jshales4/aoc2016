##AoC_2016_14.py
import hashlib
def main():
    #salt = 'abc'
    salt = 'ahsbgdzn'
    index = 0
    result_set = []
    counter = 0
    hash_dict = {}
    while counter < 64:
        ##salted_index = hashlib.md5(salt+str(index)).hexdigest()
        salted_index, hash_dict = mega_hash(salt+str(index), hash_dict)
        for n in range(len(salted_index)):
            if salted_index[n] == salted_index[n+1] and salted_index[n]==salted_index[n+2]:
                result = key_checker(salt,index,salted_index[n], hash_dict)
                hash_dict = result[2]
                if result[0] == True:
                    result_set.append(result[1])
                    counter += 1
                break
            if n == len(salted_index) -3:
                break
        index += 1
    print result_set[63]

def key_checker(salt, index, letter_found, hash_dict):
    for p in range(1,1001):
        salted_index, hash_dict = mega_hash(salt+str(index+p), hash_dict)
        ##salted_index = hashlib.md5(salt+str(index+p)).hexdigest()
        if letter_found * 5 in salted_index:
            return True, index, hash_dict
    else: return False, 0, hash_dict

def mega_hash(salted_index, hash_dict):
    salted_index_iter = hashlib.md5(salted_index).hexdigest()
    if salted_index_iter in hash_dict:
        return hash_dict[salted_index_iter], hash_dict
    else:
        for n in range(2016):
            salted_index_iter = hashlib.md5(salted_index_iter).hexdigest()
        hash_dict[hashlib.md5(salted_index).hexdigest()] = salted_index_iter
        return salted_index_iter, hash_dict 





if __name__ == '__main__':
    main()
