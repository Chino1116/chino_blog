<template>
    <main class="app-chino-admin-main-chino">
        <header class="admin-header">
            <h2 class="page-title">分类管理</h2>
            <NuxtLink to="/chino/article" class="app-chino-admin-btn-chino outline">
                <span class="icon"></span> 文章管理
            </NuxtLink>
        </header>

        <div class="app-chino-admin-card-chino control-panel">
            <div class="form-section">
                <h3 class="section-title">新增分类</h3>
                <div class="input-grid-category">
                    <input v-model="newCategory.name" placeholder="分类名称 (e.g. 技术)"
                        class="app-chino-admin-input-chino" />
                    <input v-model="newCategory.route" placeholder="路由别名 (e.g. tech)"
                        class="app-chino-admin-input-chino" />
                    <button @click="addCategory" class="app-chino-admin-btn-chino primary">
                        <span class="plus-icon">+</span> 添加
                    </button>
                </div>
            </div>
        </div>

        <div class="app-chino-admin-list-container">
            <table class="app-chino-admin-table desktop-view">
                <thead>
                    <tr>
                        <th width="80">ID</th>
                        <th>分类名称</th>
                        <th>路由别名</th>
                        <th width="140">操作</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="cat in categories" :key="cat.id">
                        <td class="id-col">#{{ cat.id }}</td>
                        <td>
                            <input v-model="cat.name" class="app-chino-admin-input-chino compact" placeholder="分类名称" />
                        </td>
                        <td>
                            <input v-model="cat.route" class="app-chino-admin-input-chino compact" placeholder="路由别名" />
                        </td>
                        <td class="action-col">
                            <button @click="updateCategory(cat)" class="app-chino-admin-btn-chino icon-btn save"
                                title="保存修改">
                                存
                            </button>
                            <button @click="deleteCategory(cat.id)" class="app-chino-admin-btn-chino icon-btn delete"
                                title="删除分类">
                                删
                            </button>
                        </td>
                    </tr>
                    <tr v-if="categories.length === 0">
                        <td colspan="4" style="text-align:center; color: #999; padding: 32px;">暂无分类数据</td>
                    </tr>
                </tbody>
            </table>

            <div class="mobile-view-list">
                <div v-for="cat in categories" :key="cat.id" class="app-chino-admin-card-chino category-card-mobile">
                    <div class="mobile-card-header">
                        <span class="mobile-id">ID: #{{ cat.id }}</span>
                    </div>
                    <div class="mobile-card-body">
                        <div class="input-group">
                            <label>名称</label>
                            <input v-model="cat.name" class="app-chino-admin-input-chino" />
                        </div>
                        <div class="input-group">
                            <label>路由</label>
                            <input v-model="cat.route" class="app-chino-admin-input-chino" />
                        </div>
                    </div>
                    <div class="mobile-card-actions">
                        <button @click="updateCategory(cat)" class="app-chino-admin-btn-chino small save">保存修改</button>
                        <button @click="deleteCategory(cat.id)"
                            class="app-chino-admin-btn-chino small delete">删除</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE = 'http://localhost:8000';
const categories = ref([]);
const newCategory = ref({ name: '', route: '' });

async function fetchCategories() {
    try {
        const res = await fetch(API_BASE + '/category');
        const data = await res.json();
        if (Array.isArray(data)) {
            categories.value = data.map(cat => ({ ...cat }));
        } else {
            categories.value = [];
        }
    } catch (e) {
        categories.value = [];
    }
}

function getAdminKey() {
    const match = document.cookie.match(/(?:^|; )chino_admin_key=([^;]*)/);
    return match ? decodeURIComponent(match[1]) : '';
}

async function addCategory() {
    if (!newCategory.value.name) return alert('分类名称不能为空');
    const key = getAdminKey();
    const res = await fetch(API_BASE + '/api/admin/category', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...newCategory.value, action: 'add', key })
    });
    const result = await res.json();
    if (result.success) {
        newCategory.value = { name: '', route: '' };
        fetchCategories();
    } else {
        alert(result.error || '操作失败');
    }
}

async function updateCategory(cat) {
    const key = getAdminKey();
    const res = await fetch(API_BASE + '/api/admin/category', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: cat.name, route: cat.route, id: cat.id, action: 'update', key })
    });
    const result = await res.json();
    if (result.success) {
        // Optional: toast success
    } else {
        alert(result.error || '操作失败');
    }
    fetchCategories();
}

async function deleteCategory(id) {
    if (!confirm('确定要删除该分类吗？')) return;
    const key = getAdminKey();
    const res = await fetch(API_BASE + '/api/admin/category', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, action: 'delete', key })
    });
    const result = await res.json();
    if (result.success) {
        fetchCategories();
    } else {
        alert(result.error || '操作失败');
    }
}

onMounted(fetchCategories);
</script>

<style scoped>
/* 复用 Article.vue 的核心变量与样式 */
:root {
    --primary: #4671bb;
    --bg-page: #f4f7fa;
    --bg-card: #ffffff;
    --text-main: #202e62;
    --danger: #e45649;
}

/* === 核心优化 === */
.app-chino-admin-main-chino {
    /* 高度设定 */
    height: calc(100vh - 128px);
    /* 背景透明 */
    background-color: transparent;
    /* 内部滚动 */
    overflow-y: auto;
    overflow-x: hidden;
    /* 宽度自适应 */
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
}

.page-title {
    margin: 0;
    color: #4671bb;
    font-size: 1.8rem;
    font-weight: 700;
}

/* Card & Form */
.app-chino-admin-card-chino {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    padding: 24px;
    margin-bottom: 24px;
}

.section-title {
    margin: 0 0 16px 0;
    font-size: 1rem;
    color: #202e62;
}

.input-grid-category {
    display: grid;
    grid-template-columns: 1fr 1fr auto;
    gap: 12px;
    align-items: center;
}

/* Inputs */
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

/* Buttons */
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
    justify-content: center;
    gap: 6px;
    text-decoration: none;
}

.app-chino-admin-btn-chino.primary {
    background: #4671bb;
    color: white;
    box-shadow: 0 4px 10px rgba(70, 113, 187, 0.3);
    white-space: nowrap;
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
    width: 32px;
    height: 32px;
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

/* Table */
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

.action-col {
    white-space: nowrap;
}

/* Mobile View */
.mobile-view-list {
    display: none;
    flex-direction: column;
    gap: 16px;
}

.category-card-mobile {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 16px;
}

.mobile-card-header {
    border-bottom: 1px dashed #eee;
    padding-bottom: 8px;
    color: #aaa;
    font-size: 12px;
}

.mobile-card-body {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.input-group label {
    display: block;
    font-size: 12px;
    color: #4671bb;
    margin-bottom: 4px;
}

.mobile-card-actions {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 8px;
    padding-top: 12px;
    border-top: 1px solid #f5f5f5;
}

.app-chino-admin-btn-chino.small {
    padding: 6px 12px;
    font-size: 12px;
    background: rgba(70, 113, 187, 0.1);
    color: #4671bb;
}

.app-chino-admin-btn-chino.small.save {
    background: rgba(46, 204, 113, 0.15);
    color: #27ae60;
}

.app-chino-admin-btn-chino.small.delete {
    background: rgba(228, 86, 73, 0.15);
    color: #e45649;
}

/* Responsive */
@media (max-width: 768px) {
    .desktop-view {
        display: none;
    }

    .mobile-view-list {
        display: flex;
    }

    .input-grid-category {
        grid-template-columns: 1fr;
    }

    .app-chino-admin-btn-chino.primary {
        width: 100%;
    }

    .admin-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }
}
</style>