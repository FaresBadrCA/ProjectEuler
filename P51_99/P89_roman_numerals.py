lines = open(r"data\0089_roman.txt").read().splitlines()

# read characaters until we hit a different one
# if the next character is greater than the current one, the current sum is SUBTRACTED

d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
def from_roman(line):
    prev_v = max(d.values()) # value of previous letter. Used to check for ascending order, indicating subtractive operation  
    n, v_sum = 0, 0  # v_sum: sum of the current repeating character, used in case subtractive rule is invoked
    for c in line:
        v = d[c] # value of current character. Assume additive-only rule for now
    
        if v != prev_v: # new chain of letters
            if v > prev_v: # Ascending order invokes subtractive rule
                n -= 2 * v_sum
            v_sum = 0 # new chain of letters
   
        v_sum += v
        n += v
        prev_v = v
    return n


def to_roman(n):
    chars = []
    while n >= 1000:
        n -= 1000
        chars.append('M')

    if n//100 == 9:
        n -= 900
        chars.extend(['C','M'])
#    elif n//100 == 8:
#        n -= 800
#        chars.extend(['C','C','M'])
    
    if n >= 500:
        n -= 500
        chars.append('D')
    elif n//100 == 4:
        n -= 400
        chars.extend(['C', 'D'])

    while n >= 100:
        n -= 100
        chars.append('C')

    if n//10 == 9:
        n -= 90
        chars.extend(['X','C'])
#    elif n//10 == 8:
#        n -= 80
#        chars.extend(['X','X','C'])
    elif n >= 50:
        n -= 50
        chars.append('L')
    elif n//10 == 4:
        n -= 40
        chars.extend(['X', 'L'])

    while n >= 10:
        n -= 10
        chars.append('X')

    if n == 9:
        n -= 9
        chars.extend(['I','X'])
    #elif n == 8:
    #    n -= 8
    #    chars.extend(['I', 'I', 'X'])

    if n >= 5:
        n -= 5
        chars.append('V')
    elif n == 4:
        n -= 4
        chars.append('I')
        chars.append('V')

    while n >= 1:
        n -= 1
        chars.append('I')

    return ''.join(chars)

result = 0 
for line in lines:
    n = from_roman(line)
    new_line = to_roman(n)

    print(n, new_line)

    if n != from_roman(new_line):
        print("PROBLEM")


    result += len(line) - len(new_line)

print(result)