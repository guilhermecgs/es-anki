# ankiweb-flashcard

Crie flashcards otimizados para memorização e sincronize com o Anki.

## Estrutura

```
flashcards/          ← cards gerados (Markdown), legíveis no editor
sync_anki.py         ← envia cards novos para o Anki e grava anki_id de volta
main.py              ← cria um card avulso via CLI (uso simples)
```

## Fluxo de uso

1. **Gere flashcards** usando a Cursor Skill `create-flashcards` (diga "crie flashcards sobre X" ou anexe uma imagem).
2. Os cards são salvos em `flashcards/` como arquivos `.md`.
3. Revise no editor — cada card é legível e editável.
4. Quando quiser enviar para o Anki:

```bash
uv run python sync_anki.py
```

5. O script grava o `anki_id` de volta no arquivo — rodar novamente não cria duplicatas.
6. No Anki Desktop, clique **Sync** para enviar ao AnkiWeb.

## Comandos

```bash
# Preview sem enviar
uv run python sync_anki.py --dry-run

# Sync de verdade
uv run python sync_anki.py

# Criar um card avulso (sem salvar em arquivo)
uv run python main.py --front "Pergunta?" --back "Resposta"
```

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado
- Anki Desktop com o add-on **AnkiConnect** (código `2055492159`)
