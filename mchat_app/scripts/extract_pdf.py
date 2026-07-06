"""Script de desenvolvimento: extrai o texto bruto do PDF oficial do M-CHAT-R/F.

Uso: python3 mchat_app/scripts/extract_pdf.py
Não é importado pelo app em runtime - serve apenas para gerar o texto que é
transcrito manualmente (validado) para mchat_app/content/items.py.
"""

from pathlib import Path

import pypdf

PDF_PATH = Path(__file__).resolve().parent.parent / "assets" / "MCHATR_F_Brazilian_Portuguese_v2.pdf"


def main() -> None:
    reader = pypdf.PdfReader(PDF_PATH)
    print(f"Total de páginas: {len(reader.pages)}\n")
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        print(f"\n{'=' * 20} PÁGINA {i} {'=' * 20}\n")
        print(text)


if __name__ == "__main__":
    main()
