def principal():
    ano_atual = 2022

    # Solicita o nome do usuário
    nome = input("Digite seu nome completo: ").strip()

    while True:
        try:
            # Solicita o ano de nascimento
            ano_nascimento = input("Digite o ano do seu nascimento (entre 1922 e 2021): ").strip()
            ano_nascimento = int(ano_nascimento)

            # Verifica se o ano está no intervalo permitido
            if 1922 <= ano_nascimento <= 2021:
                idade = ano_atual - ano_nascimento
                print(f"\n{nome}, você completou ou completará {idade} anos em {ano_atual}.")
                break
            else:
                print("Ano inválido. Digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    principal()