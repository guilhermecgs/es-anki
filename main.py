import argparse
import json
from datetime import datetime

import requests


ANKI_CONNECT_URL = "http://127.0.0.1:8765"


def invoke_anki(action: str, params: dict) -> dict:
    payload = {"action": action, "version": 6, "params": params}
    response = requests.post(ANKI_CONNECT_URL, json=payload, timeout=10)
    response.raise_for_status()

    data = response.json()
    if data.get("error"):
        raise RuntimeError(f"Erro do AnkiConnect: {data['error']}")

    return data


def get_default_deck() -> str:
    """Retorna o primeiro deck disponível (Default, Padrão ou outro)."""
    data = invoke_anki("deckNames", {})
    names = data.get("result") or []
    for preferred in ("Default", "Padrão", "default"):
        if preferred in names:
            return preferred
    return names[0] if names else "Default"


def get_basic_model_and_fields() -> tuple[str, dict]:
    """Usa o modelo básico disponível (Basic ou Básico) e os nomes dos campos."""
    data = invoke_anki("modelNames", {})
    names = data.get("result") or []
    if "Básico" in names:
        return "Básico", {"Frente": None, "Verso": None}
    if "Basic" in names:
        return "Basic", {"Front": None, "Back": None}
    if names:
        # fallback: primeiro modelo e campos genéricos
        data = invoke_anki("modelFieldNames", {"modelName": names[0]})
        fields = {f: None for f in (data.get("result") or [])}
        return names[0], fields
    raise RuntimeError("Nenhum modelo de notas encontrado no Anki.")


def add_basic_flashcard(deck: str, front: str, back: str) -> int:
    if deck == "Default":
        deck = get_default_deck()
    model_name, field_map = get_basic_model_and_fields()
    fields = dict(field_map)
    keys = list(fields.keys())
    if len(keys) >= 2:
        fields[keys[0]], fields[keys[1]] = front, back
    else:
        fields[keys[0]] = f"{front}\n\n{back}" if keys else front

    note = {
        "deckName": deck,
        "modelName": model_name,
        "fields": fields,
        "options": {"allowDuplicate": False},
        "tags": ["script-uv", "ankiweb-sync"],
    }

    data = invoke_anki("addNote", {"note": note})
    return data["result"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cria um flashcard no Anki via AnkiConnect."
    )
    parser.add_argument(
        "--deck",
        default="Default",
        help="Nome do deck (padrao: Default).",
    )
    parser.add_argument(
        "--front",
        default=f"Pergunta criada em {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        help="Conteudo da frente do card.",
    )
    parser.add_argument(
        "--back",
        default="Resposta gerada por script Python com uv.",
        help="Conteudo do verso do card.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        note_id = add_basic_flashcard(args.deck, args.front, args.back)
    except requests.exceptions.RequestException as exc:
        raise SystemExit(
            "Nao consegui conectar ao AnkiConnect em http://127.0.0.1:8765. "
            "Abra o Anki Desktop e instale/ative o add-on AnkiConnect."
        ) from exc
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc

    print(json.dumps({"status": "ok", "note_id": note_id}, ensure_ascii=True))


if __name__ == "__main__":
    main()
