import os

files_to_retranslate = [
    'src/app/[locale]/guides/permission-requests/zh-CN.mdx',
    'src/app/[locale]/guides/the-at-stack/zh-CN.mdx',
    'src/app/[locale]/guides/video-handling/zh-CN.mdx',
    'src/app/[locale]/specs/at-uri-scheme/zh-CN.mdx',
    'src/app/[locale]/specs/repository/zh-CN.mdx'
]

# They were messed up because the header fixer script broke the first line import
for f in files_to_retranslate:
    en_f = f.replace('zh-CN.mdx', 'en.mdx')
    with open(en_f, 'r', encoding='utf-8') as en:
        content = en.read()
    with open(f, 'w', encoding='utf-8') as ch:
        ch.write(content)
