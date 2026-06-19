import os
import re

def fix_headers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sometimes title gets description mashed into it: title: '即将投入生产改进 Atmosphere 堆栈部署以供大规模生产使用production use at scale',
    header_match = re.search(r'export const header = \{([^\}]+)\}', content)
    if not header_match:
        return

    header_content = header_match.group(1)

    # Let's just fix it by looking up the english original if the Chinese one is missing a description
    if 'description:' not in header_content:
        en_filepath = filepath.replace('zh-CN.mdx', 'en.mdx')
        if os.path.exists(en_filepath):
            with open(en_filepath, 'r', encoding='utf-8') as en_f:
                en_content = en_f.read()
            en_header_match = re.search(r'export const header = \{([^\}]+)\}', en_content)
            if en_header_match:
                # We'll just replace the whole header with the translated English one
                from deep_translator import GoogleTranslator
                translator = GoogleTranslator(source='en', target='zh-CN')
                en_header = en_header_match.group(1)

                title_match = re.search(r"title:\s*['\"]([^'\"]+)['\"]", en_header)
                desc_match = re.search(r"description:\s*['\"]([^'\"]+)['\"]", en_header)

                new_header = 'export const header = {\n'
                if title_match:
                    t = translator.translate(title_match.group(1)).replace("'", "\\'")
                    new_header += f"  title: '{t}',\n"
                if desc_match:
                    d = translator.translate(desc_match.group(1)).replace("'", "\\'")
                    new_header += f"  description: '{d}',\n"
                new_header += '}'

                content = content[:header_match.start()] + new_header + content[header_match.end():]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed header in: {filepath}")

for root, _, files in os.walk('src/app/[locale]'):
    for file in files:
        if file.endswith('zh-CN.mdx'):
            path = os.path.join(root, file)
            fix_headers(path)
