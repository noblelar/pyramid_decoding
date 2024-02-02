
def organize_into_pyramid(input_file):
    # Read the values from the file
    with open(input_file, 'r') as file:
        values = sorted([int(line.split()[0]) for line in file])

    # Calculate the number of rows needed for the pyramid
    num_values = len(values)
    num_rows = int((-1 + (1 + 8 * num_values) ** 0.5) / 2)

    # Initialize the pyramid with zeros
    pyramid = [[0] * i for i in range(1, num_rows + 1)]

    # Fill the pyramid with the given values
    index = 0
    for i in range(num_rows):
        for j in range(i + 1):
            pyramid[i][j] = values[index]
            index += 1

    return pyramid

# # Example usage:
# input_file = 'coding_qual_input.txt'
# resulting_pyramid = organize_into_pyramid(input_file)

# # Print the resulting pyramid
# for row in resulting_pyramid:
#     print(row)

# print(resulting_pyramid)


def decode(message_file):
 # Read the encoded message from the file
   with open(message_file, 'r') as file:
         lines = file.readlines()

   pyramid_outcome = organize_into_pyramid(message_file)

   decoded_words = []
   for pyramid_item in pyramid_outcome:
      decoded_value = pyramid_item[-1]
      
      for item in lines:
         parts = item.split()
         if int(parts[0]) == decoded_value:
            decoded_words.append(parts[-1])

     # Join the decoded words into a string
   decoded_message = ' '.join(decoded_words)
   return decoded_message

 # Test Case
encoded_file = 'coding_qual_input1.txt'
decoded_message = decode(encoded_file)

print(decoded_message)
 