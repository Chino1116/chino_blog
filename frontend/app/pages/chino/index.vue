<template>
    <main class="app-chino-admin-main-chino center-layout">
        <div class="app-chino-admin-card-chino login-card">
            <header class="login-header">
                <div><img src="~/assets/img/chino.png" alt="CHINO" class="logo-circle" /></div>
                <h1>CHINO ADMIN</h1>
                <p class="subtitle">管理系统身份验证</p>
            </header>

            <div class="form-group">
                <input v-model="keyInput" type="password" placeholder="请输入后台密钥..."
                    class="app-chino-admin-input-chino big-input" @keyup.enter="saveKey" />
                <button @click="saveKey" class="app-chino-admin-btn-chino primary full-btn">
                    验证并登录
                </button>
            </div>

            <transition name="fade">
                <div v-if="keySaved" class="success-message">
                    <span class="icon"></span> 密钥已保存，系统已就绪
                </div>
            </transition>

            <hr class="divider" v-if="keySaved" />

            <div class="nav-grid" :class="{ disabled: !keySaved }">
                <NuxtLink to="/chino/article" class="nav-card">
                    <span class="nav-icon"></span>
                    <span class="nav-text">文章管理</span>
                    <span class="nav-arrow">→</span>
                </NuxtLink>
                <NuxtLink to="/chino/category" class="nav-card">
                    <span class="nav-icon"></span>
                    <span class="nav-text">分类管理</span>
                    <span class="nav-arrow">→</span>
                </NuxtLink>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const keyInput = ref('');
const keySaved = ref(false);

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return '';
}

function setCookie(name, value, days = 30) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
}

onMounted(() => {
    const savedKey = getCookie('chino_admin_key');
    if (savedKey) {
        keyInput.value = savedKey;
        keySaved.value = true;
    }
});

function saveKey() {
    if (keyInput.value) {
        setCookie('chino_admin_key', keyInput.value, 30);
        keySaved.value = true;
    }
}
</script>

<style scoped>
/* === 核心容器优化 === */
.app-chino-admin-main-chino {
    /* 这里的 calc(100vh - 128px) 是你的核心需求 */
    height: calc(100vh - 128px);
    width: 100%;
    background-color: transparent;
    /* 全透明背景 */
    overflow-y: auto;
    /* 内部滚动 */
    overflow-x: hidden;
    /* 防止横向溢出 */
    box-sizing: border-box;
    padding: 20px;

    /* Flex用于居中，但在容器高度变小时允许滚动内容被展示 */
    display: flex;
    align-items: center;
    justify-content: center;

    /* 字体设置 */
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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

.login-card {
    background: #fff;
    border-radius: 24px;
    box-shadow: 0 10px 40px rgba(70, 113, 187, 0.08);
    padding: 40px;
    width: 100%;
    max-width: 420px;
    text-align: center;
    /* 边框略微调整以适应不同背景 */
    border: 1px solid rgba(70, 113, 187, 0.1);
    /* 防止在小屏幕下贴边 */
    margin: auto;
}

/* Header Styles */
.logo-circle {
    width: 64px;
    height: 64px;
    background: rgba(70, 113, 187, 0.1);
    color: #4671bb;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: 0 auto 20px;
}

.login-header h1 {
    margin: 0;
    color: #202e62;
    font-size: 1.5rem;
    letter-spacing: 1px;
}

.subtitle {
    margin: 8px 0 32px;
    color: #b8b3bc;
    font-size: 0.9rem;
}

/* Inputs & Buttons */
.form-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.app-chino-admin-input-chino {
    padding: 12px 16px;
    border: 1px solid rgba(70, 113, 187, 0.2);
    border-radius: 10px;
    font-size: 15px;
    background: #fafafa;
    transition: all 0.2s;
    text-align: center;
    width: 100%;
    box-sizing: border-box;
}

.app-chino-admin-input-chino:focus {
    border-color: #4671bb;
    background: #fff;
    outline: none;
    box-shadow: 0 0 0 4px rgba(70, 113, 187, 0.1);
}

.app-chino-admin-btn-chino.primary {
    background: #4671bb;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(70, 113, 187, 0.2);
    width: 100%;
}

.app-chino-admin-btn-chino.primary:hover {
    background: #3a5da0;
    transform: translateY(-1px);
}

/* Success State */
.success-message {
    margin-top: 16px;
    color: #27ae60;
    font-size: 14px;
    background: rgba(39, 174, 96, 0.1);
    padding: 8px;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.divider {
    border: 0;
    height: 1px;
    background: #eee;
    margin: 32px 0 24px;
}

/* Navigation Cards */
.nav-grid {
    display: grid;
    gap: 16px;
    transition: opacity 0.3s;
}

.nav-grid.disabled {
    opacity: 0.5;
    pointer-events: none;
    filter: grayscale(1);
}

.nav-card {
    display: flex;
    align-items: center;
    padding: 16px 20px;
    background: #fff;
    border: 1px solid rgba(70, 113, 187, 0.15);
    border-radius: 12px;
    text-decoration: none;
    color: #202e62;
    transition: all 0.2s;
}

.nav-card:hover {
    background: rgba(70, 113, 187, 0.03);
    border-color: #4671bb;
    transform: translateX(4px);
}

.nav-icon {
    font-size: 20px;
    margin-right: 12px;
}

.nav-text {
    font-weight: 500;
    flex: 1;
    text-align: left;
}

.nav-arrow {
    color: #b8b3bc;
    font-weight: bold;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>