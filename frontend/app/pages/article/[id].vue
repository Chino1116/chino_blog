<template>
    <main class="app-article-main-chino">
        <div v-if="error" class="app-article-error-chino">
            <h2>加载失败</h2>
            <p>{{ error.message }}</p>
            <button @click="refresh" class="app-retry-btn-chino">重试</button>
        </div>

        <template v-else>
            <aside class="app-article-toc-chino">
                <div class="app-toc-header-chino" @click="toggleToc">
                    <span class="app-toc-title-chino">Content</span>
                    <span class="app-toc-icon-chino">{{ isTocCollapsed ? '▼' : '▲' }}</span>
                </div>
                <div class="app-toc-content-chino" :class="{ 'app-toc-collapsed-chino': isTocCollapsed }">
                    <div v-if="pending || isRendering" class="app-toc-placeholder-chino">
                        <div v-for="i in 5" :key="i" class="app-toc-placeholder-item-chino"></div>
                    </div>
                    <nav v-else-if="toc.length > 0">
                        <ul>
                            <li v-for="item in toc" :key="item.id" :style="{ paddingLeft: `${item.level * 15}px` }">
                                <a :href="`#${item.id}`" @click.prevent="scrollToHeading(item.id)">{{ item.text }}</a>
                            </li>
                        </ul>
                    </nav>
                    <div v-else class="app-toc-empty-chino">
                        <p>暂无目录</p>
                    </div>
                </div>
            </aside>

            <div class="app-article-center-container-chino">
                <article class="app-article-card-chino">
                    <header class="app-article-header-chino">
                        <h1 class="app-article-title-chino">
                            {{ pending ? '加载中...' : (article.title || '未找到数据') }}
                        </h1>
                        <div class="app-article-meta-chino">
                            <span v-if="pending" class="app-article-meta-item-chino">加载中...</span>
                            <template v-else>
                                <span v-if="article.create_time" class="app-article-meta-item-chino">创建于: {{
                                    formatDate(article.create_time) }}</span>
                                <span v-if="article.update_time" class="app-article-meta-item-chino">更新于: {{
                                    formatDate(article.update_time) }}</span>
                            </template>
                        </div>
                    </header>

                    <section class="app-article-content-section-chino">
                        <div v-if="pending || isRendering" class="app-article-loading-placeholder-chino">
                            正在加载文章内容...
                        </div>
                        <div v-else class="app-article-content-chino" v-html="renderedContent"
                            @click="handleContentClick">
                        </div>
                    </section>
                </article>

                <nav v-if="!pending && !error" class="app-article-navigation-chino">
                    <div class="app-article-nav-wrapper-chino">
                        <NuxtLink v-if="article.previous?.id" :to="`/article/${article.previous.id}`"
                            class="app-article-nav-link-chino app-article-nav-prev-chino">
                            <span class="app-article-nav-icon-chino">«</span>
                            <div class="app-article-nav-text-chino">
                                <span class="app-article-nav-label-chino">上一篇</span>
                                <span class="app-article-nav-title-chino">{{ article.previous.title || '未找到数据' }}</span>
                            </div>
                        </NuxtLink>
                        <div v-else class="app-article-nav-placeholder-chino app-article-nav-prev-chino">
                            <span class="app-article-nav-icon-chino" style="opacity: 0.3;">«</span>
                            <div class="app-article-nav-text-chino">
                                <span class="app-article-nav-label-chino">上一篇</span>
                                <span class="app-article-nav-title-chino">无上一篇</span>
                            </div>
                        </div>
                    </div>

                    <div class="app-article-nav-wrapper-chino">
                        <NuxtLink v-if="article.next?.id" :to="`/article/${article.next.id}`"
                            class="app-article-nav-link-chino app-article-nav-next-chino">
                            <div class="app-article-nav-text-chino">
                                <span class="app-article-nav-label-chino">下一篇</span>
                                <span class="app-article-nav-title-chino">{{ article.next.title || '未找到数据' }}</span>
                            </div>
                            <span class="app-article-nav-icon-chino">»</span>
                        </NuxtLink>
                        <div v-else class="app-article-nav-placeholder-chino app-article-nav-next-chino">
                            <div class="app-article-nav-text-chino">
                                <span class="app-article-nav-label-chino">下一篇</span>
                                <span class="app-article-nav-title-chino">无下一篇</span>
                            </div>
                            <span class="app-article-nav-icon-chino" style="opacity: 0.3;">»</span>
                        </div>
                    </div>
                </nav>
            </div>
        </template>

        <Transition name="app-lightbox-fade-chino">
            <div v-if="isLightboxVisible" class="app-lightbox-overlay-chino" @click="closeLightbox">
                <div class="app-lightbox-content-chino" @click.stop>
                    <img :src="lightboxImageSrc" class="app-lightbox-image-chino" alt="Full size view">
                    <button class="app-lightbox-close-btn-chino" @click="closeLightbox">×</button>
                </div>
            </div>
        </Transition>
    </main>
</template>

<script setup>
import { ref, onMounted, nextTick, watch, computed, onUnmounted } from 'vue';
import { useRoute, useHead, useFetch, createError } from '#app';

// --- 引用本地 Assets 资源 ---
import highlightCssUrl from '~/assets/css/atom-one-light.min.css?url';
import katexCssUrl from '~/assets/css/katex.min.css?url';
import markedJsUrl from '~/assets/js/marked.min.js?url';
import highlightJsUrl from '~/assets/js/highlight.min.js?url';
import katexJsUrl from '~/assets/js/katex.min.js?url';

// --- 常量定义 ---
const COPY_ICON_SVG = `<svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M298.666667 170.666667V85.333333h426.666666v85.333334h128.298667c23.381333 0 42.368 18.986667 42.368 42.368v683.264a42.410667 42.410667 0 0 1-42.368 42.368H170.368A42.410667 42.410667 0 0 1 128 896.298667V213.034667C128 189.653333 146.986667 170.666667 170.368 170.666667H298.666667z m0 85.333333H213.333333v597.333333h597.333334V256h-85.333334v85.333333H298.666667V256z m85.333333-85.333333v85.333333h256V170.666667H384z" fill="#4671bb"></path></svg>`;

// --- 工具函数 ---
const decodeUnicodeString = (str) => {
    if (typeof str !== 'string' || !str.includes('\\u')) return str;
    try { return JSON.parse(`"${str}"`); } catch (e) { return str; }
};

const formatDate = (d) => d ? new Date(d * 1000).toLocaleString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
}) : '';

// --- 状态管理 ---
const route = useRoute();
const id = route.params.id;

// --- 核心修改：使用 useFetch 进行服务端数据获取 ---
const { data: article, pending, error, refresh } = await useFetch(`http://localhost:8000/article/${id}`, {
    key: `article-${id}`, // 确保 hydration 匹配
    transform: (data) => {
        // 在数据到达时立即处理解码，这样服务端渲染出的 HTML 就是正确的
        return {
            ...data,
            title: decodeUnicodeString(data.title),
            content: decodeUnicodeString(data.content),
            previous: data.previous ? { ...data.previous, title: decodeUnicodeString(data.previous.title) } : null,
            next: data.next ? { ...data.next, title: decodeUnicodeString(data.next.title) } : null,
        };
    }
});

// SEO Meta 可以在服务端直接生效
useHead({
    title: computed(() => article.value?.title ? `${article.value.title} - CHINO's Blog` : `CHINO's Blog - loading...`),
    meta: [
        { name: 'description', content: computed(() => article.value?.title || `CHINO's Blog - loading...`) }
    ]
});

const toc = ref([]);
const renderedContent = ref('');
const isRendering = ref(true); // 新增：标记是否正在进行 Markdown 渲染
const isTocCollapsed = ref(true);
const isLightboxVisible = ref(false);
const lightboxImageSrc = ref('');

// --- 交互逻辑 ---
const toggleToc = () => isTocCollapsed.value = !isTocCollapsed.value;
const scrollToHeading = (id) => document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });

const handleContentClick = async (event) => {
    const target = event.target;
    if (target.tagName === 'IMG' && target.classList.contains('app-clickable-zoom-chino')) {
        lightboxImageSrc.value = target.src;
        isLightboxVisible.value = true;
        document.body.style.overflow = 'hidden';
        return;
    }
    const copyBtn = target.closest('.app-copy-btn-chino');
    if (copyBtn) {
        const wrapper = copyBtn.closest('.code-block-wrapper');
        if (wrapper) {
            const codeElement = wrapper.querySelector('pre code');
            if (codeElement) {
                try {
                    await navigator.clipboard.writeText(codeElement.innerText);
                    copyBtn.classList.add('copied');
                    setTimeout(() => copyBtn.classList.remove('copied'), 2000);
                } catch (err) {
                    alert('复制失败');
                }
            }
        }
    }
};

const closeLightbox = () => {
    isLightboxVisible.value = false;
    lightboxImageSrc.value = '';
    document.body.style.overflow = '';
};

// --- 资源加载 ---
const loadExternalScripts = () => {
    // 如果在服务端，直接跳过
    if (import.meta.server) return Promise.resolve();

    const resources = [
        { id: 'highlight-css', type: 'link', href: highlightCssUrl },
        { id: 'katex-css', type: 'link', href: katexCssUrl },
        { id: 'marked-js', type: 'script', src: markedJsUrl, globalName: 'marked' },
        { id: 'highlight-js', type: 'script', src: highlightJsUrl, globalName: 'hljs' },
        { id: 'katex-js', type: 'script', src: katexJsUrl, globalName: 'katex' }
    ];

    const promises = resources.map(res => {
        return new Promise((resolve, reject) => {
            if (document.getElementById(res.id)) {
                resolve();
                return;
            }
            let el;
            if (res.type === 'link') {
                el = document.createElement('link');
                el.rel = 'stylesheet';
                el.href = res.href;
            } else {
                el = document.createElement('script');
                el.src = res.src;
            }
            el.id = res.id;
            el.onload = resolve;
            el.onerror = () => reject(new Error(`Failed to load ${res.href || res.src}`));
            document.head.appendChild(el);
        });
    });
    return Promise.all(promises);
};

// --- Markdown 渲染逻辑 ---
const renderMarkdownProcess = () => {
    if (!window.marked || !article.value?.content) return;

    // KaTeX 扩展
    const katexExtension = {
        name: 'katex',
        level: 'inline',
        start(src) { return src.indexOf('$'); },
        tokenizer(src, tokens) {
            const blockRule = /^\$\$([\s\S]+?)\$\$/;
            const blockMatch = blockRule.exec(src);
            if (blockMatch) {
                return { type: 'katex', raw: blockMatch[0], text: blockMatch[1], displayMode: true };
            }
            const inlineRule = /^\$([^$\n]+)\$/;
            const inlineMatch = inlineRule.exec(src);
            if (inlineMatch) {
                return { type: 'katex', raw: inlineMatch[0], text: inlineMatch[1], displayMode: false };
            }
        },
        renderer(token) {
            if (window.katex) {
                try {
                    return window.katex.renderToString(token.text, {
                        displayMode: token.displayMode,
                        throwOnError: false,
                        output: 'html'
                    });
                } catch (error) { return token.raw; }
            }
            return token.raw;
        }
    };

    // 高亮扩展 (==text==)
    const markExtension = {
        name: 'mark',
        level: 'inline',
        start(src) { return src.indexOf('=='); },
        tokenizer(src) {
            const rule = /^==([^=]+)==/;
            const match = rule.exec(src);
            if (match) return { type: 'mark', raw: match[0], text: match[1] };
        },
        renderer(token) { return `<mark>${token.text}</mark>`; }
    };

    window.marked.use({ extensions: [katexExtension, markExtension] });

    const renderer = new window.marked.Renderer();
    const tempToc = [];

    renderer.heading = (text, level) => {
        const id = `heading-${tempToc.length}`;
        tempToc.push({ id, text, level });
        return `<h${level} id="${id}">${text}</h${level}>`;
    };

    renderer.code = (code, language) => {
        const validLang = !!(language && language !== 'plaintext');
        const cleanLang = validLang ? language.replace(/[{}[\]]/g, '') : '';

        let highlightedCode = code;
        if (window.hljs) {
            try {
                if (validLang && window.hljs.getLanguage(cleanLang)) {
                    highlightedCode = window.hljs.highlight(code, { language: cleanLang }).value;
                } else {
                    highlightedCode = window.hljs.highlightAuto(code).value;
                }
            } catch (e) { /* ignore */ }
        }

        const langClass = validLang ? `language-${cleanLang}` : '';
        return `
            <div class="code-block-wrapper">
                <div class="code-header-chino">
                    <span class="code-language-label">${cleanLang || 'Code'}</span>
                    <button class="app-copy-btn-chino" title="Copy code">${COPY_ICON_SVG}</button>
                </div>
                <pre><code class="hljs ${langClass}">${highlightedCode}</code></pre>
            </div>`;
    };

    renderer.image = (href, title, text) => `<img src="${href}" alt="${text}" title="${title || text}" class="app-article-rendered-image-chino app-clickable-zoom-chino">`;

    window.marked.setOptions({ renderer, breaks: true, gfm: true });

    renderedContent.value = window.marked.parse(article.value.content);
    toc.value = tempToc;
    isRendering.value = false; // 渲染完成
};

const applyPostRenderEffects = () => {
    if (import.meta.server) return;
    const container = document.querySelector('.app-article-content-chino');
    if (!container) return;
    container.querySelectorAll('a[href^="http"]').forEach(l => l.setAttribute('target', '_blank'));
};

// --- 生命周期 ---
onMounted(async () => {
    // 客户端挂载后，加载外部脚本库，然后渲染 Markdown
    try {
        await loadExternalScripts();
        if (article.value) {
            renderMarkdownProcess();
            nextTick(() => applyPostRenderEffects());
        }
    } catch (e) {
        console.error("Failed to load resources:", e);
        isRendering.value = false;
    }
});

onUnmounted(() => {
    document.body.style.overflow = '';
});

// 监听数据变化（例如路由切换导致 id 变化）
watch(() => article.value, (newVal) => {
    if (newVal && window.marked) {
        isRendering.value = true;
        // 稍微延迟一下确保 DOM 更新或者脚本已就绪
        nextTick(() => {
            renderMarkdownProcess();
            nextTick(() => applyPostRenderEffects());
        });
    }
});
</script>

<style>
/* === 全局样式 (去除 scoped 以支持 v-html 内部样式) === */

/* 数学公式样式修正 */
.katex-display {
    margin: 1em 0;
    overflow-x: auto;
    overflow-y: hidden;
}

/* 代码块样式 */
.code-block-wrapper {
    position: relative;
    margin: 2em 0;
    border-radius: 8px;
    overflow: hidden;
    /* 背景色设置为淡蓝色调，匹配整体风格 */
    background-color: rgba(70, 113, 187, 0.1);
    border: 1px solid rgba(70, 113, 187, 0.2);
}

.code-header-chino {
    position: absolute;
    top: 0;
    right: 0;
    display: flex;
    align-items: center;
    background: rgba(70, 113, 187, 0.1);
    border-bottom-left-radius: 6px;
    z-index: 2;
}

.code-language-label {
    color: #4671bb;
    padding: 0.3em 0.8em;
    font-size: 0.75em;
    font-weight: 600;
    font-family: system-ui, -apple-system, sans-serif;
}

.app-copy-btn-chino {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 4px 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-left: 1px solid rgba(70, 113, 187, 0.1);
    transition: background-color 0.2s;
}

.app-copy-btn-chino:hover {
    background-color: rgba(70, 113, 187, 0.2);
}

.app-copy-btn-chino.copied {
    background-color: rgba(46, 204, 113, 0.2);
}

/* 重置 pre 样式，让 highlight.js 接管 */
.app-article-content-chino pre {
    margin: 0;
    padding: 2.5rem 1.5rem 1.5rem 1.5rem;
    background: transparent;
    overflow-x: auto;
}

.app-article-content-chino pre code {
    user-select: text;
    background: transparent !important;
    /* 确保不覆盖 hljs 背景 */
    padding: 0;
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    font-size: 0.95em;
    line-height: 1.6;
}

/* 高亮标记 ==text== */
.app-article-content-chino mark {
    background-color: #fef3c7;
    color: #92400e;
    padding: 0 0.2em;
    border-radius: 2px;
}
</style>

<style scoped>
/* === 主体布局 === */
.app-article-main-chino {
    width: 100%;
    height: calc(100vh - 128px);
    padding: 2rem 10%;
    margin: 0 auto;
    box-sizing: border-box;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* 错误状态 */
.app-article-error-chino {
    text-align: center;
    margin-top: 4rem;
    color: #b8b3bc;
}

.app-retry-btn-chino {
    margin-top: 1rem;
    padding: 0.5rem 1.5rem;
    background: #4671bb;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

/* === 目录 === */
.app-article-toc-chino {
    width: 100%;
    max-width: 1100px;
    margin-bottom: 2rem;
    border: 1px solid rgba(70, 113, 187, 0.2);
    border-radius: 12px;
    overflow: hidden;
    background: transparent;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
}

.app-toc-header-chino {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.5rem;
    background: rgba(70, 113, 187, 0.05);
    cursor: pointer;
    transition: background-color 0.3s ease;
    min-height: 3.5rem;
    flex-shrink: 0;
    box-sizing: border-box;
}

.app-toc-header-chino:hover {
    background: rgba(70, 113, 187, 0.1);
}

.app-toc-title-chino {
    font-size: 1.1rem;
    font-weight: 600;
    color: #4671bb;
}

.app-toc-icon-chino {
    font-size: 0.9rem;
    color: #4671bb;
    transition: transform 0.3s ease;
}

.app-toc-content-chino {
    max-height: 80vh;
    overflow-y: auto;
    padding: 1rem 1.5rem;
    background: transparent;
    opacity: 1;
    transition: max-height 0.4s cubic-bezier(0, 1, 0, 1), opacity 0.4s ease, padding 0.4s ease;
}

.app-toc-collapsed-chino {
    max-height: 0 !important;
    padding: 0 !important;
    opacity: 0;
    overflow: hidden;
}

.app-toc-content-chino ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.app-toc-content-chino li a {
    display: block;
    padding: 0.4rem 0.5rem;
    color: #4b424c;
    text-decoration: none;
    border-radius: 8px;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.app-toc-content-chino li a:hover {
    background-color: rgba(70, 113, 187, 0.1);
    color: #4671bb;
}

.app-toc-empty-chino {
    padding: 1rem 1.5rem;
    color: #b8b3bc;
    font-size: 0.9rem;
    text-align: center;
}

/* === 文章容器 === */
.app-article-center-container-chino {
    width: 100%;
    max-width: 1100px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    flex-shrink: 0;
}

.app-article-card-chino {
    background: transparent;
    border-radius: 20px;
    padding: 2rem;
    width: 100%;
    box-sizing: border-box;
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.app-article-header-chino {
    text-align: center;
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid rgba(70, 113, 187, 0.2);
}

.app-article-title-chino {
    font-size: 2.8rem;
    margin: 0 0 1.5rem 0;
    padding: 0;
    font-weight: 700;
    line-height: 1.3;
    min-height: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    word-break: break-word;
    background: linear-gradient(90deg, #4671bb, #b8b3bc);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}

.app-article-meta-chino {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    font-size: 0.9rem;
}

.app-article-meta-item-chino {
    padding: 0.4rem 1rem;
    background-color: rgba(243, 242, 244, 0.8);
    border-radius: 12px;
    color: #4671bb;
    font-weight: 500;
}

/* === 内容排版 === */
.app-article-content-section-chino {
    line-height: 1.9;
    font-size: 1.05rem;
    flex: 1;
    width: 100%;
    font-weight: 400;
}

.app-article-content-chino {
    width: 100%;
    overflow-wrap: break-word;
    word-wrap: break-word;
}

.app-article-content-chino :deep(h1) {
    margin-top: 2em;
    color: #4671bb;
    font-size: 2.2em;
    font-weight: 600;
    line-height: 1.3;
}

.app-article-content-chino :deep(h2) {
    margin-top: 2em;
    color: #4671bb;
    font-size: 1.8em;
    font-weight: 600;
}

.app-article-content-chino :deep(h3) {
    margin-top: 2em;
    color: #4671bb;
    font-size: 1.5em;
    font-weight: 600;
}

.app-article-content-chino :deep(p) {
    margin-bottom: 1.2em;
    color: #202e62;
    font-weight: 400;
}

.app-article-content-chino :deep(strong),
.app-article-content-chino :deep(b) {
    color: #4671bb;
    font-weight: 600;
}

.app-article-content-chino :deep(ul),
.app-article-content-chino :deep(ol) {
    padding-left: 1.5em;
    margin-bottom: 1.2em;
    color: #202e62;
}

.app-article-content-chino :deep(li) {
    margin-bottom: 0.5em;
}

.app-article-content-chino :deep(blockquote) {
    margin: 1.5em 0;
    padding: 0.8em 1.5em;
    border-left: 4px solid #4671bb;
    background-color: rgba(70, 113, 187, 0.1);
    color: #202e62;
    border-radius: 0 8px 8px 0;
}

.app-article-content-chino :deep(img) {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1.5em auto;
    border-radius: 8px;
    transition: transform 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.app-article-content-chino :deep(.app-clickable-zoom-chino) {
    cursor: zoom-in;
}

.app-article-content-chino :deep(.app-clickable-zoom-chino:hover) {
    transform: scale(1.01);
}

.app-article-content-chino :deep(a) {
    color: #4671bb;
    text-decoration: none;
    border-bottom: 1px dotted #4671bb;
    transition: all 0.2s ease;
}

.app-article-content-chino :deep(a:hover) {
    border-bottom-style: solid;
    color: #202e62;
}

.app-article-content-chino :deep(code:not(pre code)) {
    background: rgba(70, 113, 187, 0.1);
    color: #4671bb;
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: "IBM Plex Mono", Consolas, Monaco, monospace;
}

/* === 底部导航 === */
.app-article-navigation-chino {
    display: flex;
    justify-content: space-between;
    gap: 1.5rem;
    margin-top: 3rem;
    width: 100%;
}

.app-article-nav-wrapper-chino {
    flex: 1;
    min-width: 0;
    display: flex;
}

.app-article-nav-link-chino,
.app-article-nav-placeholder-chino {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.5rem;
    background-color: rgba(70, 113, 187, 0.1);
    border: 1px solid rgba(70, 113, 187, 0.2);
    border-radius: 16px;
    text-decoration: none;
    color: #4b424c;
    transition: all 0.3s ease;
    width: 100%;
    box-sizing: border-box;
    justify-content: space-between;
}

.app-article-nav-prev-chino {
    flex-direction: row;
    justify-content: flex-start;
}

.app-article-nav-next-chino {
    flex-direction: row;
    justify-content: flex-end;
    text-align: right;
}

.app-article-nav-next-chino .app-article-nav-text-chino {
    align-items: flex-end;
}

.app-article-nav-link-chino:hover {
    transform: translateY(-3px);
    border-color: #4671bb;
    background-color: rgba(70, 113, 187, 0.15);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.app-article-nav-placeholder-chino {
    opacity: 0.6;
    cursor: not-allowed;
}

.app-article-nav-text-chino {
    display: flex;
    flex-direction: column;
    min-width: 0;
    flex: 1;
}

.app-article-nav-prev-chino .app-article-nav-text-chino {
    text-align: left;
}

.app-article-nav-label-chino {
    font-size: 0.8rem;
    color: #b8b3bc;
    margin-bottom: 0.2rem;
}

.app-article-nav-title-chino {
    font-weight: 600;
    font-size: 1rem;
    color: #4671bb;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.app-article-nav-icon-chino {
    font-size: 2rem;
    font-weight: bold;
    color: #b8b3bc;
    flex-shrink: 0;
}

.app-article-nav-link-chino:hover .app-article-nav-icon-chino {
    color: #4671bb;
}

/* 灯箱 */
.app-lightbox-overlay-chino {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.85);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(5px);
    cursor: zoom-out;
}

.app-lightbox-content-chino {
    position: relative;
    max-width: 90vw;
    max-height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.app-lightbox-image-chino {
    max-width: 100%;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 4px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    cursor: default;
}

.app-lightbox-close-btn-chino {
    position: absolute;
    top: -40px;
    right: -10px;
    background: transparent;
    border: none;
    color: white;
    font-size: 30px;
    cursor: pointer;
    padding: 5px;
    line-height: 1;
    opacity: 0.7;
    transition: opacity 0.3s;
}

.app-lightbox-close-btn-chino:hover {
    opacity: 1;
}

.app-lightbox-fade-chino-enter-active,
.app-lightbox-fade-chino-leave-active {
    transition: opacity 0.3s ease;
}

.app-lightbox-fade-chino-enter-from,
.app-lightbox-fade-chino-leave-to {
    opacity: 0;
}

.app-article-loading-placeholder-chino {
    text-align: center;
    padding: 3rem;
    color: #b8b3bc;
    height: 200px;
}

.app-toc-placeholder-chino {
    animation: pulse 1.5s infinite;
}

.app-toc-placeholder-item-chino {
    height: 0.9rem;
    background: rgba(70, 113, 187, 0.1);
    margin-bottom: 0.5rem;
    border-radius: 4px;
}

@media (max-aspect-ratio: 1/1) {
    .app-article-main-chino {
        padding: 1rem 2%;
    }

    .app-article-navigation-chino {
        flex-direction: column;
    }

    .app-article-nav-next-chino {
        text-align: left;
        justify-content: space-between;
    }

    .app-article-nav-next-chino .app-article-nav-text-chino {
        align-items: flex-start;
    }

    .app-article-card-chino {
        padding: 1.5rem;
    }

    .app-lightbox-close-btn-chino {
        top: -40px;
        right: 0;
    }

    .app-article-title-chino {
        font-size: 2rem;
    }
}
</style>