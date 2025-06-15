import yaml
import os

def carregar_config(caminho='config.yaml'):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho}")

    with open(caminho, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Valores padrão, caso não estejam definidos no YAML
    config_padrao = {
        'nome_arquivo': 'revista_SYN',
        'fonte_padrao': 'Helvetica',
        'tamanho_fonte': 11,
        'cores': {
            'primaria': '#7A00FF',
            'fundo_claro': '#FFFFFF',
            'fundo_escuro': '#121212',
            'texto_claro': '#FFFFFF',
            'texto_escuro': '#121212'
        },
        'padding': {
            'margem_superior': 3,
            'margem_inferior': 2,
            'margem_lateral': 2
        },
        'qr': {
            'url_base': 'https://syradevops.com/syn/edicoes'
        }
    }

    # Preencher com padrões caso alguma chave esteja faltando
    def preencher_defaults(base, defaults):
        for chave, valor in defaults.items():
            if chave not in base:
                base[chave] = valor
            elif isinstance(valor, dict):
                preencher_defaults(base[chave], valor)

    preencher_defaults(config, config_padrao)
    return config
