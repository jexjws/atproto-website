const homeTranslations: Record<string, Record<string, string>> = {
  ja: {
    // page.tsx hero
    'Building the Social Internet.': 'ソーシャルインターネットを築く。',
    'GET STARTED': 'はじめる',
    'Users': 'ユーザー',
    'Totally normal posts': 'いたって普通の投稿',
    'Open data': 'オープンデータ',

    // ExplainerUnit nav items
    "It's just JSON": 'ただのJSONです',
    'The AT Protocol is a data network. Posts, likes, follows, profiles, etc, are all just JSON.':
      'ATプロトコルはデータネットワークです。投稿、いいね、フォロー、プロフィールなど、すべてJSONです。',
    'Strongly typed': '強力な型付け',
    'Compose and extend records with shared schemas.': '共有スキーマでレコードを構成・拡張できます。',
    'Hyperlinked': 'ハイパーリンク',
    'Everything has a URL. Everyone posts from their own account. Everything is interlinked.':
      'すべてにURLがあります。誰もが自分のアカウントから投稿します。すべてが相互にリンクされています。',
    'With strong links': '強いリンク',
    "Use content-IDs to create strong links to other users' data.":
      'コンテンツIDで他のユーザーのデータへの強いリンクを作成します。',
    'LEARN MORE': '詳しく見る',
    'Next': '次へ',

    // Firehose
    'Public Firehose': 'パブリックファイアホース',
    'Tap into the event stream for all public activity. Build feeds, bots, search engines, and applications using live activity. No API key required.':
      'すべての公開アクティビティのイベントストリームにアクセスできます。ライブアクティビティを使ってフィード、ボット、検索エンジン、アプリを構築しましょう。APIキーは不要です。',
    'Stop stream': '停止',
    'Start stream': '開始',

    // Usecases
    'Create an App': 'アプリを作る',
    'Tap into the shared Atmosphere network to create your next app.':
      '共有のAtmosphereネットワークを活用して次のアプリを作りましょう。',
    'Build an Agent': 'エージェントを作る',
    'Listen to the firehose for mentions and reply to users automatically.':
      'ファイアホースでメンションを受信し、自動返信しましょう。',
    'Write an Algorithm': 'アルゴリズムを書く',
    'Use simple rules or advanced ML to create custom feeds.':
      'シンプルなルールや高度なMLでカスタムフィードを作りましょう。',
    'Login with user-owned identities': 'ユーザー所有のIDでログイン',
    "Usernames are just domains. We're @atproto.com!": 'ユーザー名はドメインです。私たちは@atproto.com！',

    // BentoNav labels
    'Tutorials': 'チュートリアル',
    'Auth': '認証',
    'Read / Write': '読み取りと書き込み',
    'Sync': '同期',
    'Lexicon': 'Lexicon',
    'Media': 'メディア',
    'Moderation': 'モデレーション',
    'SDKs': 'SDK',
    'Cookbook': 'クックブック',
    'Specs': '仕様',
    'FAQ': 'FAQ',
    'Self-hosting': 'セルフホスティング',
    'Showcase': 'ショーケース',
    'Blog': 'ブログ',
  },
  'zh-CN': {
    // page.tsx hero
    'Building the Social Internet.': '构建社交互联网。',
    'GET STARTED': '开始使用',
    'Users': '用户',
    'Totally normal posts': '完全正常的帖子',
    'Open data': '开放数据',

    // ExplainerUnit nav items
    "It's just JSON": '只是 JSON',
    'The AT Protocol is a data network. Posts, likes, follows, profiles, etc, are all just JSON.':
      'AT 协议是一个数据网络。帖子、点赞、关注、个人资料等，全都是 JSON 格式的数据。',
    'Strongly typed': '强类型',
    'Compose and extend records with shared schemas.': '使用共享的模式组合和扩展记录。',
    'Hyperlinked': '超链接连接',
    'Everything has a URL. Everyone posts from their own account. Everything is interlinked.':
      '每个内容都有一个 URL。每个人都在自己的账号下发帖。所有的东西都相互连接在一起。',
    'With strong links': '强链接',
    "Use content-IDs to create strong links to other users' data.":
      '使用内容 ID（Content-IDs）来创建到其他用户数据的强链接。',
    'LEARN MORE': '了解更多',
    'Next': '下一步',

    // Firehose
    'Public Firehose': '公共数据流 (Firehose)',
    'Tap into the event stream for all public activity. Build feeds, bots, search engines, and applications using live activity. No API key required.':
      '接入所有公开活动的事件流。使用实时活动数据构建 feeds、机器人、搜索引擎和应用程序。无需 API 密钥。',
    'Stop stream': '停止流',
    'Start stream': '开启流',

    // Usecases
    'Create an App': '创建一个应用',
    'Tap into the shared Atmosphere network to create your next app.':
      '接入共享的 Atmosphere 网络，来开发你的下一个应用。',
    'Build an Agent': '构建一个代理 (Agent)',
    'Listen to the firehose for mentions and reply to users automatically.':
      '监听信息流中提及你的内容，并自动回复用户。',
    'Write an Algorithm': '编写一个算法',
    'Use simple rules or advanced ML to create custom feeds.':
      '使用简单的规则或者高级的机器学习（ML）技术，来创建属于你的定制内容流。',
    'Login with user-owned identities': '使用用户自己拥有的身份进行登录',
    "Usernames are just domains. We're @atproto.com!": '用户名其实就是域名。我们是 @atproto.com！',

    // BentoNav labels
    'Tutorials': '教程',
    'Auth': '认证',
    'Read / Write': '读 / 写',
    'Sync': '同步',
    'Lexicon': 'Lexicon',
    'Media': '媒体',
    'Moderation': '内容审核',
    'SDKs': 'SDKs',
    'Cookbook': 'Cookbook',
    'Specs': '规范',
    'FAQ': '常见问题',
    'Self-hosting': '私有化部署',
    'Showcase': '项目展示',
    'Blog': '博客',
  },
}

export function homeT(locale: string, key: string): string {
  return homeTranslations[locale]?.[key] ?? key
}
