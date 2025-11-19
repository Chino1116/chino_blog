<template>
    <!-- 使用 Vue Transition 实现平滑的淡入淡出 -->
    <Transition name="app-tools-fade-chino">
        <div v-if="isVisible" class="app-tools-container-chino">
            <!-- 回到顶部按钮 -->
            <button @click="scrollToTop" class="app-tool-button-chino" aria-label="Scroll to top" title="回到顶部">
                <!-- 颜色直接写死为主题色 #4671bb -->
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                    stroke="#4671bb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 19V5M5 12l7-7 7 7" />
                </svg>
            </button>

            <!-- 前往底部按钮 -->
            <button @click="scrollToBottom" class="app-tool-button-chino" aria-label="Scroll to bottom" title="前往底部">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                    stroke="#4671bb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 5v14M19 12l-7 7-7-7" />
                </svg>
            </button>
        </div>
    </Transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue';
import { useRoute } from 'vue-router';

const isVisible = ref(false);
const route = useRoute();
let scrollTarget = null; // 保存当前的滚动目标

// 你的滚动容器类名
const SCROLL_CONTAINER_SELECTOR = '.app-article-main-chino';

/**
 * 获取当前的滚动位置
 */
const getScrollTop = () => {
    if (!scrollTarget) return 0;
    if (scrollTarget === window) {
        return window.scrollY || document.documentElement.scrollTop;
    }
    return scrollTarget.scrollTop;
};

/**
 * 处理滚动事件
 */
const handleScroll = () => {
    const scrollTop = getScrollTop();
    // 滚动超过 200px 显示
    isVisible.value = scrollTop > 200;
};

/**
 * 平滑滚动到顶部
 */
const scrollToTop = () => {
    if (scrollTarget) {
        scrollTarget.scrollTo({ top: 0, behavior: 'smooth' });
    }
};

/**
 * 平滑滚动到底部
 */
const scrollToBottom = () => {
    if (scrollTarget) {
        const scrollHeight = scrollTarget === window
            ? document.documentElement.scrollHeight
            : scrollTarget.scrollHeight;
        scrollTarget.scrollTo({ top: scrollHeight, behavior: 'smooth' });
    }
};

/**
 * 绑定滚动事件
 */
const bindScrollEvent = () => {
    if (scrollTarget) {
        scrollTarget.removeEventListener('scroll', handleScroll);
    }

    const container = document.querySelector(SCROLL_CONTAINER_SELECTOR);

    if (container) {
        scrollTarget = container;
    } else {
        scrollTarget = window;
    }

    scrollTarget.addEventListener('scroll', handleScroll);
    handleScroll();
};

// --- 生命周期 ---

onMounted(() => {
    setTimeout(bindScrollEvent, 100);
});

onUnmounted(() => {
    if (scrollTarget) {
        scrollTarget.removeEventListener('scroll', handleScroll);
    }
});

// --- 路由监听 ---
watch(
    () => route.path,
    () => {
        isVisible.value = false;
        setTimeout(() => {
            bindScrollEvent();
        }, 300);
    }
);
</script>

<style scoped>
/* 工具栏容器位置调整 */
.app-tools-container-chino {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    z-index: 990;
}

/* 按钮样式 */
.app-tool-button-chino {
    width: 40px;
    height: 40px;
    padding: 0;
    border-radius: 50%;

    border: none;
    /* 背景保持白色半透明 */
    background-color: rgba(255, 255, 255, 0.9);

    /* 毛玻璃效果 */
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);

    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;

    /* 柔和的阴影 */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* 悬停效果：仅上浮和加深阴影，不改变颜色 */
.app-tool-button-chino:hover {
    transform: translateY(-3px);
    background-color: #fff;
    /* 悬停时稍微不透明一点 */
    box-shadow: 0 6px 16px rgba(70, 113, 187, 0.15);
}

/* 点击效果 */
.app-tool-button-chino:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

/* 动画优化 */
.app-tools-fade-chino-enter-active,
.app-tools-fade-chino-leave-active {
    transition: all 0.3s ease;
}

.app-tools-fade-chino-enter-from,
.app-tools-fade-chino-leave-to {
    opacity: 0;
    transform: translateY(20px) scale(0.9);
}
</style>