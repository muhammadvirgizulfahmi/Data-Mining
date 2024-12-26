from math import log2
# print(-((3/6) * log2(3/6) + (3/6) * log2(3/6)))

yes = int(input("Masukkan total yes: "))
no = int(input("Masukkan total no: "))
n = yes + no

entropy_awal = -((yes/n) * log2(yes/n) + (no/n) * log2(no/n))
entropy_awal = round(entropy_awal, 3)
print("E(S) = ",entropy_awal)

node_list = []
ig_list = []
node = int(input("Ada berapa atribut node: "))
for a in range(0, node):
    node_spesifik = str(input("Apa nama atributnya: "))
    node_unik = int(input("Ada berapa nilai unik atribut: "))

    weighted_average = 0
    for b in range(1, node_unik+1):
        nama_unik = str(input(f"Apa nama unik ke-{b}: "))
        yes_unik = int(input(f"Berapa jumlah yes unik ke-{b}: "))
        no_unik = int(input(f"Berapa jumlah no unik ke-{b}: "))
        n_unik = yes_unik + no_unik
        entropy_spesifik = -((yes_unik/n_unik) * log2(yes_unik/n_unik) + (no_unik/n_unik) * log2(no_unik/n_unik))
        entropy_spesifik = round(entropy_spesifik, 3)
        print(f"{nama_unik},{entropy_spesifik}")
        weighted_average = weighted_average + ((n_unik/n) * entropy_spesifik)
        weighted_average = round(weighted_average, 3)

    print(node_spesifik, weighted_average)
    information_gain = entropy_awal - weighted_average
    information_gain = round(information_gain, 3)
    print(f"{information_gain} = {entropy_awal} - {weighted_average} ")

    node_list.append(node_spesifik)
    ig_list.append(information_gain)

print(node_list, ig_list)
for c in range(0, node):
    print(node_list[c],"\n",
    ig_list[c])