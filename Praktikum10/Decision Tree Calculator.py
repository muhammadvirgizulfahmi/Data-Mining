from math import log2

yes = int(input("Masukkan total yes: "))
no = int(input("Masukkan total no: "))
n = yes + no

entropy_awal = -((yes/n) * log2(yes/n) + (no/n) * log2(no/n))
entropy_awal = round(entropy_awal, 3)

node_list = []
ig_list = []
node_unik_list = []
entropy_list = []
entropy_value_list = []
wa_list = []

node = int(input("Masukkan berapa atribut node dataset: "))
for a in range(1, node+1):
    node_spesifik = str(input(f"Masukkan nama atribut ke-{a}: "))
    node_unik = int(input(f"Masukkan berapa nilai unik {node_spesifik}: "))

    node_unik_list.append(node_unik)

    weighted_average = 0
    for b in range(1, node_unik+1):
        nama_unik = str(input(f"Masukkan nama unik ke-{b}: "))
        yes_unik = int(input(f"Masukkan jumlah yes {nama_unik}: "))
        no_unik = int(input(f"Masukkan jumlah no {nama_unik}: "))
        n_unik = yes_unik + no_unik
        entropy_spesifik = -((yes_unik/n_unik) * log2(yes_unik/n_unik) + (no_unik/n_unik) * log2(no_unik/n_unik))
        entropy_spesifik = round(entropy_spesifik, 3)
        weighted_average = weighted_average + ((n_unik/n) * entropy_spesifik)
        weighted_average = round(weighted_average, 3)

        entropy_list.append(nama_unik)
        entropy_value_list.append(entropy_spesifik)

    information_gain = entropy_awal - weighted_average
    information_gain = round(information_gain, 3)

    wa_list.append(weighted_average)
    node_list.append(node_spesifik)
    ig_list.append(information_gain)

print(entropy_list)
print(entropy_value_list)
print(node_unik_list)

print("\n---------------------------------")
print("E(S): ", entropy_awal)
for c in range(0, node):
    for d in node_unik_list:
        x = 0
        while x < d:
            print(f"E(S {entropy_list[x]}): {entropy_value_list[x]}")
            x = x + 1
    print(f"Weighted Average: {wa_list[c]}")
    print(f"Information Gain (S, {node_list[c]}): {ig_list[c]}")
print("---------------------------------")