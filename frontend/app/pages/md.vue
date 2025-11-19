<template>
    <div class="app-nav-chino">
        <nuxt-link to="/" class="app-nav-title-chino">
            <img src="~/assets/img/chino.png" alt="Chino's Blog" width="36" height="36">
            CHINO's Blog
        </nuxt-link>
        <div class="app-nav-search-chino">
            <!-- <input type="text" placeholder="Search">
            <button>Search</button> -->
        </div>
        <div class="app-nav-menu-chino">
            <nuxt-link to="/">Home</nuxt-link>
            <nuxt-link to="/blog">Blog</nuxt-link>
            <nuxt-link to="/project">Project</nuxt-link>
            <nuxt-link to="/vps">Vps</nuxt-link>
            <nuxt-link to="/about">About</nuxt-link>
            <nuxt-link to="/contact">Friends</nuxt-link>
        </div>
        <div class="app-nav-social-chino">
            <a href="https://github.com/" target="_blank">
                <svg t="1763295156005" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="26070" id="mx_n_1763295156005" width="20" height="20">
                    <path
                        d="M251.008 795.861333c-12.8-8.533333-23.808-19.413333-36.693333-34.816a2146.986667 2146.986667 0 0 1-19.882667-24.704c-19.754667-24.533333-32.213333-35.84-45.098667-40.490666a42.666667 42.666667 0 0 1 28.842667-80.341334c32.085333 11.52 53.802667 31.36 83.072 67.754667-4.010667-4.992 14.506667 18.218667 18.474667 22.997333 8.106667 9.685333 14.08 15.573333 18.773333 18.688 8.704 5.845333 25.045333 8.362667 49.066667 5.973334 0.981333-16.298667 4.010667-32.128 8.618666-46.72C229.546667 653.226667 157.866667 571.562667 157.866667 411.306667c0-52.906667 15.786667-100.522667 45.141333-140.458667-9.301333-38.144-7.893333-84.266667 12.885333-136.192a42.666667 42.666667 0 0 1 26.88-24.832c3.456-1.024 5.418667-1.493333 8.874667-2.005333 34.261333-5.248 82.645333 7.253333 145.706667 46.762666A500.522667 500.522667 0 0 1 512 141.44c38.912 0 77.568 4.437333 114.517333 13.141333 63.018667-39.808 111.488-52.309333 146.005334-46.762666 3.626667 0.554667 6.698667 1.28 9.301333 2.133333a42.666667 42.666667 0 0 1 26.282667 24.746667c20.778667 51.882667 22.186667 98.005333 12.885333 136.106666 29.482667 39.936 45.141333 87.253333 45.141333 140.501334 0 160.298667-71.424 241.706667-198.058666 272.725333 5.333333 17.706667 8.106667 37.504 8.106666 58.88a12820.992 12820.992 0 0 1-0.512 115.882667 42.666667 42.666667 0 0 1-0.810666 83.541333c-48.597333 9.728-84.608-22.698667-84.608-65.066667l0.085333-19.029333 0.213333-30.08c0.213333-30.208 0.298667-57.088 0.298667-85.248 0-29.738667-7.808-49.152-18.133333-58.026667-28.202667-24.32-13.909333-70.613333 23.04-74.752 126.592-14.208 185.045333-63.232 185.045333-198.826666 0-40.746667-13.312-74.410667-38.954667-102.570667a42.666667 42.666667 0 0 1-8.106666-44.586667c7.082667-17.664 10.112-40.832 4.096-68.864l-0.426667 0.128c-20.949333 5.930667-47.36 18.773333-79.274667 40.490667a42.666667 42.666667 0 0 1-35.541333 5.76A410.709333 410.709333 0 0 0 512 226.773333c-37.973333 0-75.605333 5.077333-110.592 14.933334a42.666667 42.666667 0 0 1-35.413333-5.717334c-32.085333-21.632-58.624-34.432-79.701334-40.405333-6.144 27.861333-3.114667 50.944 3.925334 68.565333a42.666667 42.666667 0 0 1-8.064 44.586667C256.682667 336.64 243.2 370.944 243.2 411.306667c0 135.338667 58.496 184.661333 184.405333 198.826666 36.906667 4.138667 51.242667 50.218667 23.210667 74.581334-8.192 7.168-18.304 31.232-18.304 58.197333v134.4c0 42.069333-35.626667 73.6-83.626667 65.194667a42.666667 42.666667 0 0 1-1.706666-83.712v-42.24c-38.826667 2.602667-70.912-3.754667-96.170667-20.693334z"
                        p-id="26071" fill="#4671bb"></path>
                </svg>
            </a>
            <a href="https://www.bilibili.com/" target="_blank">
                <svg t="1763295462173" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="26618" id="mx_n_1763295462173" width="20" height="20">
                    <path
                        d="M306.005333 117.632L444.330667 256h135.296l138.368-138.325333a42.666667 42.666667 0 0 1 60.373333 60.373333L700.330667 256H789.333333A149.333333 149.333333 0 0 1 938.666667 405.333333v341.333334a149.333333 149.333333 0 0 1-149.333334 149.333333h-554.666666A149.333333 149.333334 0 0 1 85.333333 746.666667v-341.333334A149.333333 149.333333 0 0 1 234.666667 256h88.96L245.632 177.962667a42.666667 42.666667 0 0 1 60.373333-60.373334zM789.333333 341.333333h-554.666666a64 64 0 0 0-63.701334 57.856L170.666667 405.333333v341.333334a64 64 0 0 0 57.856 63.701333L234.666667 810.666667h554.666666a64 64 0 0 0 63.701334-57.856L853.333333 746.666667v-341.333334A64 64 0 0 0 789.333333 341.333333zM341.333333 469.333333a42.666667 42.666667 0 0 1 42.666667 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666666-42.666667z m341.333334 0a42.666667 42.666667 0 0 1 42.666666 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666667-42.666667z"
                        p-id="26619" fill="#4671bb"></path>
                </svg>
            </a>
            <!-- 修改分享按钮 -->
            <a href="javascript:void(0)" @click="showShareModal = true">
                <svg t="1763295577669" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="27221" id="mx_n_1763295577670" width="20" height="20">
                    <path
                        d="M426.666667 128v85.333333H213.333333v597.333334h597.333334v-213.333334h85.333333v256a42.666667 42.666667 0 0 1-42.666667 42.666667H170.666667a42.666667 42.666667 0 0 1-42.666667-42.666667V170.666667a42.666667 42.666667 0 0 1 42.666667-42.666667h256z m323.669333 85.333333H554.666667V128h341.333333v341.333333h-85.333333V273.664l-298.666667 298.666667L451.669333 512l298.666667-298.666667z"
                        p-id="27222" fill="#4671bb"></path>
                </svg>
            </a>
        </div>

        <!-- 分享弹窗 -->
        <div v-if="showShareModal" class="share-modal-overlay" @click="showShareModal = false">
            <div class="share-modal" @click.stop>
                <div class="share-modal-header">
                    <h3>分享到</h3>
                    <button class="close-btn" @click="showShareModal = false">×</button>
                </div>
                <div class="share-modal-content">
                    <div class="share-grid">
                        <div class="share-item" @click="shareToQQ">
                            <div class="share-icon qq">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M824.8 613.2c-16-51.4-34.4-94.6-62.7-165.3C766.5 262.2 689.3 112 511.5 112 331.7 112 256.2 265.2 261 447.9c-28.4 70.8-46.7 113.7-62.7 165.3-34 109.5-23 154.8-14.6 155.8 18 2.2 70.1-82.4 70.1-82.4 0 49 25.2 112.9 79.8 159-26.4 8.1-85.7 29.9-71.6 53.8 11.4 19.3 196.2 12.3 249.5 6.3 53.3 6 238.1 13 249.5-6.3 14.1-23.8-45.3-45.7-71.6-53.8 54.6-46.2 79.8-110.1 79.8-159 0 0 52.1 84.6 70.1 82.4 8.5-1.1 19.5-46.4-14.5-155.8z" fill="#1E88E5"/>
                                </svg>
                            </div>
                            <span>QQ</span>
                        </div>
                        <div class="share-item" @click="shareToQzone">
                            <div class="share-icon qzone">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="#FFCE00"/>
                                    <path d="M512 336c-97.2 0-176 78.8-176 176s78.8 176 176 176 176-78.8 176-176-78.8-176-176-176z" fill="#FFCE00"/>
                                </svg>
                            </div>
                            <span>QQ空间</span>
                        </div>
                        <div class="share-item" @click="shareToWeibo">
                            <div class="share-icon weibo">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M428.5 428.5c-81.9 0-148.5 66.6-148.5 148.5s66.6 148.5 148.5 148.5 148.5-66.6 148.5-148.5-66.6-148.5-148.5-148.5z" fill="#E6162D"/>
                                    <path d="M928 448c0-141.4-114.6-256-256-256H352C210.6 192 96 306.6 96 448v128c0 141.4 114.6 256 256 256h320c141.4 0 256-114.6 256-256V448z" fill="#E6162D"/>
                                </svg>
                            </div>
                            <span>微博</span>
                        </div>
                        <div class="share-item" @click="shareToWechat">
                            <div class="share-icon wechat">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M690.1 377.4c5.9 0 11.8.2 17.6.5-24.4-128.7-158.3-227.1-319.9-227.1C209 150.8 64 271.4 64 420.2c0 81.1 43.6 154.2 111.9 203.6 5.5 3.9 9.1 10.3 9.1 17.6 0 2.4-.5 4.6-1.1 6.9-5.5 20.3-14.2 52.8-14.6 54.3-.7 2.6-1.7 5.2-1.7 7.9 0 5.9 4.8 10.8 10.8 10.8 2.3 0 4.2-.9 6.2-2l70.9-40.9c5.3-3.1 11-5 17.2-5 3.2 0 6.4.5 9.5 1.4 33.1 9.5 68.8 14.8 105.7 14.8 6 0 11.9-.1 17.8-.4-7.1-21-10.9-43.1-10.9-66 0-135.8 132.2-245.8 295.3-245.8zm-194.3-86.5c23.8 0 43.1 19.3 43.1 43.1s-19.3 43.1-43.1 43.1c-23.8 0-43.1-19.3-43.1-43.1s19.3-43.1 43.1-43.1zm-215.9 86.2c-23.8 0-43.1-19.3-43.1-43.1s19.3-43.1 43.1-43.1 43.1 19.3 43.1 43.1-19.3 43.1-43.1 43.1z" fill="#1AAD19"/>
                                    <path d="M866.7 792.7c56.9-41.2 93.2-102 93.2-169.7 0-124-120.8-224.5-269.9-224.5-149 0-269.9 100.5-269.9 224.5S540.9 847.5 690 847.5c30.8 0 60.6-4.4 88.1-12.3 2.6-.8 5.2-1.2 7.9-1.2 5.2 0 9.9 1.6 14.3 4.1l59.1 34.1c1.7 1 3.3 1.7 5.2 1.7 5 0 9.1-4.1 9.1-9.1 0-2.3-.9-4.5-2.1-6.4-3.3-10.2-11.9-36.7-16.3-53.3-.5-1.9-.9-3.8-.9-5.7.1-5.9 3.1-11.2 7.6-14.7z" fill="#1AAD19"/>
                                </svg>
                            </div>
                            <span>微信</span>
                        </div>
                        <div class="share-item" @click="shareToMoments">
                            <div class="share-icon moments">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="#1AAD19"/>
                                    <circle cx="512" cy="512" r="120" fill="#1AAD19"/>
                                </svg>
                            </div>
                            <span>朋友圈</span>
                        </div>
                        <div class="share-item" @click="copyLink">
                            <div class="share-icon link">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path d="M574 665.4a8 8 0 0 0-11.3 0L440.3 788a32 32 0 0 1-45.3 0L236 629a32 32 0 0 1 0-45.3l159-159.3a8 8 0 0 0 0-11.3l-45.2-45.3a8 8 0 0 0-11.3 0L179.4 527a96 96 0 0 0 0 135.9l159 159.3a96 96 0 0 0 135.9 0l159-159.3a8 8 0 0 0 0-11.3l-45.3-45.2zM844.6 361.4l-159-159.3a96 96 0 0 0-135.9 0l-159 159.3a8 8 0 0 0 0 11.3l45.3 45.3a8 8 0 0 0 11.3 0l159-159.3a32 32 0 0 1 45.3 0l159 159.3a32 32 0 0 1 0 45.3l-159 159.3a8 8 0 0 0 0 11.3l45.3 45.3a8 8 0 0 0 11.3 0l159-159.3a96 96 0 0 0 0-135.9z" fill="#666"/>
                                </svg>
                            </div>
                            <span>复制链接</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const showShareModal = ref(false)

// 获取当前页面信息
const getPageInfo = () => {
    if (process.client) {
        return {
            url: encodeURIComponent(window.location.href),
            title: encodeURIComponent(document.title || 'CHINO\'s Blog'),
            desc: encodeURIComponent(document.querySelector('meta[name="description"]')?.content || '来看看这个有趣的内容！')
        }
    }
    return { url: '', title: '', desc: '' }
}

// 分享到QQ
const shareToQQ = () => {
    const { url, title, desc } = getPageInfo()
    window.open(`https://connect.qq.com/widget/shareqq/index.html?url=${url}&title=${title}&summary=${desc}`, '_blank', 'width=600,height=400')
    showShareModal.value = false
}

// 分享到QQ空间
const shareToQzone = () => {
    const { url, title, desc } = getPageInfo()
    window.open(`https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=${url}&title=${title}&summary=${desc}`, '_blank', 'width=600,height=400')
    showShareModal.value = false
}

// 分享到微博
const shareToWeibo = () => {
    const { url, title } = getPageInfo()
    window.open(`https://service.weibo.com/share/share.php?url=${url}&title=${title}`, '_blank', 'width=600,height=400')
    showShareModal.value = false
}

// 分享到微信（显示二维码）
const shareToWechat = () => {
    const { url } = getPageInfo()
    // 这里可以集成二维码生成库，或者显示提示
    alert('请使用微信扫一扫功能扫描当前页面二维码分享')
    showShareModal.value = false
}

// 分享到朋友圈
const shareToMoments = () => {
    alert('请在微信中打开页面，点击右上角菜单分享到朋友圈')
    showShareModal.value = false
}

// 复制链接
const copyLink = async () => {
    if (process.client) {
        try {
            await navigator.clipboard.writeText(window.location.href)
            alert('链接已复制到剪贴板')
        } catch (err) {
            // 降级方案
            const textArea = document.createElement('textarea')
            textArea.value = window.location.href
            document.body.appendChild(textArea)
            textArea.select()
            document.execCommand('copy')
            document.body.removeChild(textArea)
            alert('链接已复制到剪贴板')
        }
    }
    showShareModal.value = false
}
</script>

<style scoped>
.share-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.share-modal {
    background: white;
    border-radius: 12px;
    width: 90%;
    max-width: 500px;
    max-height: 80vh;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.share-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    border-bottom: 1px solid #eee;
}

.share-modal-header h3 {
    margin: 0;
    font-size: 18px;
    color: #333;
}

.close-btn {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #999;
    padding: 0;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.close-btn:hover {
    color: #333;
}

.share-modal-content {
    padding: 20px;
}

.share-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 20px;
}

.share-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    transition: transform 0.2s;
}

.share-item:hover {
    transform: translateY(-2px);
}

.share-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 8px;
}

.share-icon.qq {
    background: #1E88E5;
}

.share-icon.qzone {
    background: #FFCE00;
}

.share-icon.weibo {
    background: #E6162D;
}

.share-icon.wechat,
.share-icon.moments {
    background: #1AAD19;
}

.share-icon.link {
    background: #666;
}

.share-icon svg {
    fill: white;
}

.share-item span {
    font-size: 12px;
    color: #666;
}

/* 响应式设计 */
@media (max-width: 480px) {
    .share-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }
    
    .share-icon {
        width: 40px;
        height: 40px;
    }
    
    .share-icon svg {
        width: 24px;
        height: 24px;
    }
}
</style>
