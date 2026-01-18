# Criação do arvivo
import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Agatha", "Tainá", "Wellington", "Guilherme", "Gabriel"]
}

df = pd.DataFrame(data)
df.to_csv("SDW2023.csv", index=False)

print("Arquivo SDW2023.csv criado com sucesso!")

#ETL
import pandas as pd
import json

# Extract

print("Iniciando etapa EXTRACT...")

# Lê o CSV e converte para lista de dicionários
users = pd.read_csv("SDW2023.csv").to_dict(orient="records")

# Garante a estrutura esperada
for user in users:
    user["news"] = []

print("Dados extraídos com sucesso:")
print(users)


# Transform

print("\nIniciando etapa TRANSFORM...")

def generate_ai_news(user):
    """
    Simulação de IA para geração de mensagens.
    Foco apenas no ETL
    """
    return (
        f"{user['name']}, Cada dado conta uma história, "
        "cabe a nós interpretá-la."
    )

# Gera mensagens personalizadas
for user in users:
    news = generate_ai_news(user)
    user["news"].append({
        "icon": "credit.svg",
        "description": news
    })

print("Mensagens geradas com sucesso:")
for user in users:
    print(f"{user['name']}: {user['news'][0]['description']}")


# Load

print("\nIniciando etapa LOAD...")

# Salvar em CSV
output_df = pd.DataFrame([
    {
        "id": user["id"],
        "name": user["name"],
        "message": user["news"][0]["description"]
    }
    for user in users
])

output_df.to_csv("mensagens_geradas.csv", index=False)

# Salvar em JSON
with open("resultado_final.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("Carga finalizada com sucesso!")
print("Arquivos gerados:")
print("- mensagens_geradas.csv")
print("- resultado_final.json")
