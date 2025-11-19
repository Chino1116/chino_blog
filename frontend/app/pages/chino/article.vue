<template>
    <main class="app-chino-admin-main-chino">
        <header class="admin-header">
            <h2 class="page-title">文章管理</h2>
            <NuxtLink to="/chino/category" class="app-chino-admin-btn-chino outline">
                <span class="icon"></span> 分类管理
            </NuxtLink>
        </header>

        <div class="app-chino-admin-card-chino control-panel">
            <div class="form-section">
                <h3 class="section-title">发布新文章</h3>
                <div class="input-grid">
                    <input v-model="newArticle.title" placeholder="文章标题" class="app-chino-admin-input-chino" />
                    <select v-model="newArticle.category_id" class="app-chino-admin-input-chino">
                        <option value="" disabled>选择分类</option>
                        <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                    </select>
                    <input v-model="newArticle.cover" placeholder="封面图片链接" class="app-chino-admin-input-chino" />
                    <input v-model="newArticle.description" placeholder="简短描述"
                        class="app-chino-admin-input-chino full-width" />
                </div>
                <div class="action-row">
                    <button @click="addArticle" class="app-chino-admin-btn-chino primary">
                        <span class="plus-icon">+</span> 新增文章
                    </button>
                </div>
            </div>

            <hr class="divider" />

            <div class="filter-section">
                <div class="search-box">
                    <input v-model="search" placeholder="搜索标题或描述..." class="app-chino-admin-input-chino" />
                </div>
                <div class="filter-controls">
                    <select v-model="filterCategory" class="app-chino-admin-input-chino">
                        <option value="">全部分类</option>
                        <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                    </select>
                    <select v-model="sortOrder" class="app-chino-admin-input-chino">
                        <option value="desc">时间倒序</option>
                        <option value="asc">时间正序</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="app-chino-admin-list-container">
            <table class="app-chino-admin-table desktop-view">
                <thead>
                    <tr>
                        <th width="50">ID</th>
                        <th width="20%">标题</th>
                        <th>描述</th>
                        <th width="100">分类</th>
                        <th width="150">时间</th>
                        <th width="160">操作</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="art in filteredArticles" :key="art.id">
                        <td class="id-col">#{{ art.id }}</td>
                        <td><input v-model="art.title" class="app-chino-admin-input-chino compact" /></td>
                        <td><input v-model="art.description" class="app-chino-admin-input-chino compact" /></td>
                        <td>
                            <select v-model="art.category_id" class="app-chino-admin-input-chino compact">
                                <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                            </select>
                        </td>
                        <td class="time-col">
                            <div class="time-tag">C: {{ formatDate(art.create_time) }}</div>
                            <div class="time-tag update">U: {{ formatDate(art.update_time) }}</div>
                        </td>
                        <td class="action-col">
                            <button @click="openMarkdownEditor(art)" class="app-chino-admin-btn-chino icon-btn"
                                title="编辑内容">编</button>
                            <button @click="updateArticle(art)" class="app-chino-admin-btn-chino icon-btn save"
                                title="保存元数据">存</button>
                            <button @click="deleteArticle(art.id)" class="app-chino-admin-btn-chino icon-btn delete"
                                title="删除">删</button>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div class="mobile-view-list">
                <div v-for="art in filteredArticles" :key="art.id"
                    class="app-chino-admin-card-chino article-card-mobile">
                    <div class="mobile-card-header">
                        <span class="mobile-id">#{{ art.id }}</span>
                        <span class="mobile-time">{{ formatDate(art.create_time) }}</span>
                    </div>
                    <div class="mobile-card-body">
                        <input v-model="art.title" class="app-chino-admin-input-chino" placeholder="标题" />
                        <select v-model="art.category_id" class="app-chino-admin-input-chino">
                            <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                        </select>
                        <textarea v-model="art.description" class="app-chino-admin-input-chino" rows="2"
                            placeholder="描述"></textarea>
                    </div>
                    <div class="mobile-card-actions">
                        <button @click="openMarkdownEditor(art)" class="app-chino-admin-btn-chino small">编辑正文</button>
                        <div class="right-actions">
                            <button @click="updateArticle(art)" class="app-chino-admin-btn-chino small save">保存</button>
                            <button @click="deleteArticle(art.id)"
                                class="app-chino-admin-btn-chino small delete">删除</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="showEditor" class="markdown-editor-overlay">
            <div class="markdown-editor-modal">
                <div class="editor-header">
                    <div class="editor-title">
                        <h3>编辑内容</h3>
                        <span class="editor-subtitle">ID: {{ editingArticle.id }} - {{ editingArticle.title }}</span>
                    </div>
                    <div class="editor-controls">
                        <button @click="saveMarkdown" class="app-chino-admin-btn-chino primary">保存并关闭</button>
                        <button @click="closeMarkdownEditor" class="app-chino-admin-btn-chino close">✕</button>
                    </div>
                </div>

                <div class="editor-split-view">
                    <div class="editor-pane input-pane">
                        <textarea v-model="editingArticle.markdown" placeholder="# 开始写作..."
                            class="markdown-textarea"></textarea>
                    </div>

                    <div class="editor-pane preview-pane">
                        <div class="preview-label">PREVIEW</div>
                        <div class="app-article-content-chino" v-html="renderedMarkdown"></div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>
/* 脚本内容保持不变，请保留原有的 script setup 内容 */
import { ref, onMounted, computed, watch, nextTick } from 'vue';
import markedJsUrl from '~/assets/js/marked.min.js?url';
import highlightJsUrl from '~/assets/js/highlight.min.js?url';
import katexJsUrl from '~/assets/js/katex.min.js?url';
import highlightCssUrl from '~/assets/css/atom-one-light.min.css?url';
import katexCssUrl from '~/assets/css/katex.min.css?url';

const API_BASE = 'http://localhost:8000';
const COPY_ICON_SVG = `<svg viewBox="0 0 1024 1024" width="16" height="16"><path d="M298.666667 170.666667V85.333333h426.666666v85.333334h128.298667c23.381333 0 42.368 18.986667 42.368 42.368v683.264a42.410667 42.410667 0 0 1-42.368 42.368H170.368A42.410667 42.410667 0 0 1 128 896.298667V213.034667C128 189.653333 146.986667 170.666667 170.368 170.666667H298.666667z m0 85.333333H213.333333v597.333333h597.333334V256h-85.333334v85.333333H298.666667V256z m85.333333-85.333333v85.333333h256V170.666667H384z" fill="currentColor"></path></svg>`;

const articles = ref([]);
const categories = ref([]);
const newArticle = ref({ title: '', description: '', cover: '', category_id: '', markdown: '' });
const search = ref('');
const filterCategory = ref('');
const sortOrder = ref('desc');
const showEditor = ref(false);
const editingArticle = ref({});
const renderedMarkdown = ref('');

function formatDate(dateStr) {
    if (!dateStr) return '-';
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return dateStr;
    const pad = n => n < 10 ? '0' + n : n;
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

function getAdminKey() {
    const match = document.cookie.match(/(?:^|; )chino_admin_key=([^;]*)/);
    return match ? decodeURIComponent(match[1]) : '';
}

function loadPreviewResources() {
    if (typeof window === 'undefined') return Promise.resolve();
    const resources = [
        { id: 'hl-css', type: 'link', href: highlightCssUrl },
        { id: 'kt-css', type: 'link', href: katexCssUrl },
        { id: 'mk-js', type: 'script', src: markedJsUrl, globalName: 'marked' },
        { id: 'hl-js', type: 'script', src: highlightJsUrl, globalName: 'hljs' },
        { id: 'kt-js', type: 'script', src: katexJsUrl, globalName: 'katex' }
    ];
    return Promise.all(resources.map(res => new Promise((resolve, reject) => {
        if (document.getElementById(res.id)) { resolve(); return; }
        let el = document.createElement(res.type === 'link' ? 'link' : 'script');
        if (res.type === 'link') { el.rel = 'stylesheet'; el.href = res.href; }
        else { el.src = res.src; }
        el.id = res.id;
        el.onload = resolve;
        el.onerror = () => resolve();
        document.head.appendChild(el);
    })));
}

function configureMarked() {
    if (!window.marked) return;
    const katexExt = {
        name: 'katex', level: 'inline',
        start(src) { return src.indexOf('$'); },
        tokenizer(src) {
            const block = /^\$\$([\s\S]+?)\$\$/.exec(src);
            if (block) return { type: 'katex', raw: block[0], text: block[1], displayMode: true };
            const inline = /^\$([^$\n]+)\$/.exec(src);
            if (inline) return { type: 'katex', raw: inline[0], text: inline[1], displayMode: false };
        },
        renderer(token) {
            if (window.katex) {
                try { return window.katex.renderToString(token.text, { displayMode: token.displayMode, throwOnError: false, output: 'html' }); }
                catch { return token.raw; }
            }
            return token.raw;
        }
    };

    const markExt = {
        name: 'mark', level: 'inline',
        start(src) { return src.indexOf('=='); },
        tokenizer(src) {
            const match = /^==([^=]+)==/.exec(src);
            if (match) return { type: 'mark', raw: match[0], text: match[1] };
        },
        renderer(token) { return `<mark>${token.text}</mark>`; }
    };

    window.marked.use({ extensions: [katexExt, markExt] });

    const renderer = new window.marked.Renderer();
    renderer.heading = (text, level) => `<h${level} id="h-${text.replace(/\s+/g, '-')}">${text}</h${level}>`;

    renderer.code = (code, language) => {
        const lang = (language || '').replace(/[{}[\]]/g, '');
        let highlighted = code;
        if (window.hljs) {
            try { highlighted = lang && window.hljs.getLanguage(lang) ? window.hljs.highlight(code, { language: lang }).value : window.hljs.highlightAuto(code).value; }
            catch { }
        }
        return `<div class="code-block-wrapper"><div class="code-header-chino"><span class="code-language-label">${lang || 'Code'}</span><button class="app-copy-btn-chino">${COPY_ICON_SVG}</button></div><pre><code class="hljs ${lang}">${highlighted}</code></pre></div>`;
    };

    renderer.image = (href, title, text) => `<img src="${href}" alt="${text}" title="${title || ''}" class="app-article-rendered-image-chino app-clickable-zoom-chino">`;

    window.marked.setOptions({ renderer, breaks: true, gfm: true });
}

watch([showEditor, () => editingArticle.value.markdown], async ([show, md]) => {
    if (!show) return;
    await loadPreviewResources();
    configureMarked();
    if (window.marked) {
        renderedMarkdown.value = window.marked.parse(md || '');
        nextTick(() => {
            const container = document.querySelector('.preview-pane .app-article-content-chino');
            if (container) container.querySelectorAll('a[href^="http"]').forEach(l => l.setAttribute('target', '_blank'));
        });
    }
});

async function fetchCategories() {
    try {
        const res = await fetch(API_BASE + '/category');
        categories.value = await res.json();
    } catch { categories.value = []; }
}

async function fetchArticles() {
    try {
        const res = await fetch(API_BASE + '/articles');
        const data = await res.json();
        if (Array.isArray(data)) {
            await Promise.all(data.map(async (art) => {
                art.category_id = art.category_id ? Number(art.category_id) : '';
                try {
                    const mdRes = await fetch(`${API_BASE}/article/${art.id}`);
                    const mdData = await mdRes.json();
                    art.markdown = mdData.content || '';
                } catch { art.markdown = ''; }
            }));
            articles.value = data;
        }
    } catch { articles.value = []; }
}

function openMarkdownEditor(art) { editingArticle.value = art; showEditor.value = true; }
function closeMarkdownEditor() { showEditor.value = false; }
function saveMarkdown() { updateArticle(editingArticle.value); showEditor.value = false; }

async function handleApi(body) {
    const key = getAdminKey();
    const res = await fetch(API_BASE + '/api/admin/article', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...body, key })
    });
    return await res.json();
}

async function addArticle() {
    if (!newArticle.value.title) return alert('标题不能为空');
    const res = await handleApi({ ...newArticle.value, action: 'add' });
    if (res.success) {
        newArticle.value = { title: '', description: '', cover: '', category_id: '', markdown: '' };
        fetchArticles();
    } else alert(res.error);
}

async function updateArticle(art) {
    const res = await handleApi({ ...art, action: 'update', id: art.id, content: art.markdown });
    if (res.success) fetchArticles();
    else alert(res.error);
}

async function deleteArticle(id) {
    if (!confirm('确定要删除这篇文章吗？')) return;
    const res = await handleApi({ action: 'delete', id });
    if (res.success) fetchArticles();
    else alert(res.error);
}

const filteredArticles = computed(() => {
    let list = articles.value;
    if (search.value) {
        const k = search.value.toLowerCase();
        list = list.filter(a => a.title.toLowerCase().includes(k) || (a.description && a.description.toLowerCase().includes(k)));
    }
    if (filterCategory.value) {
        list = list.filter(a => Number(a.category_id) === Number(filterCategory.value));
    }
    list.sort((a, b) => {
        const tA = new Date(a.create_time).getTime();
        const tB = new Date(b.create_time).getTime();
        return sortOrder.value === 'asc' ? tA - tB : tB - tA;
    });
    return list;
});

onMounted(() => {
    fetchCategories();
    fetchArticles();
});
</script>

<style>
/* 全局样式保持不变 */
.katex-display {
    margin: 1em 0;
    overflow-x: auto;
}

.code-block-wrapper {
    position: relative;
    margin: 2em 0;
    border-radius: 8px;
    overflow: hidden;
    background-color: rgba(70, 113, 187, 0.08);
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
}

.app-copy-btn-chino {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 4px 8px;
    color: #4671bb;
    border-left: 1px solid rgba(70, 113, 187, 0.1);
}

.app-article-content-chino pre {
    margin: 0;
    padding: 2.5rem 1.5rem 1.5rem;
    background: transparent;
    overflow-x: auto;
}

.app-article-content-chino pre code {
    font-family: Consolas, monospace;
    font-size: 0.95em;
    background: transparent;
}

.app-article-content-chino mark {
    background-color: #fef3c7;
    color: #92400e;
    padding: 0 0.2em;
    border-radius: 2px;
}

.app-article-content-chino {
    width: 100%;
    line-height: 1.8;
    color: #202e62;
}

.app-article-content-chino h1,
.app-article-content-chino h2,
.app-article-content-chino h3 {
    color: #4671bb;
    font-weight: 600;
    margin-top: 1.5em;
}

.app-article-content-chino h1 {
    font-size: 2em;
    border-bottom: 1px solid #eee;
}

.app-article-content-chino p {
    margin-bottom: 1.2em;
}

.app-article-content-chino blockquote {
    margin: 1.5em 0;
    padding: 0.8em 1.5em;
    border-left: 4px solid #4671bb;
    background-color: rgba(70, 113, 187, 0.1);
    color: #555;
    border-radius: 0 8px 8px 0;
}

.app-article-content-chino img {
    max-width: 100%;
    border-radius: 8px;
    margin: 1.5em auto;
    display: block;
}

.app-article-content-chino a {
    color: #4671bb;
    text-decoration: none;
    border-bottom: 1px dotted #4671bb;
}

.app-article-content-chino code:not(pre code) {
    background: rgba(70, 113, 187, 0.1);
    color: #4671bb;
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: monospace;
}
</style>

<style scoped>
/* 通用变量 */
:root {
    --primary: #4671bb;
    --bg-page: #f4f7fa;
    --bg-card: #ffffff;
    --text-main: #202e62;
    --text-sub: #b8b3bc;
    --danger: #e45649;
}

/* === 核心优化 === */
.app-chino-admin-main-chino {
    /* 高度设定：总高度 - 顶部导航(假设) - 额外空间 */
    height: calc(100vh - 128px);
    /* 背景透明 */
    background-color: transparent;
    /* 内部滚动 */
    overflow-y: auto;
    overflow-x: hidden;
    /* 宽度自适应但受限 */
    width: 100%;
    box-sizing: border-box;
    padding: 24px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* 滚动条美化 */
.app-chino-admin-main-chino::-webkit-scrollbar {
    width: 6px;
}

.app-chino-admin-main-chino::-webkit-scrollbar-thumb {
    background: rgba(70, 113, 187, 0.2);
    border-radius: 3px;
}

.app-chino-admin-main-chino::-webkit-scrollbar-track {
    background: transparent;
}

/* Header */
.admin-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(70, 113, 187, 0.1);
    /* 确保 Header 在透明背景下文字清晰，或者可以考虑加白色背景条 */
}

.page-title {
    margin: 0;
    color: #4671bb;
    font-size: 1.8rem;
    font-weight: 700;
}

/* 卡片容器 - 保持白色背景 */
.app-chino-admin-card-chino {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    padding: 24px;
    margin-bottom: 24px;
}

/* 输入框 */
.app-chino-admin-input-chino {
    padding: 10px 14px;
    border: 1px solid rgba(70, 113, 187, 0.2);
    border-radius: 8px;
    font-size: 14px;
    color: #4b424c;
    transition: all 0.2s;
    background: #fafafa;
    width: 100%;
    box-sizing: border-box;
}

.app-chino-admin-input-chino:focus {
    border-color: #4671bb;
    background: #fff;
    outline: none;
    box-shadow: 0 0 0 3px rgba(70, 113, 187, 0.1);
}

.app-chino-admin-input-chino.compact {
    padding: 6px 10px;
    font-size: 13px;
    border-color: transparent;
    background: transparent;
}

.app-chino-admin-input-chino.compact:focus {
    border-color: #4671bb;
    background: #fff;
}

/* 按钮 */
.app-chino-admin-btn-chino {
    padding: 8px 16px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.app-chino-admin-btn-chino.primary {
    background: #4671bb;
    color: white;
    box-shadow: 0 4px 10px rgba(70, 113, 187, 0.3);
}

.app-chino-admin-btn-chino.primary:hover {
    background: #3a5da0;
    transform: translateY(-1px);
}

.app-chino-admin-btn-chino.outline {
    background: transparent;
    border: 1px solid #4671bb;
    color: #4671bb;
}

.app-chino-admin-btn-chino.outline:hover {
    background: rgba(70, 113, 187, 0.1);
}

.app-chino-admin-btn-chino.icon-btn {
    padding: 6px;
    background: rgba(70, 113, 187, 0.1);
    color: #4671bb;
    border-radius: 6px;
    margin: 0 4px;
}

.app-chino-admin-btn-chino.icon-btn:hover {
    background: #4671bb;
    color: white;
}

.app-chino-admin-btn-chino.icon-btn.delete:hover {
    background: #e45649;
}

.app-chino-admin-btn-chino.icon-btn.save:hover {
    background: #2ecc71;
}

/* 表单区域 */
.section-title {
    margin: 0 0 16px 0;
    font-size: 1rem;
    color: #202e62;
}

.input-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}

.full-width {
    grid-column: 1 / -1;
}

.action-row {
    text-align: right;
}

.divider {
    border: 0;
    height: 1px;
    background: rgba(70, 113, 187, 0.1);
    margin: 20px 0;
}

/* 筛选区 */
.filter-section {
    display: flex;
    gap: 16px;
    justify-content: space-between;
    flex-wrap: wrap;
}

.search-box {
    flex: 1;
    min-width: 200px;
}

.filter-controls {
    display: flex;
    gap: 12px;
}

/* 表格 */
.app-chino-admin-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.app-chino-admin-table th {
    background: rgba(70, 113, 187, 0.05);
    color: #4671bb;
    font-weight: 600;
    padding: 16px;
    text-align: left;
    font-size: 14px;
}

.app-chino-admin-table td {
    padding: 12px 16px;
    border-bottom: 1px solid #f0f2f5;
    vertical-align: middle;
}

.app-chino-admin-table tr:last-child td {
    border-bottom: none;
}

.id-col {
    color: #b8b3bc;
    font-size: 12px;
    font-family: monospace;
}

.time-tag {
    font-size: 12px;
    color: #888;
    background: #f5f5f5;
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 4px;
}

.time-tag.update {
    color: #4671bb;
    background: rgba(70, 113, 187, 0.1);
}

/* 移动端视图 (默认隐藏) */
.mobile-view-list {
    display: none;
}

.desktop-view {
    display: table;
}

/* 编辑器模态框 - Fixed 布局，不跟随父容器滚动 */
.markdown-editor-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(32, 46, 98, 0.7);
    backdrop-filter: blur(4px);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
}

.markdown-editor-modal {
    background: #fff;
    width: 95%;
    height: 92%;
    max-width: 1400px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

.editor-header {
    padding: 16px 24px;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fff;
}

.editor-title h3 {
    margin: 0;
    color: #4671bb;
    font-size: 1.2rem;
}

.editor-subtitle {
    font-size: 0.85rem;
    color: #999;
    margin-left: 8px;
}

.editor-controls {
    display: flex;
    gap: 12px;
    align-items: center;
}

.app-chino-admin-btn-chino.close {
    background: #f5f5f5;
    color: #666;
    width: 32px;
    height: 32px;
    padding: 0;
    justify-content: center;
    border-radius: 50%;
}

.editor-split-view {
    flex: 1;
    display: flex;
    overflow: hidden;
}

.editor-pane {
    flex: 1;
    height: 100%;
    overflow-y: auto;
    padding: 24px;
    box-sizing: border-box;
}

.input-pane {
    background: #f9fafc;
    border-right: 1px solid #eee;
    padding: 0;
}

.markdown-textarea {
    width: 100%;
    height: 100%;
    border: none;
    background: transparent;
    padding: 24px;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 15px;
    line-height: 1.6;
    color: #333;
    resize: none;
    outline: none;
}

.preview-pane {
    background: #fff;
    position: relative;
}

.preview-label {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 10px;
    font-weight: bold;
    color: #ddd;
    letter-spacing: 1px;
    pointer-events: none;
}

/* === 响应式优化 === */
@media (max-width: 1024px) {
    .input-grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 768px) {
    .app-chino-admin-main-chino {
        padding: 12px;
    }

    .admin-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }

    /* 切换视图 */
    .desktop-view {
        display: none;
    }

    .mobile-view-list {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    .app-chino-admin-card-chino {
        padding: 16px;
    }

    .input-grid {
        grid-template-columns: 1fr;
    }

    .filter-section {
        flex-direction: column;
    }

    /* 移动端卡片样式 */
    .article-card-mobile {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .mobile-card-header {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #aaa;
        border-bottom: 1px dashed #eee;
        padding-bottom: 8px;
    }

    .mobile-card-body {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .mobile-card-actions {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 8px;
        padding-top: 8px;
        border-top: 1px solid #eee;
    }

    .right-actions {
        display: flex;
        gap: 8px;
    }

    .app-chino-admin-btn-chino.small {
        padding: 6px 10px;
        font-size: 12px;
    }

    .app-chino-admin-btn-chino.small.delete {
        background: #ffecec;
        color: #e45649;
    }

    /* 编辑器移动端适配 */
    .editor-split-view {
        flex-direction: column;
    }

    .editor-pane {
        height: 50%;
    }

    .input-pane {
        border-right: none;
        border-bottom: 1px solid #ddd;
    }

    .editor-title {
        max-width: 60%;
    }

    .editor-subtitle {
        display: none;
    }
}
</style>