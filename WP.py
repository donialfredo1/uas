##33333333333333333333333333333333333333333333333333333333333 baris
print('ada berapa jumlah baris?')
ans = input()
print("-"*40)
if ans == "3":
    print("silahkan masukkan angka baris pertama")
    c1a1 = float(input("c1a1 : "))
    c2a1 = float(input("c2a1 : "))
    c3a1 = float(input("c3a1 : "))
    c4a1 = float(input("c4a1 : "))
    c5a1 = float(input("c5a1 : "))
    print("masukkan angka baris kedua")
    c1a2 = float(input("c1a2 : "))
    c2a2 = float(input("c2a2 : "))
    c3a2 = float(input("c3a2 : "))
    c4a2 = float(input("c4a2 : "))
    c5a2 = float(input("c5a2 : "))
    print("masukkan angka baris ketiga")
    c1a3 = float(input("c1a3 : "))
    c2a3 = float(input("c2a3 : "))
    c3a3 = float(input("c3a3 : "))
    c4a3 = float(input("c4a3 : "))
    c5a3 = float(input("c5a3 : "))

    print("masukkan angka bobot")
    c1 = float(input("c1 : "))
    c2 = float(input("c2 : "))
    c3 = float(input("c3 : "))
    c4 = float(input("c4 : "))
    c5 = float(input("c5 : "))

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C1 : ")
    print("=" * 40)
    if answers == "B":
        c1 = c1
    else:
        c1 = -c1

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C2 : ")
    print("=" * 40)
    if answers == "B":
        c2 = c2
    else:
        c2 = -c2

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c3 = c3
    else:
        c3 = -c3

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c4 = c4
    else:
        c4 = -c4

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c5 = c5
    else:
        c5 = -c5

    a = c1a1 ** c1
    aa = c2a1 ** c2
    aaa = c3a1 ** c3
    aaaa = c4a1 ** c4
    aaaaa = c5a1 ** c5

    b = c1a2 ** c1
    bb = c2a2 ** c2
    bbb = c3a2 ** c3
    bbbb = c4a2 ** c4
    bbbbb = c5a2 ** c5

    c = c1a3 ** c1
    cc = c2a3 ** c2
    ccc = c3a3 ** c3
    cccc = c4a3 ** c4
    ccccc = c5a3 ** c5

    S1 = float(a * aa * aaa * aaaa * aaaaa)
    S2 = float(b * bb * bbb * bbbb * bbbbb)
    S3 = float(c * cc * ccc * cccc * ccccc)

    print("")
    print("")
    print("S1 =", a, " x ", aa, " x ", aaa, " x ", aaaa, " x ", aaaaa)
    print("S1 = ", S1)
    print("")
    print("S2 =", b, " x ", bb, " x ", bbb, " x ", bbbb, " x ", bbbbb)
    print("S2 = ", S2)
    print("")
    print("S3 =", c, " x ", cc, " x ", ccc, " x ", cccc, " x ", ccccc)
    print("S3 = ", S3)
    print("")

    V1 = S1 / (S1 + S2 + S3)
    V2 = S2 / (S1 + S2 + S3)
    V3 = S3 / (S1 + S2 + S3)

    print("V1 = ", V1)
    print("V2 = ", V2)
    print("V3 = ", V3)

else:
    print("silahkan masukkan angka baris pertama")
    c1a1 = float(input("c1a1 : "))
    c2a1 = float(input("c2a1 : "))
    c3a1 = float(input("c3a1 : "))
    c4a1 = float(input("c4a1 : "))
    c5a1 = float(input("c5a1 : "))
    print("masukkan angka baris kedua")
    c1a2 = float(input("c1a2 : "))
    c2a2 = float(input("c2a2 : "))
    c3a2 = float(input("c3a2 : "))
    c4a2 = float(input("c4a2 : "))
    c5a2 = float(input("c5a2 : "))
    print("masukkan angka baris ketiga")
    c1a3 = float(input("c1a3 : "))
    c2a3 = float(input("c2a3 : "))
    c3a3 = float(input("c3a3 : "))
    c4a3 = float(input("c4a3 : "))
    c5a3 = float(input("c5a3 : "))
    print("masukkan angka baris keempat")
    c1a4 = float(input("c1a4 : "))
    c2a4 = float(input("c2a4 : "))
    c3a4 = float(input("c3a4 : "))
    c4a4 = float(input("c4a4 : "))
    c5a4 = float(input("c5a4 : "))
    print("masukkan angka baris kelima")
    c1a5 = float(input("c1a5 : "))
    c2a5 = float(input("c2a5 : "))
    c3a5 = float(input("c3a5 : "))
    c4a5 = float(input("c4a5 : "))
    c5a5 = float(input("c5a5 : "))

    print("masukkan angka bobot")
    c1 = float(input("c1 : "))
    c2 = float(input("c2 : "))
    c3 = float(input("c3 : "))
    c4 = float(input("c4 : "))
    c5 = float(input("c5 : "))

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C1 : ")
    print("=" * 40)
    if answers == "B":
        c1 = c1
    else:
        c1 = -c1

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C2 : ")
    print("=" * 40)
    if answers == "B":
        c2 = c2
    else:
        c2 = -c2

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c3 = c3
    else:
        c3 = -c3

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c4 = c4
    else:
        c4 = -c4

    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        c5 = c5
    else:
        c5 = -c5

    a = c1a1**c1
    aa = c2a1**c2
    aaa = c3a1**c3
    aaaa = c4a1**c4
    aaaaa = c5a1**c5

    b = c1a2**c1
    bb = c2a2**c2
    bbb = c3a2**c3
    bbbb = c4a2**c4
    bbbbb = c5a2**c5

    c = c1a3**c1
    cc = c2a3**c2
    ccc = c3a3**c3
    cccc = c4a3**c4
    ccccc = c5a3**c5

    d = c1a4**c1
    dd = c2a4**c2
    ddd = c3a4**c3
    dddd = c4a4**c4
    ddddd = c5a4**c5

    e = c1a5**c1
    ee = c2a5**c2
    eee = c3a5**c3
    eeee = c4a5**c4
    eeeee = c5a5**c5

    S1 = float(a * aa * aaa * aaaa * aaaaa)
    S2 = float(b * bb * bbb * bbbb * bbbbb)
    S3 = float(c * cc * ccc * cccc * ccccc)
    S4 = float(d * dd * ddd * dddd * ddddd)
    S5 = float(e * ee * eee * eeee * eeeee)

    # S1 = float(c1a1**c1 * c2a1**c2 * c3a1**c3 * c4a1**c4 * c5a1**c5)
    # S2 = float(c1a2**c1 * c2a2**c2 * c3a2**c3 * c4a2**c4 * c5a2**c5)
    # S3 = float(c1a3**c1 * c2a3**c2 * c3a3**c3 * c4a3**c4 * c5a3**c5)
    # S4 = float(c1a4**c1 * c2a4**c2 * c3a4**c3 * c4a4**c4 * c5a4**c5)
    # S5 = float(c1a5**c1 * c2a5**c2 * c3a5**c3 * c4a5**c4 * c5a5**c5)
    print("")
    print("")
    print("S1 =",a," x ",aa," x ",aaa," x ",aaaa," x ",aaaaa)
    print("S1 = ",S1)
    print("")
    print("S2 =",b," x ",bb," x ",bbb," x ",bbbb," x ",bbbbb)
    print("S2 = ",S2)
    print("")
    print("S3 =",c," x ",cc," x ",ccc," x ",cccc," x ",ccccc)
    print("S3 = ",S3)
    print("")
    print("S4 =",d," x ",dd," x ",ddd," x ",dddd," x ",ddddd)
    print("S4 = ",S4)
    print("")
    print("S5 =",e," x ",ee," x ",eee," x ",eeee," x ",eeeee)
    print("S5 = ",S5)
    print("")
    print("")

    V1 = S1 / (S1+S2+S3+S4+S5)
    V2 = S2 / (S1+S2+S3+S4+S5)
    V3 = S3 / (S1+S2+S3+S4+S5)
    V4 = S4 / (S1+S2+S3+S4+S5)
    V5 = S5 / (S1+S2+S3+S4+S5)

    print("V1 = ",V1)
    print("V2 = ",V2)
    print("V3 = ",V3)
    print("V4 = ",V4)
    print("V5 = ",V5)


