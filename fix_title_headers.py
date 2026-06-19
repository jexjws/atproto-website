import os
import re
import time
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text.strip():
        return text
    try:
        translator = GoogleTranslator(source='en', target='zh-CN')
        res = translator.translate(text)
        return res if res else text
    except Exception as e:
        time.sleep(1)
        try:
            translator = GoogleTranslator(source='en', target='zh-CN')
            res = translator.translate(text)
            return res if res else text
        except:
            return text

def translate_headers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    header_match = re.search(r'export const header = \{([^\}]+)\}', content)
    if not header_match:
        return

    header_content = header_match.group(1)

    title_match = re.search(r"title:\s*['\"]([^'\"]+)['\"]", header_content)

    changed = False

    if title_match:
        title = title_match.group(1)
        if re.search(r'[a-zA-Z]', title) and not re.search(r'[\u4e00-\u9fa5]', title):
            translated_title = translate_text(title)
            if translated_title:
                translated_title = translated_title.replace("'", "\\'")
                content = content[:title_match.start(1)] + translated_title + content[title_match.end(1):]
                changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Translated header title in: {filepath}")

for root, _, files in os.walk('src/app/[locale]'):
    for file in files:
        if file.endswith('zh-CN.mdx'):
            path = os.path.join(root, file)
            translate_headers(path)
