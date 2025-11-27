import os

FILTER_DIR = "filters"
OUTPUT_FILE = "ultimateadguardfilter.txt"

def listar_arquivos(pasta):
    return [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.endswith(".txt")
    ]

def validar_linha(linha):
    linha = linha.strip()

    if not linha:
        return False

    if linha.startswith("<"):
        return False

    if any(tag in linha.lower() for tag in ["doctype", "html", "style", "meta", "body"]):
        return False

    return True

def ler_arquivo_local(caminho):
    regras = []
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            if validar_linha(linha):
                regras.append(linha.strip())
    return regras

def salvar_arquivo_saida(saida, regras):
    with open(saida, "w", encoding="utf-8") as f:
        for r in sorted(regras):
            f.write(r + "\n")

def main():
    arquivos = listar_arquivos(FILTER_DIR)
    todas_regras = set()

    for arq in arquivos:
        conteudo = ler_arquivo_local(arq)
        todas_regras.update(conteudo)

    salvar_arquivo_saida(OUTPUT_FILE, todas_regras)
    print(f"Gerado: {OUTPUT_FILE} ({len(todas_regras)} regras)")

if __name__ == "__main__":
    main()

