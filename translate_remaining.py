import os
import re
import time
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text.strip():
        return text
    try:
        # Use a longer timeout or retry
        translator = GoogleTranslator(source='en', target='zh-CN')
        return translator.translate(text)
    except Exception as e:
        print(f"Translation failed for: {text[:30]}... Error: {e}")
        time.sleep(2)
        try:
            translator = GoogleTranslator(source='en', target='zh-CN')
            return translator.translate(text)
        except Exception as e:
            print(f"Retry failed for: {text[:30]}... Error: {e}")
            return text

def translate_mdx_file(filepath):
    print(f"Translating: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the file by Markdown paragraphs/blocks to keep JSX/Code intact

    # Simple state machine for parsing MDX
    lines = content.split('\n')
    new_lines = []

    in_code_block = False
    in_jsx = False
    in_frontmatter = False

    current_block = []

    def process_block(block):
        text = '\n'.join(block)
        if not text.strip():
            return text

        # Don't translate lines that look like JSX imports or exports
        if re.match(r'^(import|export)\b', text):
            # We will handle header translation separately
            return text

        # Protect markdown headers, but translate the text
        header_match = re.match(r'^(#+)\s+(.*)', text)
        if header_match:
            hashes, title = header_match.groups()
            translated_title = translate_text(title)
            return f"{hashes} {translated_title}"

        # Protect lists
        list_match = re.match(r'^(\s*[-*+]|\s*\d+\.)\s+(.*)', text)
        if list_match:
            marker, item = list_match.groups()
            # translate the item, but watch out for inline code
            # this is simple block translation, let's just translate the item
            translated_item = translate_text(item)
            return f"{marker} {translated_item}"

        # Protect links
        if re.match(r'^\[.*\]\(.*\)$', text.strip()):
            return text

        # Don't translate HTML/JSX tags themselves
        if text.strip().startswith('<') and text.strip().endswith('>'):
            return text

        # Don't translate things that look like URLs
        if text.strip().startswith('http://') or text.strip().startswith('https://'):
            return text

        # Generic paragraph translation
        # Splitting by chunks if needed, but GoogleTranslator handles up to 5000 chars
        translated_text = translate_text(text)
        return translated_text

    for line in lines:
        if line.startswith('```'):
            if current_block:
                new_lines.append(process_block(current_block))
                current_block = []
            new_lines.append(line)
            in_code_block = not in_code_block
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # Handle simple JSX components
        if re.match(r'^<\w+', line.strip()) and not re.search(r'>.*<', line):
            if current_block:
                new_lines.append(process_block(current_block))
                current_block = []
            new_lines.append(line)
            in_jsx = True
            continue

        if in_jsx and re.match(r'^</\w+>$', line.strip()):
            new_lines.append(line)
            in_jsx = False
            continue

        if in_jsx:
            new_lines.append(line)
            continue

        if not line.strip():
            if current_block:
                new_lines.append(process_block(current_block))
                current_block = []
            new_lines.append('')
            continue

        current_block.append(line)

    if current_block:
        new_lines.append(process_block(current_block))

    # Re-apply the formatting rule from previous code reviews
    # "**xxx:** " -> "**xxx：** "
    final_content = '\n'.join(new_lines)
    final_content = re.sub(r'\*\*(.*?)\*\*:\s+', r'**\1：** ', final_content)
    # add space before Chinese char after bold if needed
    final_content = re.sub(r'(\*\*(.*?)\*\*(：)?)([\u4e00-\u9fa5])', r'\1 \4', final_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)


files_to_translate = [
    'src/app/[locale]/guides/reading-data/zh-CN.mdx',
    'src/app/[locale]/guides/writing-data/zh-CN.mdx',
    'src/app/[locale]/guides/video-handling/zh-CN.mdx',
    'src/app/[locale]/guides/custom-feed-tutorial/zh-CN.mdx',
    'src/app/[locale]/guides/images-and-video/zh-CN.mdx',
    'src/app/[locale]/guides/oauth-tutorial/zh-CN.mdx',
    'src/app/[locale]/guides/installing-lexicons/zh-CN.mdx',
    'src/app/[locale]/guides/feeds/zh-CN.mdx',
    'src/app/[locale]/guides/sdk-auth/zh-CN.mdx',
    'src/app/[locale]/guides/reads-and-writes/zh-CN.mdx',
    'src/app/[locale]/guides/data-validation/zh-CN.mdx',
    'src/app/[locale]/guides/go-oauth-cli-tutorial/zh-CN.mdx',
    'src/app/[locale]/guides/auth/zh-CN.mdx',
    'src/app/[locale]/specs/repository/zh-CN.mdx',
    'src/app/[locale]/specs/at-uri-scheme/zh-CN.mdx',
    'src/app/[locale]/specs/xrpc/zh-CN.mdx',
    'src/app/[locale]/specs/permission/zh-CN.mdx'
]

for f in files_to_translate:
    translate_mdx_file(f)
    print(f"Finished {f}")
