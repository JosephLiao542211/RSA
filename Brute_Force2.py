from math import gcd
import time
import random
data_file = open('output.txt', 'a')

digit_7 =[1000033 ,
1000081 ,
1000099 ,
1000231 ,
1000669 ,
1000999 ,
1002341 ,
1002887 ,
1003001 ,
1005481 ,
1005581 ,
1005679 ,
1006301 ,
1008001 ,
1010003 ,
1010203 ,
1011001 ,
1012573 ,
1015423 ,
1015823 ,
1018253 ,
1023467 ,
1023487 ,
1023557 ,
1023571 ,
1023857,
1023947]
digit_8 = [10234589 ,
10234759 ,
10235647 ,
10235749 ,
10243657 ,
10282339 ,
10307137 ,
10312007 ,
10321919 ,
10392467 ,
10466689 ,
10620793 ,
10699181,
10699891,
20153153 ,
20200109 ,
20201231 ,
20202019 ,
20213233 ,
20388839 ,
20487359
]
digit_12 = [100123456789 ,
100529784361 ,
101103163367 ,
101107157131 ,
101111111111 ,
101234567897 ,
101601701401,
101740496633,
123462985007 ,
123511311277 ,
124567987631 ,
125411328001 ,
126704222713 ,
127397154761 ,
129866728583 ,
130147795189 ,
131681894401 ,
131707310437 ,
134141142143 ,
136363636361 ,
137168442221 ,
137438691329 ,
137438953481 ,
139149151157 ,
            ]
digit_15 = [18197520028579 ,
18285670562881 ,
18640889198609 ,
18691113008663 ,
18826507658281 ,
19489355557003 ,
19981091998181 ,
20215043836789 ,
20325153628489 ,
20479999999999 ,
20991129234731 ,
21732382677641 ,
]
digit_16= [1181118711931201 ,
1208152477719361 ,
1235711131175321 ,
1238926361552897 ,
1255571292290713 ,
1301477951890177 ,
1311753223571113 ,
1311870831664661 ,
1333333333333333 ,
1391098979592919 ,
1423214346574567 ,
1510553619999637 ,
1593350922240001 ,
1609161918110111 ,
1616668118999191 ,
1657688103077659 ,
1680588011350901 ,
1693182318746371,
1737476797107127 ]
digits_16p2 = [2231588810593399,
2345678911111111 ,
2355457523880889 ,
2357275332573527 ,
2357353373727757 ,
2380072466365871 ,
2468642135797531 ,
2573253757232573 ,
2744337540964913 ,
2828074326968519 ,
2856646544865959 ,
2956667885147129 ,
3129313031303131 ,
3325997869054417 ,
3391382115599173 ,
3733799929399999 ,
3931520917431241 ,
3940518300860411 ,
4429978144299823 ,
4444280714420857 ,
4547495153555759 ,
4564564564564561 ,
4847464544434241 ,
5111111111111119 ,
5944066965503999 ,
5953474341373129 ,
5999999999899999 ,
6171054912832631 ,
6241156164232441 ,
6435616333396997 ,
6664666366626661 ,
]
digit_18 = [100109100129100151 ,
102598800232111471 ,
111101234567891111 ,
100109100129100151 ,
102598800232111471 ,
111101234567891111 ,
113127131137139149 ,
115578717622022981 ,
117116115114112111 ,
124277066894534299 ,
137153163127255511 ,
139717391739171397 ,
147578905723456789 ,
153722867280912929 ,
159067808851610657 ,
160409920439929091 ,
161111111111111111 ,
165678739293946997 ,
166667166667000003 ,
169177178183185187 ,
180811181061181081 ,
191128877173556587 ]
digit_20 = [10089886811898868001 ,
10092003300140014003 ,
10093100991010310111 ,
10141516181932277123 ,
10611063106910871091 ,
10691097123712491259 ,
10911097110311091151 ,
11111111111111111011 ,
11111313171722335577 ,
11138479445180240497 ,
11976506590973322187 ,
12345678901234567891 ,
12345678910987654321 ,
12797382490434158663 ,
12904149405941903143 ,
13080048459073205527 ]

def factorization(n):

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors



systemRandom = random.SystemRandom()


for x in range(0, 12):
 Num1 = systemRandom.randint(1, 18)

 Num2 = systemRandom.randint(1, 18)

 if Num1 != Num2:
    start_time = time.time()
    a= str((factorization(digit_18[Num1]*digit_18[Num2])))
    data_file.write("\n")
    data_file.write(a)
    print(a)
    t= (" %s seconds" % (time.time() - start_time))
    data_file.write(t)
    print(t)
 else:
    print("Num1 and Num2 are the same")

