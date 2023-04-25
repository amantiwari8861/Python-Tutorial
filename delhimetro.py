from time import sleep

_yellow = [['y1', 'Samaypur Badli'], ['y2', 'Rohini Sector 18,19'], ['y3', 'Haiderpur Badli Mor'], ['y4', 'Jahangirpuri'], ['y5', 'Adarsh Nagar'], ['y6', 'Azadpur'], ['y7', 'Model Town'], ['y8', 'GTB Nagar'], ['y9', 'Vishwavidyalaya'], ['y10', 'Vidhan Sabha'], ['y11', 'Civil Lines'], ['y12', 'Kashmere Gate'], ['y13', 'Chandni Chowk'], ['y14', 'Chawri Bazar'], ['y15', 'New Delhi'], ['y16', 'Rajiv Chowk'], ['y17', 'Patel Chowk'], ['y18', 'Central Secretariat'], [
    'y19', 'Udyog Bhawan'], ['y20', 'Lok Kalyan Marg'], ['y21', 'Jor Bagh'], ['y22', 'INA'], ['y23', 'AIIMS'], ['y24', 'Green Park'], ['y25', 'Hauz Khas'], ['y26', 'Malviya Nagar'], ['y27', 'Saket'], ['y28', 'Qutab Minar'], ['y29', 'Chhatarpur'], ['y30', 'Sultanpur'], ['y31', 'Ghitorni'], ['y32', 'Arjangarh'], ['y33', 'Guru Dronacharya'], ['y34', 'Sikandarpur'], ['y35', 'MG Road'], ['y36', 'IFFCO Chowk'], ['y37', 'Huda City Centre']]
_voilet = [['v1', 'Kashmere Gate'], ['v2', 'Lal Quila'], ['v3', 'Jama Masjid'], ['v4', 'Delhi Gate'], ['v5', 'ITO'], ['v6', 'Mandi House'], ['v7', 'Janpath'], ['v8', 'Central Secretariat'], ['v9', 'Khan Market'], ['v10', 'JLN Stadium'], ['v11', 'Jangpura'], ['v12', 'Lajpat Nagar'], ['v13', 'Moolchand'], ['v14', 'Kailash Colony'], ['v15', 'Nehru Place'], ['v16', 'Kalkaji Mandir'], ['v17', 'Govind Puri'], ['v18', 'Harkesh Nagar Okhla'], [
    'v19', 'Jasola Apollo'], ['v20', 'Sarita Vihar'], ['v21', 'Mohan Estate'], ['v22', 'Tughlakabad'], ['v23', 'Badarpur Border'], ['v24', 'Sarai'], ['v25', 'NHPC Chowk'], ['v26', 'Mewala Maharajpur'], ['v27', 'Sector-28'], ['v28', 'Badkal Mor'], ['v29', 'Old Faridabad'], ['v30', 'Neelam Chowk Ajronda'], ['v31', 'Bata Chowk'], ['v32', 'Escorts Mujesar'], ['v33', 'Sant Surdas (Sihi)'], ['v34', 'Raja Nahar Singh']]
_red = [['r1', 'Rithala'], ['r2', 'Rohini West'], ['r3', 'Rohini East'], ['r4', 'Pitampura'], ['r5', 'Kohat Enclave'], ['r6', 'Netaji Subhash Place'], ['r7', 'Keshav Puram'], ['r8', 'Kanhaiya Nagar'], ['r9', 'Inderlok'], ['r10', 'Shastri Nagar'], ['r11', 'Pratap Nagar'], ['r12', 'Pul Bangash'], ['r13', 'Tis Hazari'], ['r14', 'Kashmere Gate'], [
    'r15', 'Shastri Park'], ['r16', 'Seelampur'], ['r17', 'Welcome'], ['r18', 'Shahdara'], ['r19', 'Mansarovar Park'], ['r20', 'Jhilmil'], ['r21', 'Dilshad Garden'], ['r22', 'Shaheed Nagar'], ['r23', 'Raj Bagh'], ['r24', 'Rajendra Nagar'], ['r25', 'Shyam Park'], ['r26', 'Mohan Nagar'], ['r27', 'Hindon River Arthala'], ['r28', 'New Bus Adda']]
_magenta = [['m1', 'Botanical Garden'], ['m2', 'Okhla Bird Sanctuary  '], ['m3', 'Kalindi Kunj'], ['m4', 'Shaheen Bagh'], ['m5', 'Okhla Vihar'], ['m6', 'Jamia Millia Islamia'], ['m7', 'Sukhdev Vihar'], ['m8', 'Okhla NSIC'], ['m9', 'Kalkaji Mandir'], ['m10', 'Nehru Enclave'], ['m11', 'Greater Kailash'], ['m12', 'Chirag Delhi'], [
    'm13', 'Panchsheel Park'], ['m14', 'Hauz Khas'], ['m15', 'IIT'], ['m16', 'RK Puram'], ['m17', 'Munirka'], ['m18', 'Vasant Vihar'], ['m19', 'Shankar Vihar'], ['m20', 'Terminal 1- IGI Airport'], ['m21', 'Sadar Bazar Cantonment'], ['m22', 'Palam'], ['m23', 'Dashrath Puri'], ['m24', 'Dabri Mor'], ['m25', 'Janak Puri West']]
_pink = [['p1', 'Majlis Park'], ['p2', 'Azadpur'], ['p3', 'Shalimar Bagh'], ['p4', 'Netaji Subhash Place'], ['p5', 'Shakurpur'], ['p6', 'Punjabi Bagh'], ['p7', 'ESI Hospital'], ['p8', 'Rajouri Garden'], ['p9', 'Mayapuri'], ['p10', 'Naraina Vihar'], ['p11', 'Delhi Cantonment'], ['p12', 'Durgabai Deshmukh South Campus'], ['p13', 'Sir Vishweshwaraiah Moti Bagh'], ['p14', 'Bhikaji Cama Place'], ['p15', 'Sarojini Nagar'], ['p16', 'INA'], ['p17', 'South Extension'], ['p18', 'Lajpat Nagar'], ['p19', 'Vinobapuri'], [
    'p20', 'Ashram'], ['p21', 'Hazrat Nizamuddin'], ['p22', 'Mayur Vihar I'], ['p23', 'Mayur Vihar Pocket 1'], ['p24', 'Trilokpuri'], ['p25', 'East Vinod Nagar - Mayur Vihar-II'], ['p26', 'Mandawali West Vinod Nagar'], ['p27', 'IP Extension'], ['p28', 'Anand Vihar'], ['p29', 'Karkarduma'], ['p30', 'Karkarduma Court'], ['p31', 'Krishna Nagar'], ['p32', 'East Azad Nagar'], ['p33', 'Welcome'], ['p34', 'Jafrabad'], ['p35', 'Maujpur'], ['p36', 'Gokulpuri'], ['p37', 'Johri Enclave'], ['p38', 'Shiv Vihar']]
_green = [['g1', 'Inderlok'], ['g2', 'Ashok Park Main'], ['g3', 'Punjabi Bagh'], ['g4', 'Shivaji Park'], ['g5', 'Madipur'], ['g6', 'Paschim Vihar (East)'], ['g7', 'Paschim Vihar (West)'], ['g8', 'Peera Garhi'], ['g9', 'Udyog Nagar'], ['g10', 'Maharaja Surajmal Stadium'], ['g11', 'Nangloi'], [
    'g12', 'Nangloi Railway Station'], ['g13', 'Rajdhani Park'], ['g14', 'Mundka'], ['g15', 'Mundka Industrial Area (MIA)'], ['g16', 'Ghevra Metro Station'], ['g17', 'Tikri Kalan'], ['g18', 'Tikri Border'], ['g19', 'Pandit Shree Ram Sharma'], ['g20', 'Bahadurgarh City'], ['g21', 'Brigadier Hoshiyar Singh']]
_bgreen = [['G1', 'Ashok Park Main'], [
    'G2', 'Satguru Ram Singh Marg'], ['G3', 'Kirti Nagar']]
_blue = [['b1', 'Noida Electronic City'], ['b2', 'Noida Sector 62'], ['b3', 'Noida Sector 59'], ['b4', 'Noida Sector 61'], ['b5', 'Noida Sector 52'], ['b6', 'Noida Sector 34'], ['b7', 'Noida City Centre'], ['b8', 'Golf Course'], ['b9', 'Botanical Garden'], ['b10', 'Noida Sect 18'], ['b11', 'Noida Sect 16'], ['b12', 'Noida Sect 15'], ['b13', 'New Ashok Nagar'], ['b14', 'Mayur Vihar Ext'], ['b15', 'Mayur Vihar-I'], ['b16', 'Akshardham'], ['b17', 'Yamuna Bank'], ['b18', 'Indraprasta'], ['b19', 'Supreme Court'], ['b20', 'Mandi House'], ['b21', 'Barakhamba'], ['b22', 'Rajiv Chowk'], ['b23', 'RK Ashram Marg'], ['b24', 'Jhandewalan'], ['b25', 'Karol Bagh'],
         ['b26', 'Rajendra Place'], ['b27', 'Patel Nagar'], ['b28', 'Shadi Pur'], ['b29', 'Kirti Nagar'], ['b30', 'Moti Nagar'], ['b31', 'Ramesh Nagar'], ['b32', 'Rajouri Garden'], ['b33', 'Tagore Garden'], ['b34', 'Subash Nagar'], ['b35', 'Tilak Nagar'], ['b36', 'Janak Puri East'], ['b37', 'Janak Puri West'], ['b38', 'Uttam Nagar East'], ['b39', 'Uttam Nagar West'], ['b40', 'Nawada'], ['b41', 'Dwaraka Mor'], ['b42', 'Dwarka'], ['b43', 'Dwarka Sector – 14'], ['b44', 'Dwarka Sector – 13'], ['b45', 'Dwarka Sector – 12'], ['b46', 'Dwarka Sector – 11'], ['b47', 'Dwarka Sector – 10'], ['b48', 'Dwarka Sector – 9'], ['b49', 'Dwarka Sector – 8'], ['b50', 'Dwarka Sector – 21']]
_bblue = [['B1', 'Yamuna Bank'], ['B2', 'Laxmi Nagar'], ['B3', 'Nirman Vihar'], ['B4', 'Preet Vihar'], [
    'B5', 'Karkar Duma'], ['B6', 'Anand Vihar'], ['B7', 'Kaushambi'], ['B8', 'Vaishali']]
_aqua = [['a1', 'Noida Sector 51'], ['a2', 'Noida Sector 50'], ['a3', 'Noida Sector 76'], ['a4', 'Noida Sector 101'], ['a5', 'Noida Sector 81'], ['a6', 'NSEZ'], ['a7', 'Noida Sector 83'], ['a8', 'Noida Sector 137'], ['a9', 'Noida Sector 142'], ['a10', 'Noida Sector 143'], [
    'a11', 'Noida Sector 144'], ['a12', 'Noida Sector 145'], ['a13', 'Noida Sector 146'], ['a14', 'Noida Sector 147'], ['a15', 'Noida Sector 148'], ['a16', 'Knowledge Park II'], ['a17', 'Pari Chowk'], ['a18', 'Alpha 1'], ['a19', 'Delta 1'], ['a20', 'GNIDA Office'], ['a21', 'Depot']]
_orange = [['o1', 'Dwarka Sector – 21'], ['o2', 'IGI Airport'], ['o3', 'Delhi Aerocity'], [
    'o4', 'Dhaula Kuan'], ['o5', 'Shivaji Stadium'], ['o6', 'New Delhi']]
_grey = [['g1', 'Dwarka'], ['g2', 'Nangli'], [
    'g3', 'Najafgarh'], ['g4', 'Dhansa Bus Stand']]
_rapid = [['R1', 'Sector 55 56'], ['R2', 'Sector 54 Chowk'], ['R3', 'Sector 53 54'], ['R4', 'Sector 42 43'], ['R5', 'Phase 1'], ['R6', 'Sikandarpur'], [
    'R7', 'Phase 2'], ['R8', 'Vodafone Belvedere Towers'], ['R9', 'Indusland Cyber City'], ['R10', 'Micromax Moulsari Avenue'], ['R11', 'Phase 3']]

_lines = [_yellow, _voilet, _red, _magenta, _pink, _green,
          _bgreen, _bblue, _blue, _orange, _aqua, _grey, _rapid]

_start = ""
_end = ""

all_stations = []
for i in _yellow:
    all_stations.append(i[1])
for i in _voilet:
    all_stations.append(i[1])
for i in _red:
    all_stations.append(i[1])
for i in _magenta:
    all_stations.append(i[1])
for i in _pink:
    all_stations.append(i[1])
for i in _green:
    all_stations.append(i[1])
for i in _bgreen:
    all_stations.append(i[1])
for i in _blue:
    all_stations.append(i[1])
for i in _bblue:
    all_stations.append(i[1])
for i in _aqua:
    all_stations.append(i[1])
for i in _orange:
    all_stations.append(i[1])
for i in _grey:
    all_stations.append(i[1])
for i in _rapid:
    all_stations.append(i[1])
all_stations = list(dict.fromkeys(all_stations))


def loc_set():
    moderate = True
    while moderate == True:
        print("Enter the starting point")
        n_start = input(": ")  # n_start = new start
        if n_start in all_stations:
            _start = n_start
            moderate = False
        else:
            print("Invalid input. Try again")
            print(all_stations)
    moderate = True
    while moderate == True:
        print("Enter the ending point")
        n_end = input(": ")  # n_end = new end
        if n_end in all_stations:
            _end = n_end
            moderate = False
        else:
            print("Invalid input. Try again")
            print(all_stations)
    return (_start, _end)


def find_line(station):
    line_list = []
    for i in _yellow:
        if station in i:
            l1 = ["_yellow", i[1], i[0]]  # yellow
            line_list.append(l1)
            continue
    for i in _magenta:
        if station in i:
            l1 = ["_magenta", i[1], i[0]]  # magenta
            line_list.append(l1)
            continue
    for i in _voilet:
        if station in i:
            l1 = ["_voilet", i[1], i[0]]  # voilet
            line_list.append(l1)
            continue
    for i in _red:
        if station in i:
            l1 = ["_red", i[1], i[0]]  # red
            line_list.append(l1)
            continue
    for i in _pink:
        if station in i:
            l1 = ["_pink", i[1], i[0]]  # pink
            line_list.append(l1)
            continue
    for i in _blue:
        if station in i:
            l1 = ["_blue", i[1], i[0]]  # blue
            line_list.append(l1)
            continue
    for i in _bblue:
        if station in i:
            l1 = ["_bblue", i[1], i[0]]  # _bblue
            line_list.append(l1)
            continue
    for i in _green:
        if station in i:
            l1 = ["_green", i[1], i[0]]
            line_list.append(l1)  # green
            continue
    for i in _bgreen:
        if station in i:
            l1 = ["_bgreen", i[1], i[0]]  # _bgreen
            line_list.append(l1)
            continue
    for i in _grey:
        if station in i:
            l1 = ["_grey", i[1], i[0]]  # grey
            line_list.append(l1)
            continue
    for i in _aqua:
        if station in i:
            l1 = ["_aqua", i[1], i[0]]  # aqua
            line_list.append(l1)
            continue
    for i in _rapid:
        if station in i:
            l1 = ["_rapid", i[1], i[0]]  # rapid
            line_list.append(l1)
            continue
    return (line_list)


_junction = ['Kashmere Gate', 'Central Secretariat', 'Hauz Khas', 'Azadpur', 'INA', 'Rajiv Chowk', 'New Delhi', 'Kalkaji Mandir', 'Lajpat Nagar', 'Mandi House', 'Netaji Subhash Place',
             'Welcome', 'Inderlok', 'Botanical Garden', 'Janak Puri West', 'Punjabi Bagh', 'Anand Vihar', 'Rajouri Garden', 'Ashok Park Main', 'Kirti Nagar', 'Yamuna Bank', 'Dwarka Sector – 21']


def single(_start, _end):
    l1 = find_line(_start)
    l2 = find_line(_end)
    e1 = []
    for i in l1:
        for j in l2:
            if i[0] == j[0]:
                r = abs(int(i[2][1:]) - int(j[2][1:]))
                e1.append(i)
                e1.append(j)
                e1.append(r)
            else:
                continue
    return e1


def double(_start, _end):
    l2 = []
    st_count = []
    for i in find_line(_start):
        for j in _junction:
            l1 = find_line(j)
            for m in l1:
                if i[0] == m[0]:
                    for k in find_line(_end):
                        for l in l1:
                            if l[0] == k[0]:
                                l2.append([i, m, l, k])
                            else:
                                continue
                            continue
                        continue
                    continue
                else:
                    continue
                continue
            continue
        continue
    for i in range(len(l2)):
        r = abs(int(l2[i][0][2][1:]) - int(l2[i][1][2][1:])) + \
            abs(int(l2[i][2][2][1:])-int(l2[i][3][2][1:]))
        st_count.append(r)
        continue
    if st_count == []:
        s_route = []
        return s_route
    else:
        _min = min(st_count)
        index = st_count.index(_min)
        s_route = l2[index]
        s_route.append(st_count[index])
        return s_route


def triple(_start, _end):
    e1 = []
    e2 = []
    e3 = []
    e4 = []
    if _start in _junction:
        _junction.remove(_start)
    if _end in _junction:
        _junction.remove(_end)
    for i in _junction:
        l3 = single(_start, i)
        e1.append(l3)
        continue
    for j in range(e1.count([])):
        e1.remove([])
        continue
    for k in range(len(e1)):
        st = e1[k][1][1]
        l4 = double(st, _end)
        e2.append(l4)
        continue
    for l in range(len(e2)):
        if e2[l] == []:
            continue
        else:
            l5 = e1[l]
            l5.extend(e2[l])
            e3.append(l5)
            continue
    for m in range(len(e3)):
        r = e3[m][7] + e3[m][2]
        e4.append(r)
        continue
    if e4 == []:
        s_route = []
        return s_route
    else:
        _min = min(e4)
        _index = e4.index(_min)
        s_route = e3[_index]
        s_route.append(e4[_index])
        return s_route


def start():
    _start, _end = loc_set()
    r = 0
    while r > -1:
        if r == 0:
            l1 = single(_start, _end)
            if l1 == []:
                r += 1
            else:
                print(
                    f"Start at {l1[0][1]} - {l1[0][0][1:]} line to {l1[1][1]} - {l1[1][0][1:]} line ")
                r = -1
        elif r == 1:
            l2 = double(_start, _end)
            if l2 == []:
                r += 1
            else:
                print(
                    f"Start at {l2[0][1]}-{l2[0][0][1:]} line to {l2[1][1]}-{l2[1][0][1:]} line ; {l2[2][1]}-{l2[2][0][1:]} line to {l2[3][1]}-{l2[3][0][1:]} line)")
                r = -1
        elif r == 2:
            l2 = triple(_start, _end)
            if l2 == []:
                r += 1
            else:
                print(f"Start at {l2[0][1]}-{l2[0][0][1:]} line to {l2[1][1]}-{l2[1][0][1:]} line ; {l2[3][1]}-{l2[3][0][1:]} line to {l2[4][1]}-{l2[4][0][1:]} line ; {l2[5][1]}-{l2[5][0][1:]} line to {l2[6][1]}-{l2[6][0][1:]} line")
                r = -1
        else:
            print("Route not found")
            r = -1


def start2():
    _start, _end = loc_set()
    r = 0
    uk = []
    l1 = single(_start, _end)
    l2 = double(_start, _end)
    l3 = triple(_start, _end)
    while r > -1:
        if r == 0:
            if l1 == []:
                uk.append(100)
                r += 1
            else:
                uk.append(l1[-1])
                r += 1
        elif r == 1:
            if l2 == []:
                uk.append(100)
                r += 1
            else:
                uk.append(l2[-1])
                r += 1
        elif r == 2:
            if l3 == []:
                uk.append(100)
                r += 1
            else:
                uk.append(l3[-1])
                r += 1
        else:
            print("HUH! YOU DID IT WRONG AGAIN")
            r = -1

    _min = min(uk)

    if _min == uk[0]:
        print(
            f"Start at {l1[0][1]} - {l1[0][0][1:]} line to {l1[1][1]} - {l1[1][0][1:]} line ")
    elif _min == uk[1]:
        print(f"Start at {l2[0][1]}-{l2[0][0][1:]} line to {l2[1][1]}-{l2[1][0][1:]} line ; {l2[2][1]}-{l2[2][0][1:]} line to {l2[3][1]}-{l2[3][0][1:]} line)")
    elif _min == uk[2]:
        print(f"Start at {l3[0][1]}-{l3[0][0][1:]} line to {l3[1][1]}-{l3[1][0][1:]} line ; {l3[3][1]}-{l3[3][0][1:]} line to {l3[4][1]}-{l3[4][0][1:]} line ; {l3[5][1]}-{l3[5][0][1:]} line to {l3[6][1]}-{l3[6][0][1:]} line")
    else:
        print("Die Asshole")


mod1 = True

print("Welcome to Delhi Metro Program")

while mod1 == True:
    print("Enter \n [0] to exit \n [1] to start \n [2] to get the list of all stations \n [3] to get the delhi metro map \n [4] for information about a station ")
    wee = input(": ")
    match wee:
        case '0':
            print("THE END")
            print("Thanks for using")
            print("Credits : Chirag Sugla")
            sleep(5)
            mod1 = False
        case '1':
            mod2 = True
            while mod2 == True:
                print(
                    "Enter \n [0] to exit \n [1] to find the best route with least line changing \n [2] to find the best route with least no. of stations")
                wee2 = input(": ")
                match wee2:
                    case '0':
                        mod2 = False
                    case '1':
                        l1 = start()
                    case '2':
                        l2 = start()
                    case _:
                        print("Wrong input. Please try again.")
        case '2':
            for i in all_stations:
                print(i)
        case '3':
            print("still in progress.")
        case '4':
            mod3 = True
            while mod3 == True:
                stat = input("Enter the name of the station: ")
                if stat not in all_stations:
                    print("Wrong Input. Please try again.")
                    print(all_stations)
                else:
                    l1 = find_line(stat)
                    for i in l1:
                        print(f"You will find {stat} on {i[0][1:]} line")
                    mod3 = False
        case _:
            print("Wrong input. Please try again.")