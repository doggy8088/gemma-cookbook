import json
import pathlib
import re
import sys
from functools import lru_cache

from deep_translator import GoogleTranslator


ROOT = pathlib.Path(__file__).resolve().parents[1]
GLOSSARY_PATH = ROOT / "docs" / "translation-glossary.zh-TW.md"

KEEP_ENGLISH_EXTRA = [
    "Google Colab",
    "Hugging Face",
    "Hugging Face Hub",
    "Transformers.js",
    "ONNX Runtime",
    "ONNX Runtime Web",
    "MediaPipe",
    "MediaPipe LLM Inference API",
    "Google GenAI SDK",
    "OpenAI SDK",
    "Visual Studio Code",
    "Android Studio",
    "Cloud Run",
    "Vertex AI",
    "Model Garden",
    "Secret Manager",
    "Jupyter",
    "GitHub",
    "Keras",
    "JAX",
    "PyTorch",
    "Flax",
    "LoRA",
    "QLoRA",
    "DPO",
    "RAG",
    "MMLU",
    "WebGPU",
    "JavaScript",
    "Python",
    "FastAPI",
    "Gradio",
    "Ollama",
    "LlamaCpp",
    "Transformers",
    "Gemini",
    "token",
    "tokens",
    "runtime",
    "notebook",
    "cell",
    "cells",
    "prompt",
    "system prompt",
    "chatbot",
    "streaming",
    "agent",
    "agentic",
    "inference",
    "fine-tuning",
    "finetuning",
]

NORMALIZE_REPLACEMENTS = {
    "筆記本": "notebook",
    "筆記本電腦": "laptop",
    "令牌": "token",
    "運行": "執行",
    "運作時間": "runtime",
    "執行階段": "runtime",
    "教程": "教學",
    "教學課程": "教學",
    "視窗": "視窗",
    "配置": "設定",
    "程式庫": "library",
    "擴充功能": "extension",
    "部落格": "blog",
    "資料集": "dataset",
    "推理": "推論",
    "本notebook": "此 notebook",
    "此notebook": "此 notebook",
    "您的 HF token": "HF token",
    "設定您的 HF token": "設定 HF token",
    "抱臉": "Hugging Face",
    "版權所有": "Copyright",
}

PROTECTED_LINE_PATTERNS = [
    re.compile(r"^\s*```"),
    re.compile(r"^\s*~~~"),
    re.compile(r"^\s*<pre>"),
    re.compile(r"^\s*</pre>"),
    re.compile(r"^\s*\$ "),
    re.compile(r"^\s*!"),
    re.compile(r"^\s*%"),
    re.compile(r"^\s*import "),
    re.compile(r"^\s*from "),
    re.compile(r"^\s*[A-Za-z0-9_./\\-]+\s*=\s*"),
]

TRANSLATOR = GoogleTranslator(source="auto", target="zh-TW")


def parse_keep_english_terms() -> list[str]:
    terms = []
    if GLOSSARY_PATH.exists():
        for line in GLOSSARY_PATH.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) < 5 or parts[0] == "English term":
                continue
            term, _, policy, _, _ = parts[:5]
            if "keep English" in policy:
                terms.append(term)
    terms.extend(KEEP_ENGLISH_EXTRA)
    return sorted(set(terms), key=len, reverse=True)


KEEP_ENGLISH_TERMS = parse_keep_english_terms()


def protect_terms(text: str) -> tuple[str, dict[str, str]]:
    protected = {}
    counter = 0

    def stash(value: str) -> str:
        nonlocal counter
        key = f"@@P{counter:04d}@@"
        counter += 1
        protected[key] = value
        return key

    def replace_pattern(pattern: re.Pattern[str], value: str) -> str:
        return pattern.sub(lambda m: stash(m.group(0)), value)

    text = replace_pattern(re.compile(r"```[\s\S]*?```", re.MULTILINE), text)
    text = replace_pattern(re.compile(r"~~~[\s\S]*?~~~", re.MULTILINE), text)
    text = replace_pattern(re.compile(r"`[^`\n]+`"), text)
    text = replace_pattern(re.compile(r"(?<=\]\()([^)\n]+)(?=\))"), text)
    text = replace_pattern(re.compile(r"(?<=src=\")([^\"]+)(?=\")"), text)
    text = replace_pattern(re.compile(r"(?<=href=\")([^\"]+)(?=\")"), text)
    text = replace_pattern(re.compile(r"https?://[^\s)>\"]+"), text)
    text = replace_pattern(re.compile(r"</?[^>\n]+>"), text)

    for term in KEEP_ENGLISH_TERMS:
        if term and term in text:
            text = text.replace(term, stash(term))

    return text, protected


def restore_terms(text: str, protected: dict[str, str]) -> str:
    changed = True
    while changed:
        changed = False
        for key, value in protected.items():
            if key in text:
                text = text.replace(key, value)
                changed = True
    return text


@lru_cache(maxsize=10000)
def translate_text(text: str) -> str:
    if not text.strip():
        return text
    try:
        translated = TRANSLATOR.translate(text)
    except Exception:
        translated = text
    if translated is None:
        translated = text
    if "Error 500 (Server Error)" in translated:
        parts = re.split(r"(\n+)", text)
        if len(parts) > 1:
            return "".join(translate_text(part) if not re.fullmatch(r"\n+", part or "") else part for part in parts)
        sentence_parts = re.split(r"([.!?]\s+)", text)
        if len(sentence_parts) > 1:
            rebuilt = []
            for part in sentence_parts:
                if re.fullmatch(r"[.!?]\s+", part or ""):
                    rebuilt.append(part)
                elif part:
                    rebuilt.append(TRANSLATOR.translate(part))
            return "".join(rebuilt)
        return text
    return translated


def normalize_text(text: str) -> str:
    for src, dst in NORMALIZE_REPLACEMENTS.items():
        text = text.replace(src, dst)
    text = re.sub(r"Google Colab 中執行", "在 Google Colab 中執行", text)
    text = re.sub(r"\bHF 令牌\b", "HF token", text)
    text = re.sub(r"\bAPI 金鑰\b", "API key", text)
    text = re.sub(r"\b模型 家族\b", "模型家族", text)
    text = re.sub(r"\bColab 和 Gemma 功能\b", "Gemma 存取權限", text)
    text = re.sub(r"Gemma設置", "Gemma 設定", text)
    text = re.sub(r"Gemma設定", "Gemma 設定", text)
    text = re.sub(r"打開", "開啟", text)
    text = re.sub(r"點擊", "點選", text)
    text = re.sub(r"秘密標籤", "Secrets 標籤", text)
    text = re.sub(r"機密管理器", "Secrets manager", text)
    text = re.sub(r"新的secret", "新的 secret", text)
    text = re.sub(r"允許notebook", "允許 notebook", text)
    text = re.sub(r"透過點選", "透過點選", text)
    text = re.sub(r"複製/貼上", "複製/貼上", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])notebook", " notebook", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])runtime", " runtime", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])token", " token", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])secret", " secret", text)
    text = re.sub(r"(?<=[A-Za-z])(?=[\u4e00-\u9fff])", " ", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])(?=[A-Za-z])", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text


def split_prefix(line: str) -> tuple[str, str]:
    patterns = [
        r"^(\s{0,3}#{1,6}\s+)",
        r"^(\s{0,3}>\s+)",
        r"^(\s{0,3}[-*+]\s+)",
        r"^(\s{0,3}\d+\.\s+)",
    ]
    for pattern in patterns:
        m = re.match(pattern, line)
        if m:
            return m.group(1), line[m.end():]
    return "", line


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and set(stripped.replace("|", "").replace(":", "").replace("-", "").replace(" ", "")) == set()


def translate_table_row(line: str) -> str:
    leading = line[: len(line) - len(line.lstrip())]
    stripped = line.strip()
    if not stripped.startswith("|") or is_table_separator(line):
        return line
    parts = stripped.split("|")
    translated = []
    for idx, part in enumerate(parts):
        if idx == 0 or idx == len(parts) - 1:
            translated.append(part)
            continue
        cell = part.strip()
        if not cell:
            translated.append(part)
            continue
        protected_text, protected = protect_terms(cell)
        translated_cell = translate_text(protected_text)
        translated_cell = restore_terms(normalize_text(translated_cell), protected)
        translated.append(f" {translated_cell} ")
    return leading + "|".join(translated)


def should_keep_line(line: str, in_fence: bool) -> bool:
    if in_fence:
        return True
    if not line.strip():
        return True
    if is_table_separator(line):
        return True
    if line.startswith("    ") and not line.lstrip().startswith(("* ", "- ", "+ ")):
        return True
    return any(pattern.search(line) for pattern in PROTECTED_LINE_PATTERNS)


def translate_line(line: str, in_fence: bool) -> str:
    if should_keep_line(line, in_fence):
        return line
    if line.strip().startswith("|"):
        return translate_table_row(line)
    newline = "\n" if line.endswith("\n") else ""
    body = line[:-1] if newline else line
    prefix, content = split_prefix(body)
    protected_text, protected = protect_terms(content)
    if not protected_text.strip():
        return line
    translated = translate_text(protected_text)
    translated = restore_terms(normalize_text(translated), protected)
    return prefix + translated + newline


def translate_block(text: str) -> str:
    protected_text, protected = protect_terms(text)
    if not protected_text.strip():
        return text
    translated = translate_text(protected_text)
    return restore_terms(normalize_text(translated), protected)


def is_prefixed_markdown_line(line: str) -> bool:
    return bool(
        re.match(r"^\s{0,3}(#{1,6}\s+|>\s+|[-*+]\s+|\d+\.\s+)", line)
    )


def translate_markdown_source(text: str) -> str:
    lines = text.splitlines(True)
    out = []
    paragraph_buffer = []
    in_fence = False

    def flush_paragraph_buffer() -> None:
        nonlocal paragraph_buffer
        if not paragraph_buffer:
            return
        block = "".join(paragraph_buffer)
        out.append(translate_block(block))
        paragraph_buffer = []

    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            flush_paragraph_buffer()
            out.append(line)
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(line)
            continue
        if not line.strip():
            flush_paragraph_buffer()
            out.append(line)
            continue
        if line.strip().startswith("|"):
            flush_paragraph_buffer()
            out.append(translate_table_row(line))
            continue
        if should_keep_line(line, in_fence):
            flush_paragraph_buffer()
            out.append(line)
            continue
        if is_prefixed_markdown_line(line):
            flush_paragraph_buffer()
            out.append(translate_line(line, in_fence))
            continue
        paragraph_buffer.append(line)
    flush_paragraph_buffer()
    return "".join(out)


def translate_notebook(path: pathlib.Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = "".join(cell.get("source", []))
        translated = translate_markdown_source(source)
        if translated != source:
            cell["source"] = translated.splitlines(True)
            changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    targets = [pathlib.Path(arg) for arg in sys.argv[1:]] or list(ROOT.rglob("*.ipynb"))
    changed_count = 0
    for rel in targets:
        path = rel if rel.is_absolute() else ROOT / rel
        if not path.exists():
            print(f"missing\t{rel}")
            continue
        changed = translate_notebook(path)
        print(f"{'changed' if changed else 'skipped'}\t{path.relative_to(ROOT)}")
        if changed:
            changed_count += 1
    print(f"changed_count={changed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
