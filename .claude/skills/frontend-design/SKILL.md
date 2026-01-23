---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

---

## 中文界面补充指南

当用户使用中文交流或明确要求中文界面时，遵循以下原则：

**语言与内容**：
- 页面所有可见文本使用中文（标题、按钮、提示、描述等）
- 仅在技术术语、代码、注释、API 参数中使用英文
- 语言设置：`<html lang="zh-CN">`

**中文字体选择**：
- 优先使用支持中文的优质字体组合
- 标题字体推荐：Noto Serif SC（思源宋体）、Noto Sans SC（思源黑体）、站酷高端黑、阿里巴巴普惠体
- 正文字体：Noto Sans SC、PingFang SC（苹方）、Microsoft YaHei（微软雅黑）
- 英文/数字搭配：选择与中文字体风格协调的西文字体
- 避免直接使用系统默认字体（宋体、楷体等），选择更有设计感的字体

**中文排版**：
- 行高（line-height）建议 1.6-2.0，比西文更宽松
- 中文字符可适当增加字间距（letter-spacing: 2-4px）提升精致感
- 段落首行缩进：使用 `text-indent: 2em`

**中文UI组件**：
- 按钮文本：使用中文动词，如"提交"、"获取"、"开始"、"了解更多"、"立即注册"
- 占位提示：中文提示如"请输入..."、"搜索内容..."
- 空状态：中文提示如"暂无数据"、"内容为空"
- 标签/分类：使用简洁的中文词汇如"热门"、"推荐"、"最新"

**色彩与文化**：
- 可融入中国传统色彩（如：朱红 #ff4d4f、黛蓝 #5c6bc0、墨灰 #4a4a4a、牙白 #faf8f5）
- 红色作为点缀色时注意文化含义
- 整体配色应符合中文用户的审美习惯

**示例结构**：
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>页面标题</title>
</head>
<body>
  <h1>标题</h1>
  <button>提交</button>
</body>
</html>
```
