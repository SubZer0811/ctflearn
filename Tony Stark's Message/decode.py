import pickle

class Node:

	def __init__(self):
		pass

string = [None] *100
table = []

def third(el):
	return el[2]

def print_vars (x, enc):

	table.append([x.data, x.freq, x._count, enc])
	# print(type(x.freq), x.freq)
	# print(type(x.data), x.data)
	# print(type(x.left), x.left)
	# print(type(x.right), x.right)
	# print(type(x._count), x._count)
	print()

encoded_data = "110110101000111001001100011010000100101011110101100110100011001110100100011001110000100011101000001001010111011010111110001101101001000001011010110011011001110010111010011010110011001010111011011011010000001110100100001011111101010011001000011000001111110100001011111000100001101011101011110010000101111001111101001010010001001110100100000101110101001111101100011101110001111101111010101111101000010011000111110010110111111000010011111111001111111011011010000100111100111010111011100011011111100010100011110101010011111110011110100110101100010101111011111110110100010101000110110111001000011011111101110101001111110111001001100011101111011100100101010010001100001110101000011000010001110100001001011110101011101011111110000010011000000"
encoding_table = []

def rec(node, i):

	global string
	if(node == None):
		return
	
	if(node.data != '\x00'):
		encoding_table.append((''.join(string[:i]), node.data))
		# print(''.join(string[:i]), node.data)

	string[i] = '0'
	rec(node.left, i+1)
	string[i] = '1'
	rec(node.right, i+1)

if __name__ == "__main__":
	
	# load : get the data from file
	data = pickle.load(open('node_data.txt', "rb"))

	print("!!!!!!!!!!!!!!!!!!!!!!!")

	rec(data, 0)
	print("ENCODING TABLE:")
	for i in encoding_table:
		print(i)

	check = ''

	for bit in encoded_data:
		check += str(bit)

		for encoding in encoding_table:
			if(check == encoding[0]):
				print(encoding[1], end='')
				check = ''
				break