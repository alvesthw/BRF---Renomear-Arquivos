# 🖼️ Renomeador de Imagens .IS2 por Pasta

Este script em Python foi desenvolvido para automatizar o processo de **renomear arquivos de imagem com extensão `.is2`** dentro de subpastas, utilizando o nome da pasta como base para o novo nome do arquivo.

---

## ✅ Funcionalidades

- 🔍 **Busca automática** por subpastas dentro da pasta principal onde o script está localizado.
- 🖼️ **Renomeia arquivos `.is2`** com base no nome da pasta onde estão localizados.
- 🔢 Adiciona **numeração sequencial entre parênteses** no final do nome do arquivo, como `(1)`, `(2)`, `(3)` etc.
- 🧼 **Sanitiza nomes de pastas**, removendo ou substituindo caracteres inválidos (como `%`, quebras de linha, `*`, `?`, etc.) para evitar erros no sistema de arquivos.
- 🛡️ **Tratamento de erros**: exibe mensagens claras caso algum arquivo não possa ser renomeado.

---

## 🗂️ Exemplo de Funcionamento

### Estrutura Original:
📁 Projeto/ ├── 📁 QEF030006109%0ACCM+GFI+COND+1.8+-+COL+8%0ASL+PAINEIS+COND+GFI/ │ ├── imagem1.is2 │ ├── imagem2.is2

### Após execução:
📁 Projeto/ ├── 📁 QEF030006109%0ACCM+GFI+COND+1.8+-+COL+8%0ASL+PAINEIS+COND+GFI/ │ ├── QEF030006109_CCM+GFI+COND+1.8+-+COL+8_SL+PAINEIS+COND+GFI_(1).is2 │ ├── QEF030006109_CCM+GFI+COND+1.8+-+COL+8_SL+PAINEIS+COND+GFI_(2).is2
---

## ⚙️ Como Usar

1. Coloque o script na **pasta principal** que contém as subpastas com os arquivos `.is2`.
2. Execute o script com Python 3:
   ```bash
   python renomear_imagens.py

# 🛠️ Criando Arquivos `.exe` com PyInstaller

Este guia explica como transformar um script Python (`.py`) em um executável `.exe` para Windows usando o **PyInstaller**, e destaca a diferença entre usar ou não o parâmetro `--noconsole`.

---

## 📦 O que é o PyInstaller?

O PyInstaller é uma ferramenta que empacota scripts Python em executáveis independentes, permitindo que você rode seus programas em máquinas que **não têm Python instalado**.

---

## ✅ Como criar um `.exe`

1. **Instale o PyInstaller** (se ainda não tiver):
   ```bash
   pip install pyinstaller
   ```
2. **criar o executavel**
 ```bash
   pyinstaller --onefile nome_do_seu_script.py
   ```

# Com console (ideal para scripts com input/print)
pyinstaller --onefile renomear_imagens.py

# Sem console (ideal para apps com interface gráfica)
pyinstaller --onefile --noconsole renomear_imagens.py

