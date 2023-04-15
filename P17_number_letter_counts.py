num_word_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
                10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
                20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
                }

num_len_dict = {n : len(num_word_dict[n]) for n in num_word_dict }

one_to_nine_num_letters = 0
for i in range(1, 10, 1):
    one_to_nine_num_letters += num_len_dict[i]

ten_to_nineteen_num_letters = 0
for i in range(10, 20, 1):
    ten_to_nineteen_num_letters += num_len_dict[i]

tens_num_letters = 0 # twenty, twenty one, twenty two, ..., thirty, thirty one, thirty two, ... , ninety nine
for i in range(20, 100, 10):
    tens_num_letters += num_len_dict[i] * 10 + one_to_nine_num_letters

one_to_99_num_letters = one_to_nine_num_letters + ten_to_nineteen_num_letters + tens_num_letters

# one hundred, two hundred, three hundred, ... nine hundred
hundreds_flat_num_letters = 9 * 7 + one_to_nine_num_letters

# one hundred and one, one hundred and two, one hundred and three, ..., one hundred and ninety nine
hundreds_num_letters = 0
for i in range(1, 10, 1): # 101 to 199, then 201 to 299, ..., then 901 to 999
    n_hundreds_num_letters = num_len_dict[i]
    ############################    (N + hundred + and) + ... 
    hundreds_num_letters += (n_hundreds_num_letters + 7 + 3) * 99 + one_to_99_num_letters

total = one_to_99_num_letters + hundreds_flat_num_letters + hundreds_num_letters + len('onethousand')
print(total)