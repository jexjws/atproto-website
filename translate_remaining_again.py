import os
import re
import time
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text or not text.strip():
        return text
    try:
        translator = GoogleTranslator(source='en', target='zh-CN')
        res = translator.translate(text)
        return res if res else text
    except Exception as e:
        print(f"Translation failed for: {text[:30]}... Error: {e}")
        time.sleep(2)
        try:
            translator = GoogleTranslator(source='en', target='zh-CN')
            res = translator.translate(text)
            return res if res else text
        except Exception as e:
            return text

def translate_mdx_file(filepath):
    print(f"Translating: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []

    in_code_block = False

    for line in lines:
        if line.startswith('```'):
            new_lines.append(line)
            in_code_block = not in_code_block
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # Protect JSX tags roughly
        if re.search(r'<[A-Za-z]+', line) and not re.search(r'>.*<', line):
            new_lines.append(line)
            continue

        if re.match(r'^\s*</[A-Za-z]+>\s*$', line):
            new_lines.append(line)
            continue

        if re.match(r'^(import|export)\b', line):
            new_lines.append(line)
            continue

        if not line.strip() or (line.strip().startswith('<') and line.strip().endswith('>')):
            new_lines.append(line)
            continue

        # If line contains Chinese characters already, likely already translated
        if re.search(r'[\u4e00-\u9fff]', line):
            new_lines.append(line)
            continue

        if re.match(r'^(\s*[-*+]|\s*\d+\.)\s+(.*)', line):
            marker = re.match(r'^(\s*[-*+]|\s*\d+\.)\s+', line).group(0)
            text = line[len(marker):]
            translated = translate_text(text)
            if not translated: translated = text
            new_lines.append(f"{marker}{translated}")
            continue

        translated = translate_text(line)
        if not translated: translated = line
        new_lines.append(translated)

    final_content = '\n'.join(new_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)


files_to_translate = [
    'src/app/[locale]/guides/reading-data/zh-CN.mdx',
    'src/app/[locale]/guides/writing-data/zh-CN.mdx',
    'src/app/[locale]/guides/images-and-video/zh-CN.mdx',
    'src/app/[locale]/guides/installing-lexicons/zh-CN.mdx',
    'src/app/[locale]/guides/go-oauth-cli-tutorial/zh-CN.mdx'
]

for f in files_to_translate:
    translate_mdx_file(f)
    print(f"Finished {f}")
