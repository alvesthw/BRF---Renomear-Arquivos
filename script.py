import os
import sys
import re

# Caminho da pasta onde o script está
pasta_principal = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__))

# Extensões de imagem válidas
extensoes_imagem = ['.is2']

# Remove caracteres inválidos para nomes de arquivos/pastas no Windows
def limpar_nome(nome):
    return re.sub(r'[<>:"/\\|?*\n\r]', '', nome)

# Gera nome único com sufixo (1), (2), etc.
def gerar_nome_unico(caminho_pasta, nome_base, extensao):
    contador = 1
    while True:
        novo_nome = f"{nome_base} ({contador}){extensao}"
        caminho_novo = os.path.join(caminho_pasta, novo_nome)
        if not os.path.exists(caminho_novo):
            return caminho_novo
        contador += 1

# Percorre todas as subpastas
for nome_pasta in os.listdir(pasta_principal):
    caminho_pasta_original = os.path.join(pasta_principal, nome_pasta)

    if os.path.isdir(caminho_pasta_original):
        nome_pasta_limpo = limpar_nome(nome_pasta)

        # Renomeia a pasta se o nome estiver inválido
        if nome_pasta != nome_pasta_limpo:
            caminho_pasta_limpo = os.path.join(pasta_principal, nome_pasta_limpo)
            try:
                os.rename(caminho_pasta_original, caminho_pasta_limpo)
                print(f"Pasta renomeada: {nome_pasta} -> {nome_pasta_limpo}")
                caminho_pasta = caminho_pasta_limpo
            except Exception as e:
                print(f"Erro ao renomear pasta {nome_pasta}: {e}")
                continue
        else:
            caminho_pasta = caminho_pasta_original

        # Renomeia os arquivos .is2 dentro da pasta
        for nome_arquivo in sorted(os.listdir(caminho_pasta)):
            nome, extensao = os.path.splitext(nome_arquivo)
            if extensao.lower() in extensoes_imagem:
                caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
                caminho_novo = gerar_nome_unico(caminho_pasta, nome_pasta_limpo, extensao.lower())

                try:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {nome_arquivo} -> {os.path.basename(caminho_novo)}")
                except Exception as e:
                    print(f"Erro ao renomear {nome_arquivo}: {e}")

print("Renomeação concluída.")
input("Pressione Enter para sair...")
