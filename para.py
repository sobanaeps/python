filename=(path/godfather.txt")
with open(filename,'r')as file:
 lines_in_file=file.read()
 ntlk_tokens=nltk.word_tokenize(lines_in_file)
 print5 nltk_tokens
 print"/n"
 print"Number of words:",len(nltk_tokens)
