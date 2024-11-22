# Conjunto de dados
filmes = [
    {"nome": "Mad Max", "genero": "Ação"},
    {"nome": "Toy Story", "genero": "Comédia"},
    {"nome": "Invocação do Mal", "genero": "Terror"},
    {"nome": "O Rei Leão", "genero": "Animação"},
]

# Entrada do usuário
genero_preferido = input("Qual gênero você prefere (Ação, Comédia, Terror, Animação)? ").capitalize()

# Filtrar filmes
sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]

# Exibir sugestões
if sugestoes:
    print(f"Recomendamos os seguintes filmes de {genero_preferido}: {', '.join(sugestoes)}")
else:
    print("Desculpe, não temos sugestões para esse gênero.")
