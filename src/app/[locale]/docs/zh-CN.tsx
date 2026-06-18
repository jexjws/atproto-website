import { Usecases } from '@/components/home/Usecases'
import Link from 'next/link'
import { OutlineIconEnum, Icon } from '@/components/icons/outline'

export const header = {
  title: '我们可以构建各种各样的应用',
  description:
    '创建默认具备互操作性的大规模社交应用程序。',
  primaryCTA: {
    label: '简介',
    href: '/guides/understanding-atproto',
  },
  secondaryCTA: {
    label: 'SDKs',
    href: '/sdks',
  },
}

export default function DocsHome() {
  return (
    <div className="flex flex-1 flex-col gap-16 px-8 pb-16 pt-8 md:pt-16 xl:max-w-6xl xl:px-16">
      <div className="grid gap-6 md:grid-cols-2">
        <NavItem
          icon="key"
          title="认证"
          description="登录和权限管理"
          href="/guides/auth"
        />
        <NavItem
          icon="database"
          title="读写操作"
          description="用户数据仓库"
          href="/guides/reads-and-writes"
        />
        <NavItem
          icon="stream"
          title="同步"
          description="流式获取用户活动"
          href="/guides/sync"
        />
        <NavItem
          icon="puzzle-piece"
          title="Lexicon"
          description="记录和 API 的数据架构"
          href="/guides/lexicon"
        />
        <NavItem
          icon="media"
          title="图片和视频"
          description="处理你的 CDN"
          href="/guides/images-and-video"
        />
        <NavItem
          icon="flag"
          title="内容审核"
          description="可组合的信任与安全体系"
          href="/guides/moderation"
        />
      </div>
      <div className="[html_:where(&amp;&gt;*)]:max-w-2xl [html_:where(&amp;&gt;*)]:lg:max-w-3xl prose flex-auto dark:prose-invert">
        <h2 className="scroll-mt-24">
          这是什么？
        </h2>
        <p>
          Atproto 是一个大世界、开放的社交协议。用户将 JSON 记录发布到自己的数据仓库（repositories）。然后，这些记录的变更流（changestreams）会在整个网络中同步，从而驱动各种应用程序运行。
        </p>
        <p>
          我们强烈推荐阅读由社区成员{' '}
          <a
            href="https://bsky.app/profile/danabra.mov"
            target="_blank"
            rel="noopener noreferrer"
          >
            Dan Abramov
          </a>
          {' '}撰写的这几篇精彩文章：
        </p>
        <ul>
          <li>
            <Link href="https://overreacted.io/open-social/">
              <strong>Open Social (开放社交)</strong>
            </Link>{' '}
            - 协议即 API。
          </li>
          <li>
            <Link href="https://overreacted.io/where-its-at/">
              <strong>Where it&apos;s at://</strong>
            </Link>{' '}
            - 从 Handle（句柄）到托管。
          </li>
          <li>
            <Link href="https://overreacted.io/a-social-filesystem/">
              <strong>A Social Filesystem (社交文件系统)</strong>
            </Link>{' '}
            - 数据格式优于应用。
          </li>
        </ul>
        <p>
          或者，你也可以<Link href="/guides/understanding-atproto">在我们的简介文档中</Link>了解更多信息。
        </p>
      </div>
    </div>
  )
}


function NavItem({
  title,
  description,
  href,
  icon,
}: {
  title: string
  description: string
  href: string
  icon: OutlineIconEnum
}) {
  return (
    <Link className="group flex flex-row items-center gap-6" href={href}>
      <div>
        <div className="rounded-sm p-4 ring-1 ring-zinc-900/15 group-hover:ring-zinc-900/30 dark:ring-zinc-100/15 dark:group-hover:ring-zinc-100/25">
          <Icon
            icon={icon}
            className="size-8 fill-none stroke-current"
            strokeWidth="1.0"
          />
        </div>
      </div>
      <div className="flex-1">
        <div className="text-2xl font-medium leading-normal">{title}</div>
        <div className="text-zinc-700 dark:text-zinc-400">{description}</div>
      </div>
    </Link>
  )
}
