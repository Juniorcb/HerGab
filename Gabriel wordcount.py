from collections import Counter

# file list 



def countAndWrite():
	test_list =[] 
	test_dict = {}
	blank  = False
	tab = False
	temp_word = '' 
	r8_test = "r8-test-all-terms.txt"
	r8_train = "r8-train-all-terms.txt"
	r52_train = "r52-train-all-terms.txt"
	r52_test  = "r52-test-all-terms.txt"

	with open(r8_test,'r+') as f:
		k = f.read()
	
	with open(r8_train,'r+') as f:
		k += f.read()
	with open(r52_test,'r+') as f:
		k += f.read()
	with open(r52_train,'r+') as f:
		k += f.read()
	
	# make a list of words 
	for i in k:
		if i==' ' or  i=='\t' and not blank :
			test_list.append(temp_word)
			temp_word = ''
			blank = True
			
		else:
			temp_word += i 
			blank = False


	#count the number of occurences 
	test_dict = Counter(test_list)
		
	#write it to a file 
	with open("result.txt", 'w+') as f:
		for i in test_dict:
			f.write(i+' - '+str(test_dict[i])+'\n')
	
countAndWrite()
