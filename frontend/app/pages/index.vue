<template>
    <div class="app-main-chino">
        <div class="app-main-title-chino">
            <h1>CHINO's Blog</h1>
            <h2>CHINO's moe blog, CHINO IS THE CUTEST!</h2>
            <p>Kafuu Chino, the cutest girl in the world!</p>
            <div class="app-main-links-buttons-chino">
                <nuxt-link to="/article/1" class="app-main-button-chino active">Example</nuxt-link>
                <nuxt-link to="/category/blog" class="app-main-button-chino">Blog</nuxt-link>
                <nuxt-link to="/category/project" class="app-main-button-chino">Project</nuxt-link>
                <nuxt-link to="/category/vps" class="app-main-button-chino">Vps</nuxt-link>
                <nuxt-link to="/category/about" class="app-main-button-chino">About</nuxt-link>
                <nuxt-link to="/category/friends" class="app-main-button-chino">Friends</nuxt-link>
            </div>
        </div>
        <div class="app-main-image-chino">
            <img src="~/assets/img/chino.png" alt="">
        </div>
    </div>
</template>

<style>
.app-main-chino {
    display: grid;
    padding: 50px 12%;
    gap: 40px;
    width: 100%;
    height: calc(100vh - 128px);
    margin: 0 auto;
    grid-template-columns: 1fr 1fr;
    grid-template-areas:
        "title image"
        "buttons buttons";
    overflow-y: auto;
}

.app-main-title-chino {
    grid-area: title;
    height: 70%;
    margin: 20px;
}

.app-main-title-chino h1 {
    margin: 0;
    padding: 0;
    font-size: 56px;
    background: linear-gradient(90deg, #4671bb, #b8b3bc, #dedef0, #f3f2f4);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}

.app-main-title-chino h2 {
    margin: 0;
    padding: 0;
    font-size: 46px;
    color: #4b424c;
}

.app-main-title-chino p {
    margin: 0;
    padding: 0;
    font-size: 28px;
    color: #b8b3bc;
}

.app-main-image-chino {
    grid-area: image;
    min-width: 190px;
    height: 70%;
    padding: 20px;
}

.app-main-image-chino img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

/* 导航按钮容器 */
.app-main-links-buttons-chino {
    display: grid;
    margin: 50px 0;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
    justify-content: center;
}

/* 导航按钮基础样式 */
.app-main-button-chino {
    padding: 8px 10px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 16px;
    font-weight: 500;
    transition: all 0.3s ease;
    border: 1px solid #4671bb;
    /* 背景半透明 */
    background-color: rgba(70, 113, 187, 0.1);
    color: #4671bb;
    text-align: center;
    width: 100%;
}

/* 激活状态按钮 */
.app-main-button-chino.active {
    background-color: #4671bb;
    color: #f3f2f4;
    border: none;
    border-radius: 20px;
    box-shadow: inset 0 2px 4px rgba(33, 150, 243, 0.2);
}

/* 悬停效果 */
.app-main-button-chino:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.app-main-button-chino.active:hover {
    box-shadow: inset 0 2px 4px rgba(33, 150, 243, 0.2);
}

/* 移动端响应式 - 只使用 1/1 适配 */
@media (max-aspect-ratio: 1/1) {
    .app-main-chino {
        padding: 20px 5%;
        gap: 0;
        grid-template-columns: 1fr;
        grid-template-areas:
            "image"
            "title"
            "buttons";
    }

    .app-main-image-chino {
        margin: auto 0;
        padding: 0 15%;
    }

    .app-main-title-chino {
        text-align: center;
    }

    .app-main-title-chino h1,
    .app-main-title-chino h2 {
        font-size: 32px;
    }

    .app-main-title-chino p {
        font-size: 20px;
    }

    .app-main-links-buttons-chino {
        grid-template-columns: 1fr 1fr;
        margin: 30px 20px;
    }
}
</style>