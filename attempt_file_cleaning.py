'''
def filter_invalid_objects(x,y):
  return tf.greater(sys.getsizeof(x), 0) and tf.greater(sys.getsizeof(y), 0)

# Filter the dataset using the filter_invalid_objects function
#print(len(train_dataset), len(val_dataset), len(test_dataset))
#train_dataset2 = train_dataset.filter(filter_invalid_objects)
#val_dataset2 = val_dataset.filter(filter_invalid_objects)
#test_dataset2 = test_dataset.filter(filter_invalid_objects)

#ltrain_dataset = list(train_dataset)
#print(ltrain_dataset)


for data, labels in train_dataset:
    try:
        # Process the data (e.g., decode image)
        # If successful, append it to the list
        decoded_image = tf.image.decode_image(data)
        train_data_list.append(decoded_image)
        train_data_list.append(data)
        print(i)
        i+=1
        
    except tf.errors.InvalidArgumentError:
        # Handle the error (e.g., print a message)
        print("Skipping invalid data")
        print(i)
        i+=1
        
        continue
        '''


'''
all_labels = []

# Iterate through the dataset and append labels to the list
i =0
train_dataset_iter = iter(train_dataset)
while i < len(train_dataset):
    print(i)
    i += 1
    try: 
        element = next(train_dataset_iter)
        all_labels.append(element[1])
    except StopIteration as e:
        print("Exception: ", e)
        continue
    #for images, labels in train_dataset:
    #if (i>4980):
    #    print(labels)
#    all_labels.append(labels)
    

# Concatenate all labels into a single NumPy array
train_labels = tf.concat(all_labels, axis=0).numpy()
'''