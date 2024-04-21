def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(lst):
    count = 1
    for i in range(len(lst)):
        if lst[i] == lst[-1]:
            break
        if lst[i + 1] > lst[i] :
            count = count + 1
        if lst[i + 1] <= lst[i]:
            count = count - 1
        
    if count == len(lst):
        return True
    else:
        return False

def riffle(items, out=True):
    lst1 = []
    lst2 = []
    lst3 = []
    half = len(items) // 2
    
    for i in items[:half]:
        lst1.append(i)
    for i in items[half:]:
        lst2.append(i)
    
    if out == True:
        i = 0
        while i != half:
            lst3.append(lst1[i])
            lst3.append(lst2[i])
            i = i + 1
    
    if out == False:
        i = 0
        while i != half:
            lst3.append(lst2[i])
            lst3.append(lst1[i])
            i = i + 1
    
    return lst3

def only_odd_digits(n):
    count = 0
    
    while n:
        last = n % 10
        if last % 2 == 0:
            count = count + 1
            n = n // 10
        else: n = n // 10
    
    if count > 0:
        return False
    else: return True

def is_cyclops(n):
    if n == 0:
        return True
    a = []
    while n:
        last = n % 10
        a.append(last)
        n = n // 10
    
    if len(a) % 2 == 0:
        return False
    
    a.reverse()
    mid = (len(a) - 1) // 2
    zeros = 0
    for i in a:
        if i == 0:
            zeros = zeros + 1
    
    if zeros != 1:
        return False
        
    if a[mid] == 0:
        return True
    else: return False

def domino_cycle(tiles):
    if not tiles:
        return True
    lst = []
    for i in tiles:
        for j in i:
            lst.append(j)
    
    if lst[0] != lst[-1]:
        return False
    
    lst = lst[1:-1]

    end = True
    i = 0
    while i != len(lst):
        print(lst[i], lst[i + 1])
        if lst[i] == lst[i + 1]:
            i = i + 2
        else:
            end = False
            break   
    return end

def colour_trio(colors):
    dct =  {"yy": "y", "bb": "b", "rr": "r",
            
            "yr": "b", "ry": "b",
            "by": "r", "yb": "r",
            "rb": "y", "br": "y" }
    temp = []
    lcolors = list(colors)
    go = True
    while len(lcolors) != 1:
        while len(temp) != len(lcolors) - 1:
            for i in range(len(lcolors) - 1):
                mix = lcolors[i] + lcolors[i + 1]
                temp.append(dct[mix])
        lcolors = temp
        temp = []
    
    return lcolors[0]

def count_dominators(items):
    count = 1
    items.reverse()
    dom = items[0]
    
    for i in items:
        if i > dom:
            dom = i
            count = count + 1    
    
    return count

def extract_increasing(digits):
    
    res = []
    prior = -1
    current = 0
    
    for i in range(len(digits)):
        d = int(digits[i])
        current = (current * 10) + d
        
        if current > prior:
            res.append(current)
            prior = current
            current = 0        
    
    return res

def words_with_letters(words, letters):
   
    res = []
        
    for word in words:
        letters_char = letters[0]
        letterIndex = 0
        
        for word_char in word:
            if word_char == letters_char:
                letterIndex = letterIndex + 1
                if letterIndex == len(letters):
                    res.append(word)
                    break
                letters_char = letters[letterIndex]
    
    return res
        
def taxi_zum_zum(moves):
  
    x = 0
    y = 0
    atPosition = 12
    
    right = {12: 3, 3: 6, 6: 9, 9: 12}
    left = {12: 9, 9: 6, 6: 3, 3: 12}
    
    if moves[0] == "L":
        atPosition = 9
    elif moves[0] == "R":
        atPosition = 3
    elif moves[0] == "F":
        atPosition = 12
        y = y + 1
    
    for i in range(1, len(moves)):
        if moves[i] == "R":
            atPosition = right[atPosition]
        elif moves[i] == "L":
            atPosition = left[atPosition]
        elif moves[i] == "F":
            if atPosition == 12:
                y = y + 1
            elif atPosition == 3:
                x = x + 1
            elif atPosition == 6:
                y = y - 1
            elif atPosition == 9:
                x = x - 1
                
    return tuple([x,y])

def give_change(amount, coins):
    res = []
    
    for i in coins:
        while i <= amount:
            res.append(i)
            amount = amount - i
    
    return res

def safe_squares_rooks(n, rooks):
   
    if len(rooks) == 0:
        return n * n
    
    else:
        twoD = [['No' for x in range(n)] for y in range(n) ]
        i = 0
        while i < len(rooks):
            temp = rooks[i]
            num = temp[0]
            num1 = temp[1]
            for g in range(len(twoD[num])):
                twoD[num][g] = 'Yes'
        
            for x in range(len(twoD)):
                for j in range(len(twoD[x])):
                    if j == num1:
                        twoD[x][j] = 'Yes'
            i = i + 1
        count = 0
        for x in range(len(twoD)):
                for j in range(len(twoD[x])):
                    if twoD[x][j] != 'Yes':
                        count = count + 1
        return count

def words_with_given_shape(words, shape):
    res = []
    temp = []
    def shapeNum(current, after):
            if after > current:
                temp.append(1)
            elif current == after:
                temp.append(0)
            elif after < current:
                temp.append(-1)
    
    for word in words:
        temp = []
        if len(word) == len(shape) + 1:
            for word_char in range(len(word) - 1):
                shapeNum(word[word_char], word[word_char + 1])
                if temp == shape:
                    res.append(word)
                    break   
    return(res)

def is_left_handed(pips):
    valid = ""
    original = True
    sum7 = 7
    
    for i in range(len(pips)):
        if pips[i] > 3:
            pips[i] = sum7 - pips[i]
            original = not original
    
    validPips = [[1,2,3],[2,3,1],[3,1,2]]
    if pips in validPips:
        valid =  True
    else:
        valid = False 
           
    if (valid and original) or (not valid and not original):
        return True
    return False

