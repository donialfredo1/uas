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

    mm1 = [c1a1, c1a2, c1a3]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C1 : ")
    print("=" * 40)
    if answers == "B":
        r11 = c1a1 / max(mm1)
        r12 = c1a2 / max(mm1)
        r13 = c1a3 / max(mm1)
    else:
        r11 = min(mm1) / c1a1
        r12 = min(mm1) / c1a2
        r13 = min(mm1) / c1a3

    print('r11 =', r11)
    print('r12 =', r12)
    print('r13 =', r13)
    print("=" * 40)

    mm2 = [c2a1, c2a2, c2a3]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C2 : ")
    print("=" * 40)
    if answers == "B":
        r21 = c2a1 / max(mm2)
        r22 = c2a2 / max(mm2)
        r23 = c2a3 / max(mm2)
    else:
        r21 = min(mm2) / c2a1
        r22 = min(mm2) / c2a2
        r23 = min(mm2) / c2a3

    print('r21 =', r21)
    print('r22 =', r22)
    print('r23 =', r23)
    print("=" * 40)

    mm3 = [c3a1, c3a2, c3a3]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        r31 = c3a1 / max(mm3)
        r32 = c3a2 / max(mm3)
        r33 = c3a3 / max(mm3)
    else:
        r31 = min(mm3) / c3a1
        r32 = min(mm3) / c3a2
        r33 = min(mm3) / c3a3

    print('r31 =', r31)
    print('r32 =', r32)
    print('r33 =', r33)
    print("=" * 40)

    mm4 = [c4a1, c4a2, c4a3]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C4 : ")
    print("=" * 40)
    if answers == "B":
        r41 = c4a1 / min(mm4)
        r42 = c4a2 / min(mm4)
        r43 = c4a3 / min(mm4)

    else:
        r41 = min(mm4) / c4a1
        r42 = min(mm4) / c4a2
        r43 = min(mm4) / c4a3

    print('r41 =', r41)
    print('r42 =', r42)
    print('r43 =', r43)
    print("=" * 40)

    mm5 = [c5a1, c5a2, c5a3]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C5 : ")
    print("=" * 40)
    if answers == "B":
        r51 = c5a1 / min(mm5)
        r52 = c5a2 / min(mm5)
        r53 = c5a3 / min(mm5)
    else:
        r51 = min(mm5) / c5a1
        r52 = min(mm5) / c5a2
        r53 = min(mm5) / c5a3

    print('r51 =', r51)
    print('r52 =', r52)
    print('r53 =', r53)

    v1 = (c1 * r11) + (c2 * r21) + (c3 * r31) + (c4 * r41) + (c5 * r51)
    v2 = (c1 * r12) + (c2 * r22) + (c3 * r32) + (c4 * r42) + (c5 * r52)
    v3 = (c1 * r13) + (c2 * r23) + (c3 * r33) + (c4 * r43) + (c5 * r53)

    print("=" * 40)
    print('V1', v1)
    print('V2', v2)
    print('V3', v3)
    print("=" * 40)

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

    mm1 = [c1a1, c1a2, c1a3, c1a4, c1a5]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C1 : ")
    print("=" * 40)
    if answers == "B":
        r11 = c1a1 / max(mm1)
        r12 = c1a2 / max(mm1)
        r13 = c1a3 / max(mm1)
        r14 = c1a4 / max(mm1)
        r15 = c1a5 / max(mm1)
    else:
        r11 = min(mm1) / c1a1
        r12 = min(mm1) / c1a2
        r13 = min(mm1) / c1a3
        r14 = min(mm1) / c1a4
        r15 = min(mm1) / c1a5

    print('r11 =', r11)
    print('r12 =', r12)
    print('r13 =', r13)
    print('r14 =', r14)
    print('r15 =', r15)
    print("=" * 40)

    mm2 = [c2a1, c2a2, c2a3, c2a4, c2a5]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C2 : ")
    print("=" * 40)
    if answers == "B":
        r21 = c2a1 / max(mm2)
        r22 = c2a2 / max(mm2)
        r23 = c2a3 / max(mm2)
        r24 = c2a4 / max(mm2)
        r25 = c2a5 / max(mm2)
    else:
        r21 = min(mm2) / c2a1
        r22 = min(mm2) / c2a2
        r23 = min(mm2) / c2a3
        r24 = min(mm2) / c2a4
        r25 = min(mm2) / c2a5

    print('r21 =', r21)
    print('r22 =', r22)
    print('r23 =', r23)
    print('r24 =', r24)
    print('r25 =', r25)
    print("=" * 40)

    mm3 = [c3a1, c3a2, c3a3, c3a4, c3a5]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C3 : ")
    print("=" * 40)
    if answers == "B":
        r31 = c3a1 / max(mm3)
        r32 = c3a2 / max(mm3)
        r33 = c3a3 / max(mm3)
        r34 = c3a4 / max(mm3)
        r35 = c3a5 / max(mm3)
    else:
        r31 = min(mm3) / c3a1
        r32 = min(mm3) / c3a2
        r33 = min(mm3) / c3a3
        r34 = min(mm3) / c3a4
        r35 = min(mm3) / c3a5

    print('r31 =', r31)
    print('r32 =', r32)
    print('r33 =', r33)
    print('r34 =', r34)
    print('r35 =', r35)
    print("=" * 40)

    mm4 = [c4a1, c4a2, c4a3, c4a4, c4a5]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C4 : ")
    print("=" * 40)
    if answers == "B":
        r41 = c4a1 / min(mm4)
        r42 = c4a2 / min(mm4)
        r43 = c4a3 / min(mm4)
        r44 = c4a4 / min(mm4)
        r45 = c4a5 / min(mm4)

    else:
        r41 = min(mm4) / c4a1
        r42 = min(mm4) / c4a2
        r43 = min(mm4) / c4a3
        r44 = min(mm4) / c4a4
        r45 = min(mm4) / c4a5

    print('r41 =', r41)
    print('r42 =', r42)
    print('r43 =', r43)
    print('r44 =', r44)
    print('r45 =', r45)
    print("=" * 40)

    mm5 = [c5a1, c5a2, c5a3, c5a4, c5a5]
    print('Menentukan Kriteria Benefit atau Cost padah variabel C1 - C5! B for Benefit C for Cost(C/B)')
    answers = input("C5 : ")
    print("=" * 40)
    if answers == "B":
        r51 = c5a1 / min(mm5)
        r52 = c5a2 / min(mm5)
        r53 = c5a3 / min(mm5)
        r54 = c5a4 / min(mm5)
        r55 = c5a5 / min(mm5)
    else:
        r51 = min(mm5) / c5a1
        r52 = min(mm5) / c5a2
        r53 = min(mm5) / c5a3
        r54 = min(mm5) / c5a4
        r55 = min(mm5) / c5a5

    print('r51 =', r51)
    print('r52 =', r52)
    print('r53 =', r53)
    print('r54 =', r54)
    print('r55 =', r55)
    print("=" * 40)

    v1 = (c1 * r11) + (c2 * r21) + (c3 * r31) + (c4 * r41) + (c5 * r51)
    v2 = (c1 * r12) + (c2 * r22) + (c3 * r32) + (c4 * r42) + (c5 * r52)
    v3 = (c1 * r13) + (c2 * r23) + (c3 * r33) + (c4 * r43) + (c5 * r53)
    v4 = (c1 * r14) + (c2 * r24) + (c3 * r34) + (c4 * r44) + (c5 * r54)
    v5 = (c1 * r15) + (c2 * r25) + (c3 * r35) + (c4 * r45) + (c5 * r55)

    print("=" * 40)
    print('V1', v1)
    print('V2', v2)
    print('V3', v3)
    print('V4', v4)
    print('V5', v5)
    print("=" * 40)

