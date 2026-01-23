# 设计规范 (Modern Editorial)

## 色彩系统

```css
:root {
  /* 主色调 - 温暖的米白基底 */
  --bg-primary: #faf9f7;
  --bg-secondary: #f5f3f0;
  --bg-tertiary: #efeae5;

  /* 文字颜色 - 高级灰 */
  --text-primary: #1a1a18;
  --text-secondary: #8a8a83;
  --text-muted: #aca9a2;

  /* 强调色 - 精致的琥珀金 */
  --accent: #c4a574;
  --accent-light: #e8dcc8;
  --accent-dark: #a08050;

  /* 功能色 */
  --success: #4a7c59;
  --warning: #d4a574;
  --danger: #c45c5c;

  /* 质感 */
  --border: rgba(0, 0, 0, 0.06);
  --border-subtle: rgba(0, 0, 0, 0.04);
  --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.02);
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.08);
  --shadow-glow: 0 0 40px rgba(196, 165, 116, 0.15);

  /* 圆角 */
  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 28px;

  /* 字体 */
  --font-display: 'Noto Serif SC', Georgia, serif;
  --font-body: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'Outfit', 'SF Mono', monospace;
}
```

## 字体引入

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## 背景纹理

```css
body {
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(196, 165, 116, 0.03), transparent),
    radial-gradient(ellipse 60% 40% at 80% 60%, rgba(196, 165, 116, 0.02), transparent);
}
```

## 渐变边框

```css
.container::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  padding: 1px;
  background: linear-gradient(135deg, var(--accent-light) 0%, transparent 50%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
```

## 毛玻璃导航

```css
.nav-header {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
}
```

## 动画曲线

```css
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

## 卡片悬停效果

```css
.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}
```
