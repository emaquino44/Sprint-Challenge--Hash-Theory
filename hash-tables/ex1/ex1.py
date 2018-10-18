def get_indices_of_item_weights(weights, limit):

	ht = {} #hash table

	for i, weight in enumerate(weights):
		ht[weight] = i  #loop and check if current weight in hash table

		for i, weight in enumerate(weights):
			if limit - weight in ht:  #loop and check if it's in the key
				diff = ht[limit - weight] #return value and store the difference
				if i > diff:  #index and value
					return (i, diff)
				else:
					return (diff, i)



if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  arr = [4, 6, 10, 15, 16]
  limit =21

  print(get_indices_of_item_weights(arr, limit))
