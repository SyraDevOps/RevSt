from core.builder import RevistaBuilder

def main():
    builder = RevistaBuilder(
        config_path='config.yaml',
        dados_path='data/conteudo.json'
    )
    builder.gerar()
    print("Revista gerada com sucesso!")

if __name__ == '__main__':
    main()
