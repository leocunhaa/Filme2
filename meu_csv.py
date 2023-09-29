import csv

# Dados
data = [
    {"Nome": "Leo", "Filme": "VelozesEFuriosos"},
    {"Nome": "robesin", "Filme": "ODatePerfeito"},
    {"Nome": "serjao", "Filme": "VelozesEFuriosos"},
    {"Nome": "jennifer", "Filme": "ODatePerfeito"},
    {"Nome": "claudio", "Filme": "EsposaDeMentirinha"},
    {"Nome": "ZeAnderson", "Filme": "EsposaDeMentirinha"},
    {"Nome": "abella", "Filme": "ODatePerfeito"},
    {"Nome": "marcos", "Filme": "VelozesEFuriosos"},
    {"Nome": "anderson", "Filme": "ODatePerfeito"}
]

# Escrevendo no arquivo CSV
with open('dados.csv', mode='w', newline='') as file:
    fieldnames = ['Nome', 'Filme']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Arquivo CSV criado com sucesso.")
