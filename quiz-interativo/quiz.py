import datetime

print("Bem-vindo ao Quiz de Tecnologia!")
print("----------------------------------")

nome = input("Digite seu nome: ")

pontos = 0

perguntas = [
    {
        "pergunta": "O que significa CPU?",
        "opcoes": ["1. Unidade Central de Processamento", "2. Central de Programas Unificados", "3. Computador Pessoal Universal"],
        "resposta": "1"
    },
    {
        "pergunta": "Qual linguagem é conhecida por ser usada na web junto com HTML e CSS?",
        "opcoes": ["1. Python", "2. JavaScript", "3. C++"],
        "resposta": "2"
    },
    {
        "pergunta": "Qual desses é um sistema operacional?",
        "opcoes": ["1. Google", "2. Windows", "3. Facebook"],
        "resposta": "2"
    },
    {
        "pergunta": "O que significa 'bug' na programação?",
        "opcoes": ["1. Um recurso novo", "2. Um erro ou falha", "3. Um tipo de software"],
        "resposta": "2"
    },
    {
        "pergunta": "Qual desses é um banco de dados?",
        "opcoes": ["1. MySQL", "2. Windows", "3. Instagram"],
        "resposta": "1"
    }
]

for q in perguntas:
    print("\n" + q["pergunta"])
    for opcao in q["opcoes"]:
        print(opcao)
    
    resposta_usuario = input("Digite o número da resposta: ")

    if resposta_usuario == q["resposta"]:
        print("✅ Correto!")
        pontos += 1
    else:
        print("❌ Errado!")

total_perguntas = len(perguntas)
porcentagem = (pontos / total_perguntas) * 100

print("\n=== Quiz concluído! ===")
print(f"{nome}, você acertou {pontos} de {total_perguntas} perguntas.")
print(f"Sua porcentagem de acertos foi: {porcentagem:.2f}%")

# Salvar resultado no arquivo
data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
with open("resultados.txt", "a") as arquivo:
    arquivo.write(f"{data} - {nome}: {pontos}/{total_perguntas} ({porcentagem:.2f}%)\n")

print("\nResultado salvo com sucesso no arquivo 'resultados.txt'!")
print("Obrigado por jogar! Pressione ENTER para sair.")
input()