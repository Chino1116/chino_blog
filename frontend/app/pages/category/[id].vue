<template>
    <main class="app-article-main-chino">
        <header class="app-category-header-chino">
            <h1 class="app-category-title-chino">
                {{ id ? capitalizeFirstLetter(id) : 'Category' }}
            </h1>
            <p class="app-category-subtitle-chino">
                {{ totalArticles }} Related Article Found.
            </p>
        </header>

        <div class="app-article-center-container-chino">
            <div v-if="error" class="app-article-error-chino">
                <h2>Load Failed.</h2>
                <p>{{ error.message }}</p>
                <button @click="refresh" class="app-retry-btn-chino">Retry.</button>
            </div>

            <div v-else-if="pending" class="app-article-loading-placeholder-chino">
                <div class="loading-spinner-chino"></div>
                <p>Loading Article List...</p>
            </div>

            <div v-else-if="allArticles.length === 0" class="app-article-error-chino">
                <h2>No Article Available.</h2>
                <p>There Are No Articles Published In This Category Yet.</p>
            </div>

            <div v-else class="app-article-list-chino">
                <TransitionGroup name="list-fade">
                    <article v-for="article in displayedArticles" :key="article.id" class="app-category-card-chino"
                        @click="navigateToArticle(article.id)">
                        <div class="app-category-cover-box-chino">
                            <img v-if="article.cover" :src="article.cover" alt="cover"
                                class="app-category-cover-img-chino" loading="lazy" />
                            <div v-else class="app-category-cover-placeholder-chino">
                                <span>No Cover</span>
                            </div>
                        </div>

                        <div class="app-category-content-box-chino">
                            <h2 class="app-category-card-title-chino">
                                {{ displayValue(article.title) }}
                            </h2>

                            <p class="app-category-card-desc-chino">
                                {{ displayValue(article.description) }}
                            </p>

                            <div class="app-category-meta-footer-chino">
                                <div class="app-category-badges-chino">
                                    <span class="app-category-badge-chino app-category-badge-blue-chino">
                                        Updated On {{ formatTimeSimple(article.update_time) }}
                                    </span>
                                    <span class="app-category-badge-chino app-category-badge-light-chino">
                                        ID: {{ article.id }}
                                    </span>
                                </div>

                                <div class="app-category-info-chino">
                                    <span class="app-category-date-chino">
                                        {{ formatTimeago(article.create_time) }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </article>
                </TransitionGroup>

                <div ref="loadTrigger" class="app-scroll-trigger-chino">
                    <span v-if="isLoadingMore">Load More...</span>
                    <span v-else-if="!hasMore && displayedArticles.length > 0" class="no-more-text-chino">
                        - You've Reached The Bottom -
                    </span>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute, useRouter, useFetch, useHead } from '#app';

const route = useRoute();
const router = useRouter();
const id = route.params.id;

// --- 状态管理 ---
const allArticles = ref([]);
const displayedArticles = ref([]);
const pageSize = 10;
const currentPage = ref(1);
const isLoadingMore = ref(false);
const loadTrigger = ref(null);

// --- 工具函数 ---
const displayValue = (val) => {
    if (val === null || val === undefined || val === '') return 'Value Not Exist';
    return val;
};

const formatTimeSimple = (d) => {
    if (!d) return '-';
    const date = new Date(d * 1000);
    return `${date.getMonth() + 1}-${date.getDate()}`;
};

const formatTimeago = (d) => {
    if (!d) return '';
    const now = Date.now() / 1000;
    const diff = now - d;

    if (diff < 60) return '刚刚';
    if (diff < 3600) return `${Math.floor(diff / 60)}分钟前`;
    if (diff < 86400) return `${Math.floor(diff / 3600)}小时前`;
    if (diff < 2592000) return `${Math.floor(diff / 86400)}天前`;
    if (diff < 31536000) return `${Math.floor(diff / 2592000)}个月前`;
    return `${Math.floor(diff / 31536000)}年前`;
};

const capitalizeFirstLetter = (string) => string ? string.charAt(0).toUpperCase() + string.slice(1) : '';

// --- 数据获取 ---
const { data, pending, error, refresh } = await useFetch(`http://localhost:8000/${id}/article`, {
    key: `category-${id}`,
    transform: (res) => res.sort((a, b) => Number(b.create_time) - Number(a.create_time))
});

// --- 列表逻辑 ---
const processArticles = () => {
    if (!data.value) return;
    allArticles.value = data.value;
    currentPage.value = 1;
    displayedArticles.value = allArticles.value.slice(0, pageSize);
};

const totalArticles = computed(() => allArticles.value.length);
const hasMore = computed(() => displayedArticles.value.length < allArticles.value.length);

const loadMore = () => {
    if (!hasMore.value || isLoadingMore.value) return;
    isLoadingMore.value = true;
    setTimeout(() => {
        const nextPage = currentPage.value + 1;
        displayedArticles.value = allArticles.value.slice(0, nextPage * pageSize);
        currentPage.value = nextPage;
        isLoadingMore.value = false;
    }, 300);
};

const navigateToArticle = (articleId) => {
    router.push(`/article/${articleId}`);
};

if (data.value) processArticles();
watch(data, processArticles);

onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && hasMore.value && !isLoadingMore.value && !pending.value) {
            loadMore();
        }
    }, { root: null, threshold: 0.1 });
    if (loadTrigger.value) observer.observe(loadTrigger.value);
    watch(loadTrigger, (el) => { if (el) observer.observe(el); });
});

useHead({
    title: computed(() => `${capitalizeFirstLetter(id)} - CHINO's Blog`)
});
</script>

<style scoped>
/* --- 基础布局 (保持透明背景) --- */
.app-article-main-chino {
    width: 100%;
    height: calc(100vh - 128px);
    padding: 2rem 5%;
    margin: 0 auto;
    box-sizing: border-box;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 不设置背景色，保持透明 */
}

.app-article-center-container-chino {
    width: 100%;
    max-width: 900px;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding-bottom: 4rem;
}

.app-category-header-chino {
    text-align: center;
    margin-bottom: 2rem;
}

.app-category-title-chino {
    font-size: 2.5rem;
    /* 渐变色标题 */
    background: linear-gradient(90deg, #4671bb, #b8b3bc);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    margin: 0;
}

.app-category-subtitle-chino {
    color: #b8b3bc;
    margin-top: 0.5rem;
}

/* =========================================
   卡片样式核心 - 命名 app-category-*-chino
   ========================================= */
.app-category-card-chino {
    display: flex;
    flex-direction: row;
    /* 强制横排 */

    /* 恢复你的半透明浅蓝背景 */
    background: rgba(70, 113, 187, 0.1);
    border: 1px solid rgba(70, 113, 187, 0.2);

    border-radius: 12px;
    /*稍微大一点的圆角*/
    padding: 15px;
    gap: 15px;
    transition: all 0.3s;
    cursor: pointer;
    height: 180px;
    box-sizing: border-box;
    overflow: hidden;
}

.app-category-card-chino:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(70, 113, 187, 0.12);
    /* 悬停时稍微加深背景 */
    background-color: rgba(70, 113, 187, 0.15);
}

/* --- 左侧：封面图 --- */
.app-category-cover-box-chino {
    width: 240px;
    flex-shrink: 0;
    height: 100%;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    /* 图片背景占位色改为半透明白，适应蓝色卡片 */
    background: rgba(255, 255, 255, 0.2);
}

.app-category-cover-img-chino {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
}

.app-category-card-chino:hover .app-category-cover-img-chino {
    transform: scale(1.05);
}

.app-category-cover-placeholder-chino {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4671bb;
    font-size: 0.8rem;
    opacity: 0.7;
}

/* --- 右侧：内容区 --- */
.app-category-content-box-chino {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-width: 0;
}

/* 标题样式 - 使用深蓝色 */
.app-category-card-title-chino {
    font-size: 1.2rem;
    font-weight: 700;
    color: linear-gradient(90deg, #4671bb, #b8b3bc);
    margin: 0 0 8px 0;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* 描述样式 */
.app-category-card-desc-chino {
    font-size: 0.95rem;
    color: #4b424c;
    /* 深灰带紫 */
    line-height: 1.6;
    margin: 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    flex-grow: 1;
}

/* 底部 Meta 样式 */
.app-category-meta-footer-chino {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 10px;
}

.app-category-badges-chino {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
}

.app-category-badge-chino {
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 12px;
    transform: scale(0.9);
    transform-origin: left bottom;
    font-weight: 500;
}

/* 蓝色Badge */
.app-category-badge-blue-chino {
    background: rgba(70, 113, 187, 0.2);
    color: #4671bb;
    border: 1px solid rgba(70, 113, 187, 0.3);
}

/* 浅色Badge (ID) */
.app-category-badge-light-chino {
    background: rgba(255, 255, 255, 0.4);
    color: #666;
}

.app-category-info-chino {
    font-size: 12px;
    color: #666;
    white-space: nowrap;
    padding-bottom: 2px;
    /* 微调对齐 */
}

/* =========================================
   移动端适配
   保持横排不换行
   ========================================= */
@media (max-width: 768px) {
    .app-article-main-chino {
        padding: 1rem 3%;
    }

    .app-category-card-chino {
        padding: 10px;
        gap: 10px;
        height: 130px;
        /* 手机端高度稍小 */
    }

    .app-category-cover-box-chino {
        width: 140px;
        /* 手机端图片缩小 */
    }

    .app-category-card-title-chino {
        font-size: 1rem;
        margin-bottom: 4px;
        -webkit-line-clamp: 2;
    }

    .app-category-card-desc-chino {
        font-size: 0.8rem;
        -webkit-line-clamp: 2;
        margin-bottom: 4px;
    }

    .app-category-badge-light-chino {
        display: none;
        /* 手机端隐藏ID badge */
    }

    .app-category-meta-footer-chino {
        margin-top: 0;
    }
}

@media (max-width: 375px) {
    .app-category-cover-box-chino {
        width: 110px;
    }

    .app-category-card-desc-chino {
        -webkit-line-clamp: 1;
    }
}

/* 加载状态样式 */
.app-scroll-trigger-chino,
.app-article-error-chino {
    text-align: center;
    color: #b8b3bc;
    padding: 20px;
}

.loading-spinner-chino {
    border: 3px solid rgba(70, 113, 187, 0.1);
    border-left-color: #4671bb;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    animation: spin 1s linear infinite;
    margin: 0 auto 10px;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.list-fade-enter-active,
.list-fade-leave-active {
    transition: opacity 0.5s;
}

.list-fade-enter-from,
.list-fade-leave-to {
    opacity: 0;
}
</style>