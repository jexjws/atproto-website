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
        print(f"Translation failed for: {text[:30]}... Error: {e}")
        time.sleep(2)
        try:
            translator = GoogleTranslator(source='en', target='zh-CN')
            res = translator.translate(text)
            return res if res else text
        except Exception as e:
            return text

def translate_headers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find export const header
    header_match = re.search(r'export const header = \{([^\}]+)\}', content)
    if not header_match:
        return

    header_content = header_match.group(1)

    desc_match = re.search(r"description:\s*['\"]([^'\"]+)['\"]", header_content)

    if desc_match:
        desc = desc_match.group(1)
        if re.search(r'[a-zA-Z]', desc) and not re.search(r'[\u4e00-\u9fff]', desc):
            translated_desc = translate_text(desc)
            if translated_desc:
                # Escape single quotes in translation if using single quotes for string
                translated_desc = translated_desc.replace("'", "\\'")
                new_header = content[:desc_match.start(1)] + translated_desc + content[desc_match.end(1):]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_header)
                print(f"Translated header description in: {filepath}")

for root, _, files in os.walk('src/app/[locale]'):
    for file in files:
        if file.endswith('zh-CN.mdx'):
            path = os.path.join(root, file)
            translate_headers(path)
