import matplotlib.pyplot as plt
import numpy as np

## Cada cenario desse é uma configuração que você colocou no seu algoritmo.
## E para cada configuração, você executou 30 vezes.
## Os valores que estao nessa lista, exemplifica o resultado obtido da função objetivo em cada execução
## Você pode criar quantos cenarios quiser.
cenario_1 = [54.96714153, 48.61735699, 56.47688538, 65.23029856, 47.65846625, 47.65863043,
            65.79212816, 57.67434729, 45.30525614, 55.42560044, 45.36582307, 45.34270246,
            52.41962272, 30.86719755, 32.75082167, 44.37712471, 39.8716888,  53.14247333,
            40.91975924, 35.87696299, 64.65648769, 47.742237,   50.67528205, 35.75251814,
            44.55617275, 51.1092259,  38.49006423, 53.75698018, 43.9936131,  47.0830625]
cenario_2 = [52.77952065, 82.22733821, 59.8380333,  47.30746885, 69.87053895, 45.3498762,
            62.50636314, 36.48395851, 44.06176741, 62.36233483, 68.86159896, 62.05641937,
            58.61222061, 56.38675565, 42.25773612, 51.3618695,  54.47233475, 72.68546671,
            64.12341947, 38.84351814, 63.88900763, 55.37901264, 51.876936,   67.34011547,
            72.37199427, 71.17536143, 49.92938972, 56.28945149, 63.97516118, 71.70654153]
cenario_3 = [62.81238643, 67.21511535, 53.40497539, 52.05690064, 82.18788734, 90.34360043,
            68.91984818, 85.05299347, 75.42454038, 60.32320368, 75.42093408, 93.0705485,
            69.46260941, 93.46965484, 30.70382344, 82.32853757, 71.30570602, 65.51488974,
            71.37641165, 40.18646628, 66.70492168, 75.35668857, 92.16841067, 62.22594673,
            57.87259596, 62.47364435, 83.73103177, 74.93126664, 62.05359694, 77.6990115]


dados = [cenario_1, cenario_2, cenario_3]

# Criando o boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(dados, labels=['Cenário 1', 'Cenário 2', 'Cenário 3'])

# Adicionando título e rótulos aos eixos
plt.title('Boxplot de Execuções em Diferentes Cenários', fontsize=14)
plt.xlabel('Cenários', fontsize=12)
plt.ylabel('Valores das Execuções', fontsize=12)

# Mostrando o gráfico
plt.show()