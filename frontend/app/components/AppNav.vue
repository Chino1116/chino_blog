<template>
    <div class="app-nav-chino">
        <nuxt-link to="/" class="app-nav-title-chino">
            <img src="~/assets/img/chino.png" alt="Chino's Blog" width="36" height="36">
            CHINO's Blog
        </nuxt-link>

        <!-- <div class="app-nav-search-chino">
        </div> -->

        <div class="app-nav-menu-chino desktop-only-chino" :style="menuGridStyle">
            <template v-if="menuItems && menuItems.length > 0">
                <nuxt-link v-for="item in menuItems" :key="item.id" :to="item.route">
                    {{ item.name }}
                </nuxt-link>
            </template>
        </div>

        <div class="app-nav-social-chino desktop-only-chino">
            <a href="https://github.com/Chino1116/chino_blog" target="_blank">
                <svg t="1763467732067" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="28261" width="20" height="20">
                    <path
                        d="M251.008 795.861333c-12.8-8.533333-23.808-19.413333-36.693333-34.816a2146.986667 2146.986667 0 0 1-19.882667-24.704c-19.754667-24.533333-32.213333-35.84-45.098667-40.490666a42.666667 42.666667 0 0 1 28.842667-80.341334c32.085333 11.52 53.802667 31.36 83.072 67.754667-4.010667-4.992 14.506667 18.218667 18.474667 22.997333 8.106667 9.685333 14.08 15.573333 18.773333 18.688 8.704 5.845333 25.045333 8.362667 49.066667 5.973334 0.981333-16.298667 4.010667-32.128 8.618666-46.72C229.546667 653.226667 157.866667 571.562667 157.866667 411.306667c0-52.906667 15.786667-100.522667 45.141333-140.458667-9.301333-38.144-7.893333-84.266667 12.885333-136.192a42.666667 42.666667 0 0 1 26.88-24.832c3.456-1.024 5.418667-1.493333 8.874667-2.005333 34.261333-5.248 82.645333 7.253333 145.706667 46.762666A500.522667 500.522667 0 0 1 512 141.44c38.912 0 77.568 4.437333 114.517333 13.141333 63.018667-39.808 111.488-52.309333 146.005334-46.762666 3.626667 0.554667 6.698667 1.28 9.301333 2.133333a42.666667 42.666667 0 0 1 26.282667 24.746667c20.778667 51.882667 22.186667 98.005333 12.885333 136.106666 29.482667 39.936 45.141333 87.253333 45.141333 140.501334 0 160.298667-71.424 241.706667-198.058666 272.725333 5.333333 17.706667 8.106667 37.504 8.106666 58.88a12820.992 12820.992 0 0 1-0.512 115.882667 42.666667 42.666667 0 0 1-0.810666 83.541333c-48.597333 9.728-84.608-22.698667-84.608-65.066667l0.085333-19.029333 0.213333-30.08c0.213333-30.208 0.298667-57.088 0.298667-85.248 0-29.738667-7.808-49.152-18.133333-58.026667-28.202667-24.32-13.909333-70.613333 23.04-74.752 126.592-14.208 185.045333-63.232 185.045333-198.826666 0-40.746667-13.312-74.410667-38.954667-102.570667a42.666667 42.666667 0 0 1-8.106666-44.586667c7.082667-17.664 10.112-40.832 4.096-68.864l-0.426667 0.128c-20.949333 5.930667-47.36 18.773333-79.274667 40.490667a42.666667 42.666667 0 0 1-35.541333 5.76A410.709333 410.709333 0 0 0 512 226.773333c-37.973333 0-75.605333 5.077333-110.592 14.933334a42.666667 42.666667 0 0 1-35.413333-5.717334c-32.085333-21.632-58.624-34.432-79.701334-40.405333-6.144 27.861333-3.114667 50.944 3.925334 68.565333a42.666667 42.666667 0 0 1-8.064 44.586667C256.682667 336.64 243.2 370.944 243.2 411.306667c0 135.338667 58.496 184.661333 184.405333 198.826666 36.906667 4.138667 51.242667 50.218667 23.210667 74.581334-8.192 7.168-18.304 31.232-18.304 58.197333v134.4c0 42.069333-35.626667 73.6-83.626667 65.194667a42.666667 42.666667 0 0 1-1.706666-83.712v-42.24c-38.826667 2.602667-70.912-3.754667-96.170667-20.693334z"
                        p-id="28262" fill="#4671bb"></path>
                </svg>
            </a>

            <a href="https://www.bilibili.com/" target="_blank">
                <svg class="icon" viewBox="0 0 1024 1024" width="20" height="20">
                    <path
                        d="M306.005333 117.632L444.330667 256h135.296l138.368-138.325333a42.666667 42.666667 0 0 1 60.373333 60.373333L700.330667 256H789.333333A149.333333 149.333333 0 0 1 938.666667 405.333333v341.333334a149.333333 149.333333 0 0 1-149.333334 149.333333h-554.666666A149.333333 149.333333 0 0 1 85.333333 746.666667v-341.333334A149.333333 149.333333 0 0 1 234.666667 256h88.96L245.632 177.962667a42.666667 42.666667 0 0 1 60.373333-60.373334zM789.333333 341.333333h-554.666666a64 64 0 0 0-63.701334 57.856L170.666667 405.333333v341.333334a64 64 0 0 0 57.856 63.701333L234.666667 810.666667h554.666666a64 64 0 0 0 63.701334-57.856L853.333333 746.666667v-341.333334A64 64 0 0 0 789.333333 341.333333zM341.333333 469.333333a42.666667 42.666667 0 0 1 42.666667 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666666-42.666667z m341.333334 0a42.666667 42.666667 0 0 1 42.666666 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666667-42.666667z"
                        fill="#4671bb"></path>
                </svg>
            </a>

            <a href="javascript:void(0)" @click="showShareModal = true">
                <svg class="icon" viewBox="0 0 1024 1024" width="20" height="20">
                    <path
                        d="M426.666667 128v85.333333H213.333333v597.333334h597.333334v-213.333334h85.333333v256a42.666667 42.666667 0 0 1-42.666667 42.666667H170.666667a42.666667 42.666667 0 0 1-42.666667-42.666667V170.666667a42.666667 42.666667 0 0 1 42.666667-42.666667h256z m323.669333 85.333333H554.666667V128h341.333333v341.333333h-85.333333V273.664l-298.666667 298.666667L451.669333 512l298.666667-298.666667z"
                        fill="#4671bb"></path>
                </svg>
            </a>
        </div>
        <div class="app-nav-theme-switch-chino desktop-only-chino" :class="{ 'app-nav-is-dark-chino': isDarkMode }"
            @click="toggleTheme">
            <div class="app-nav-theme-handle-chino">
                <svg v-if="!isDarkMode" viewBox="0 0 1024 1024" width="12" height="12">
                    <path
                        d="M512 768a256 256 0 1 1 0-512 256 256 0 0 1 0 512z m0-85.333333a170.666667 170.666667 0 1 0 0-341.333334 170.666667 170.666667 0 0 0 0 341.333334zM469.333333 42.666667h85.333334v128h-85.333334V42.666667z m0 810.666666h85.333334v128h-85.333334v-128zM149.973333 210.304l60.330667-60.330667L300.8 240.469333 240.469333 300.8 149.973333 210.346667zM723.2 783.530667l60.330667-60.330667 90.496 90.496-60.330667 60.330667-90.496-90.496z m90.496-633.6l60.330667 60.373333-90.496 90.496-60.330667-60.330667 90.496-90.496zM240.469333 723.2l60.330667 60.330667-90.496 90.496-60.330667-60.330667 90.496-90.496zM981.333333 469.333333v85.333334h-128v-85.333334h128zM170.666667 469.333333v85.333334H42.666667v-85.333334h128z"
                        p-id="27622" fill="#4671bb"></path>
                </svg>
                <svg v-else viewBox="0 0 1024 1024" width="12" height="12">
                    <path
                        d="M485.546667 86.144a320 320 0 1 0 452.266666 452.266667C924.245333 761.770667 738.816 938.666667 512.042667 938.666667 276.352 938.666667 85.333333 747.648 85.333333 512c0-226.773333 176.896-412.202667 400.213334-425.856z"
                        fill="#4671bb"></path>
                </svg>
            </div>
        </div>
        <div class="app-nav-mobile-toggle-chino mobile-only-chino" @click="toggleMobileMenu">
            <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="25928"
                width="24" height="24">
                <path
                    d="M896 768v85.333333H128v-85.333333h768zM296.533333 151.466667v422.4L85.333333 362.666667l211.2-211.2zM896 469.333333v85.333334h-384v-85.333334h384z m0-298.666666v85.333333h-384V170.666667h384z"
                    p-id="25929" fill="#4671bb"></path>
            </svg>
        </div>

        <transition name="fade">
            <div v-if="isMobileMenuOpen" class="app-nav-mobile-layout-chino mobile-only-chino">

                <div class="app-nav-mobile-menu-panel-chino">
                    <div class="mobile-menu-list-chino">
                        <template v-if="menuItems && menuItems.length > 0">
                            <nuxt-link v-for="item in menuItems" :key="item.id" :to="item.route"
                                class="app-mobile-menu-item-chino" @click="isMobileMenuOpen = false">
                                {{ item.name }}
                            </nuxt-link>
                        </template>
                    </div>

                    <div class="mobile-appearance-section-chino">
                        <div class="appearance-box-chino">
                            <span>Appearance</span>
                            <div class="app-nav-theme-switch-chino" :class="{ 'app-nav-is-dark-chino': isDarkMode }"
                                @click="toggleTheme">
                                <div class="app-nav-theme-handle-chino">
                                    <svg v-if="!isDarkMode" viewBox="0 0 1024 1024" width="12" height="12">
                                        <path
                                            d="M512 768a256 256 0 1 1 0-512 256 256 0 0 1 0 512z m0-85.333333a170.666667 170.666667 0 1 0 0-341.333334 170.666667 170.666667 0 0 0 0 341.333334zM469.333333 42.666667h85.333334v128h-85.333334V42.666667z m0 810.666666h85.333334v128h-85.333334v-128zM149.973333 210.304l60.330667-60.330667L300.8 240.469333 240.469333 300.8 149.973333 210.346667zM723.2 783.530667l60.330667-60.330667 90.496 90.496-60.330667 60.330667-90.496-90.496z m90.496-633.6l60.330667 60.373333-90.496 90.496-60.330667-60.330667 90.496-90.496zM240.469333 723.2l60.330667 60.330667-90.496 90.496-60.330667-60.330667 90.496-90.496zM981.333333 469.333333v85.333334h-128v-85.333334h128zM170.666667 469.333333v85.333334H42.666667v-85.333334h128z"
                                            p-id="27622" fill="#4671bb"></path>
                                    </svg>
                                    <svg v-else viewBox="0 0 1024 1024" width="12" height="12">
                                        <path
                                            d="M485.546667 86.144a320 320 0 1 0 452.266666 452.266667C924.245333 761.770667 738.816 938.666667 512.042667 938.666667 276.352 938.666667 85.333333 747.648 85.333333 512c0-226.773333 176.896-412.202667 400.213334-425.856z"
                                            fill="#4671bb"></path>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="mobile-social-icons-chino">
                        <a href="https://github.com/" target="_blank">
                            <svg t="1763467732067" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="28261" width="24" height="24">
                                <path
                                    d="M251.008 795.861333c-12.8-8.533333-23.808-19.413333-36.693333-34.816a2146.986667 2146.986667 0 0 1-19.882667-24.704c-19.754667-24.533333-32.213333-35.84-45.098667-40.490666a42.666667 42.666667 0 0 1 28.842667-80.341334c32.085333 11.52 53.802667 31.36 83.072 67.754667-4.010667-4.992 14.506667 18.218667 18.474667 22.997333 8.106667 9.685333 14.08 15.573333 18.773333 18.688 8.704 5.845333 25.045333 8.362667 49.066667 5.973334 0.981333-16.298667 4.010667-32.128 8.618666-46.72C229.546667 653.226667 157.866667 571.562667 157.866667 411.306667c0-52.906667 15.786667-100.522667 45.141333-140.458667-9.301333-38.144-7.893333-84.266667 12.885333-136.192a42.666667 42.666667 0 0 1 26.88-24.832c3.456-1.024 5.418667-1.493333 8.874667-2.005333 34.261333-5.248 82.645333 7.253333 145.706667 46.762666A500.522667 500.522667 0 0 1 512 141.44c38.912 0 77.568 4.437333 114.517333 13.141333 63.018667-39.808 111.488-52.309333 146.005334-46.762666 3.626667 0.554667 6.698667 1.28 9.301333 2.133333a42.666667 42.666667 0 0 1 26.282667 24.746667c20.778667 51.882667 22.186667 98.005333 12.885333 136.106666 29.482667 39.936 45.141333 87.253333 45.141333 140.501334 0 160.298667-71.424 241.706667-198.058666 272.725333 5.333333 17.706667 8.106667 37.504 8.106666 58.88a12820.992 12820.992 0 0 1-0.512 115.882667 42.666667 42.666667 0 0 1-0.810666 83.541333c-48.597333 9.728-84.608-22.698667-84.608-65.066667l0.085333-19.029333 0.213333-30.08c0.213333-30.208 0.298667-57.088 0.298667-85.248 0-29.738667-7.808-49.152-18.133333-58.026667-28.202667-24.32-13.909333-70.613333 23.04-74.752 126.592-14.208 185.045333-63.232 185.045333-198.826666 0-40.746667-13.312-74.410667-38.954667-102.570667a42.666667 42.666667 0 0 1-8.106666-44.586667c7.082667-17.664 10.112-40.832 4.096-68.864l-0.426667 0.128c-20.949333 5.930667-47.36 18.773333-79.274667 40.490667a42.666667 42.666667 0 0 1-35.541333 5.76A410.709333 410.709333 0 0 0 512 226.773333c-37.973333 0-75.605333 5.077333-110.592 14.933334a42.666667 42.666667 0 0 1-35.413333-5.717334c-32.085333-21.632-58.624-34.432-79.701334-40.405333-6.144 27.861333-3.114667 50.944 3.925334 68.565333a42.666667 42.666667 0 0 1-8.064 44.586667C256.682667 336.64 243.2 370.944 243.2 411.306667c0 135.338667 58.496 184.661333 184.405333 198.826666 36.906667 4.138667 51.242667 50.218667 23.210667 74.581334-8.192 7.168-18.304 31.232-18.304 58.197333v134.4c0 42.069333-35.626667 73.6-83.626667 65.194667a42.666667 42.666667 0 0 1-1.706666-83.712v-42.24c-38.826667 2.602667-70.912-3.754667-96.170667-20.693334z"
                                    p-id="28262" fill="#4671bb"></path>
                            </svg>
                        </a>
                        <a href="https://www.bilibili.com/" target="_blank">
                            <svg class="icon" viewBox="0 0 1024 1024" width="24" height="24">
                                <path
                                    d="M306.005333 117.632L444.330667 256h135.296l138.368-138.325333a42.666667 42.666667 0 0 1 60.373333 60.373333L700.330667 256H789.333333A149.333333 149.333333 0 0 1 938.666667 405.333333v341.333334a149.333333 149.333333 0 0 1-149.333334 149.333333h-554.666666A149.333333 149.333333 0 0 1 85.333333 746.666667v-341.333334A149.333333 149.333333 0 0 1 234.666667 256h88.96L245.632 177.962667a42.666667 42.666667 0 0 1 60.373333-60.373334zM789.333333 341.333333h-554.666666a64 64 0 0 0-63.701334 57.856L170.666667 405.333333v341.333334a64 64 0 0 0 57.856 63.701333L234.666667 810.666667h554.666666a64 64 0 0 0 63.701334-57.856L853.333333 746.666667v-341.333334A64 64 0 0 0 789.333333 341.333333zM341.333333 469.333333a42.666667 42.666667 0 0 1 42.666667 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666666-42.666667z m341.333334 0a42.666667 42.666667 0 0 1 42.666666 42.666667v85.333333a42.666667 42.666667 0 0 1-85.333333 0v-85.333333a42.666667 42.666667 0 0 1 42.666667-42.666667z"
                                    fill="#4671bb"></path>
                            </svg>
                        </a>
                        <a href="javascript:void(0)" @click="showShareModal = true">
                            <svg class="icon" viewBox="0 0 1024 1024" width="24" height="24">
                                <path
                                    d="M426.666667 128v85.333333H213.333333v597.333334h597.333334v-213.333334h85.333333v256a42.666667 42.666667 0 0 1-42.666667 42.666667H170.666667a42.666667 42.666667 0 0 1-42.666667-42.666667V170.666667a42.666667 42.666667 0 0 1 42.666667-42.666667h256z m323.669333 85.333333H554.666667V128h341.333333v341.333333h-85.333333V273.664l-298.666667 298.666667L451.669333 512l298.666667-298.666667z"
                                    fill="#4671bb"></path>
                            </svg>
                        </a>
                    </div>
                </div>

                <div class="app-nav-mobile-mask-rest-chino" @click="isMobileMenuOpen = false"></div>
            </div>
        </transition>

        <div v-if="showShareModal" class="app-nav-share-modal-chino" @click="showShareModal = false">
            <div class="app-nav-share-container-chino" @click.stop>
                <div class="app-nav-share-header-chino">
                    <h3>分享到</h3>
                    <button class="app-nav-share-close-chino" @click="showShareModal = false">×</button>
                </div>
                <div class="app-nav-share-content-chino">
                    <div class="app-nav-share-grid-chino">
                        <div class="app-nav-share-item-chino" @click="shareToQQ">
                            <div class="app-nav-share-icon-chino app-nav-share-qq-chino">
                                <svg class="icon" viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M748.16 533.930667l-29.696-76.629334c0-0.896 0.426667-16 0.426667-23.808C718.848 302.421333 659.029333 170.666667 512 170.666667s-206.848 131.754667-206.848 262.826666c0 7.808 0.384 22.912 0.426667 23.808l-29.696 76.629334c-8.106667 21.973333-16.213333 44.8-22.058667 64.426666-28.032 93.397333-18.944 132.053333-12.032 132.906667 14.848 1.834667 57.770667-70.314667 57.770667-70.314667 0 41.813333 20.821333 96.341333 65.792 135.68-16.810667 5.418667-37.461333 13.653333-50.688 23.765334-11.946667 9.130667-10.453333 18.389333-8.277334 22.186666 9.386667 16.426667 161.706667 10.453333 205.653334 5.333334 43.946667 5.12 196.224 11.093333 205.653333-5.376 2.133333-3.754667 3.626667-13.013333-8.277333-22.144-13.269333-10.112-33.92-18.346667-50.773334-23.722667 45.013333-39.381333 65.792-93.952 65.792-135.722667 0 0 42.965333 72.149333 57.813334 70.314667 6.912-0.853333 16.128-39.594667-12.074667-132.949333-5.973333-19.754667-13.866667-42.410667-22.016-64.384z m43.562667 351.018666c-15.914667 27.818667-35.541333 38.058667-61.354667 45.098667a209.493333 209.493333 0 0 1-33.877333 5.888c-18.773333 1.92-42.069333 2.773333-68.821334 2.730667a1417.813333 1417.813333 0 0 1-115.626666-4.949334c-29.525333 2.773333-76.16 4.864-115.626667 4.949334a685.653333 685.653333 0 0 1-68.864-2.730667 210.261333 210.261333 0 0 1-33.834667-5.888c-25.813333-6.997333-45.44-17.28-61.44-45.184a97.024 97.024 0 0 1-10.197333-70.485333c-25.258667-5.632-42.709333-20.608-54.570667-38.869334a103.68 103.68 0 0 1-13.184-30.293333 171.861333 171.861333 0 0 1-4.949333-47.189333c0.554667-33.493333 7.978667-75.178667 22.698667-124.245334 5.973333-19.882667 13.952-43.008 24.234666-70.613333l23.594667-61.013333a661.162667 661.162667 0 0 1-0.085333-8.661334C219.818667 239.146667 323.754667 85.333333 512 85.333333c188.288 0 292.181333 153.813333 292.181333 348.16l-0.042666 8.661334 23.594666 61.013333 0.426667 1.109333c9.6 25.856 17.621333 49.194667 23.722667 69.376 14.848 49.066667 22.272 90.837333 22.826666 124.416 0.298667 17.365333-1.28 33.109333-5.034666 47.274667-2.816 10.496-6.869333 20.48-13.226667 30.208-11.776 18.218667-29.184 33.109333-54.485333 38.826667 5.546667 23.637333 2.346667 48.64-10.24 70.570666z"
                                        p-id="25959" fill="#4671bb"></path>
                                </svg>
                            </div>
                            <span>QQ</span>
                        </div>
                        <div class="app-nav-share-item-chino" @click="shareToQzone">
                            <div class="app-nav-share-icon-chino app-nav-share-qzone-chino">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z"
                                        fill="#b8b3bc" />
                                    <path
                                        d="M512 336c-97.2 0-176 78.8-176 176s78.8 176 176 176 176-78.8 176-176-78.8-176-176-176z"
                                        fill="#b8b3bc" />
                                </svg>
                            </div>
                            <span>QQ空间</span>
                        </div>
                        <div class="app-nav-share-item-chino" @click="shareToWeibo">
                            <div class="app-nav-share-icon-chino app-nav-share-weibo-chino">
                                <svg class="icon" viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M861.610667 605.738667c0 143.445333-193.28 274.090667-423.509334 274.090666C226.901333 879.786667 42.666667 776.064 42.666667 620.117333c0-83.072 50.346667-174.378667 138.24-259.754666 120.832-117.162667 265.770667-172.074667 335.274666-104.448 21.248 20.565333 30.848 47.872 30.677334 79.274666 84.266667-24.576 155.733333-17.237333 191.274666 32.085334 19.157333 26.581333 22.698667 58.88 13.909334 94.165333 64.469333 26.026667 109.568 75.52 109.568 144.298667z m-189.44-88.32c-16.469333-17.493333-17.066667-39.253333-8.448-60.16 8.874667-21.674667 9.088-34.645333 5.12-40.106667-11.264-15.701333-65.408-15.488-136.277334 13.269333a87.168 87.168 0 0 1-21.717333 5.973334c-14.677333 1.962667-28.629333 0.042667-41.941333-11.306667-17.877333-15.317333-20.224-36.48-13.738667-56.149333 9.173333-28.586667 7.68-45.909333 1.578667-51.84-7.936-7.68-33.152-8.149333-70.784 6.101333-45.610667 17.28-98.048 52.224-145.664 98.389333C167.466667 492.373333 128 563.968 128 620.117333c0 95.658667 139.776 174.378667 310.101333 174.378667 188.586667 0 338.176-101.12 338.176-188.757333 0-31.488-27.178667-57.130667-71.381333-70.485334-16.810667-4.821333-22.869333-7.296-32.725333-17.792z m300.970666-68.992a42.666667 42.666667 0 0 1-82.602666-21.418667 170.666667 170.666667 0 0 0-200.234667-210.090667 42.666667 42.666667 0 1 1-17.365333-83.541333 256 256 0 0 1 300.202666 315.050667z"
                                        fill="#4671bb"></path>
                                </svg>
                            </div>
                            <span>微博</span>
                        </div>
                        <div class="app-nav-share-item-chino" @click="shareToWechat">
                            <div class="app-nav-share-icon-chino app-nav-share-wechat-chino">
                                <svg class="icon" viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M369.792 491.136a54.442667 54.442667 0 0 1-54.826667-54.826667c0-30.634667 24.192-54.869333 54.826667-54.869333 30.592 0 54.826667 24.234667 54.826667 54.869333 0 30.592-24.234667 54.826667-54.826667 54.826667z m284.416 0a54.442667 54.442667 0 0 1-54.826667-54.826667c0-30.634667 24.234667-54.869333 54.826667-54.869333 30.634667 0 54.826667 24.234667 54.826667 54.869333 0 30.592-24.192 54.826667-54.826667 54.826667z m-363.093333 328.704l30.506666-18.602667a170.666667 170.666667 0 0 1 115.413334-22.869333c9.045333 1.408 16.469333 2.517333 22.186666 3.242667 17.322667 2.304 34.986667 3.456 52.778667 3.456 188.586667 0 337.066667-128.938667 337.066667-281.6S700.586667 221.866667 512 221.866667s-337.066667 128.938667-337.066667 281.6c0 58.282667 21.333333 114.048 61.098667 161.322666 2.048 2.432 5.12 5.845333 9.130667 10.026667a170.666667 170.666667 0 0 1 46.976 132.352l-1.066667 12.672z m-26.88 116.352a42.666667 42.666667 0 0 1-65.152-39.68l8.021333-96.426667a85.333333 85.333333 0 0 0-23.466667-66.176A298.368 298.368 0 0 1 170.666667 719.701333c-50.944-60.629333-81.066667-135.381333-81.066667-216.234666 0-202.666667 189.098667-366.933333 422.4-366.933334s422.4 164.266667 422.4 366.933333-189.098667 366.933333-422.4 366.933333c-21.76 0-43.093333-1.408-63.957333-4.181333a1007.36 1007.36 0 0 1-24.277334-3.584 85.333333 85.333333 0 0 0-57.728 11.434666l-101.845333 62.122667z"
                                        fill="#4b424c"></path>
                                </svg>
                            </div>
                            <span>微信</span>
                        </div>
                        <div class="app-nav-share-item-chino" @click="shareToMoments">
                            <div class="app-nav-share-icon-chino app-nav-share-moments-chino">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z"
                                        fill="#4b424c" />
                                    <circle cx="512" cy="512" r="120" fill="#4b424c" />
                                </svg>
                            </div>
                            <span>朋友圈</span>
                        </div>
                        <div class="app-nav-share-item-chino" @click="copyLink">
                            <div class="app-nav-share-icon-chino app-nav-share-link-chino">
                                <svg viewBox="0 0 1024 1024" width="32" height="32">
                                    <path
                                        d="M574 665.4a8 8 0 0 0-11.3 0L440.3 788a32 32 0 0 1-45.3 0L236 629a32 32 0 0 1 0-45.3l159-159.3a8 8 0 0 0 0-11.3l-45.2-45.3a8 8 0 0 0-11.3 0L179.4 527a96 96 0 0 0 0 135.9l159 159.3a96 96 0 0 0 135.9 0l159-159.3a8 8 0 0 0 0-11.3l-45.3-45.2zM844.6 361.4l-159-159.3a96 96 0 0 0-135.9 0l-159 159.3a8 8 0 0 0 0 11.3l45.3 45.3a8 8 0 0 0 11.3 0l159-159.3a32 32 0 0 1 45.3 0l159 159.3a32 32 0 0 1 0 45.3l-159 159.3a8 8 0 0 0 0-135.9z"
                                        fill="#4b424c" />
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
import { ref, computed, watch, onMounted } from 'vue'
import { useFetch, useCookie } from '#app'

// 1. 获取数据
const { data: menuItems } = await useFetch('http://localhost:8000/category')

const menuGridStyle = computed(() => {
    const count = menuItems.value?.length
    return {
        gridTemplateColumns: `repeat(${count}, 1fr)`
    }
})

const showShareModal = ref(false)
const isMobileMenuOpen = ref(false)

// 2. 夜间模式状态管理 (Cookie 持久化)
// 默认为 'light'
const colorMode = useCookie('chino-color-mode', { default: () => 'light', maxAge: 60 * 60 * 24 * 365 })
const isDarkMode = computed(() => colorMode.value === 'dark')

// 3. 应用主题函数 (优化滤镜参数版)
const applyTheme = () => {
    if (process.client) {
        const html = document.documentElement;
        // 1. 获取背景图片元素
        const bgElement = document.querySelector('.app-background-chino');

        if (colorMode.value === 'dark') {
            // --- 父元素 (全局) 滤镜 ---
            html.style.filter = 'invert(0.95) hue-rotate(180deg) brightness(0.9) contrast(0.9)';

            html.classList.add('is-dark-mode-global');
            html.style.colorScheme = 'dark';

            // --- 关键修复开始 ---

            // A. 防止背景图片消失：强制让 body 背景透明
            // 原因：html 反色后，body 默认的白色背景会变成不透明的深灰色，可能盖住位于底层的背景图。
            document.body.style.backgroundColor = 'transparent';

            // B. 还原背景图片颜色：负负得正
            if (bgElement) {
                // 再次反转 0.95 + 旋转 180度 = 还原颜色
                // 亮度/对比度放大 1.11倍 (1/0.9) = 抵消变暗
                bgElement.style.filter = 'invert(0.95) hue-rotate(180deg) brightness(1.11) contrast(1.11)';

                // 强制开启 GPU 硬件加速，防止滤镜导致的渲染层级丢失
                bgElement.style.transform = 'translateZ(0)';
            }
            // --- 关键修复结束 ---

        } else {
            // --- 恢复正常模式 ---
            html.style.filter = '';
            html.classList.remove('is-dark-mode-global');
            html.style.colorScheme = '';

            // 清除 body 的强制透明
            document.body.style.backgroundColor = '';

            // 清除背景图的滤镜
            if (bgElement) {
                bgElement.style.filter = '';
                bgElement.style.transform = '';
            }
        }
    }
}

// 4. 切换主题
const toggleTheme = () => {
    colorMode.value = colorMode.value === 'light' ? 'dark' : 'light'
}

// 5. 监听状态变化并初始化
watch(colorMode, applyTheme)
onMounted(() => {
    applyTheme()
})

const toggleMobileMenu = () => {
    isMobileMenuOpen.value = !isMobileMenuOpen.value
}

// 辅助函数
const isMobile = () => {
    if (process.client) {
        return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
    }
    return false
}

const getPageInfo = () => {
    if (process.client) {
        return {
            url: window.location.href,
            title: document.title || 'CHINO\'s Blog',
            desc: document.querySelector('meta[name="description"]')?.content || '来看看这个有趣的内容！'
        }
    }
    return { url: '', title: '', desc: '' }
}

const openApp = (scheme, fallback = null) => {
    if (isMobile()) {
        const iframe = document.createElement('iframe')
        iframe.style.display = 'none'
        iframe.src = scheme
        document.body.appendChild(iframe)
        setTimeout(() => { document.body.removeChild(iframe); if (fallback) window.open(fallback, '_blank') }, 2000)
    } else if (fallback) {
        window.open(fallback, '_blank')
    }
}

// Share functions
const shareToQQ = () => { const { url, title, desc } = getPageInfo(); openApp(`mqqapi://share/qq_share?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&desc=${encodeURIComponent(desc)}`, `https://connect.qq.com/widget/shareqq/index.html?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&summary=${encodeURIComponent(desc)}`); showShareModal.value = false }
const shareToQzone = () => { const { url, title, desc } = getPageInfo(); openApp(`mqqapi://share/to_qzone?src_type=web&url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&summary=${encodeURIComponent(desc)}`, `https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&summary=${encodeURIComponent(desc)}`); showShareModal.value = false }
const shareToWeibo = () => { const { url, title } = getPageInfo(); openApp(`sinaweibo://sendweibo?content=${encodeURIComponent(title + ' ' + url)}`, `https://service.weibo.com/share/share.php?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`); showShareModal.value = false }
const shareToWechat = () => { const { url } = getPageInfo(); isMobile() ? (openApp(`weixin://share/${encodeURIComponent(url)}`), setTimeout(() => showShareTip('请使用微信扫一扫功能分享当前页面'), 2500)) : showShareTip('请使用微信扫一扫功能分享当前页面'); showShareModal.value = false }
const shareToMoments = () => { if (isMobile()) { openApp(`weixin://share/moments/${encodeURIComponent(window.location.href)}`); setTimeout(() => showShareTip('请在微信中打开页面，点击右上角菜单分享到朋友圈'), 2500) } else { showShareTip('请在微信中打开页面，点击右上角菜单分享到朋友圈') } showShareModal.value = false }
const copyLink = async () => { if (process.client) { try { await navigator.clipboard.writeText(window.location.href); showShareTip('链接已复制到剪贴板') } catch (err) { const ta = document.createElement('textarea'); ta.value = window.location.href; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta); showShareTip('链接已复制到剪贴板') } } showShareModal.value = false }

const showShareTip = (message) => {
    const tip = document.createElement('div')
    tip.style.cssText = `position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0, 0, 0, 0.8); color: white; padding: 12px 20px; border-radius: 8px; font-size: 14px; z-index: 10000; max-width: 80%; text-align: center; animation: fadeIn 0.3s ease;`
    tip.textContent = message
    const style = document.createElement('style'); style.textContent = `@keyframes fadeIn { from { opacity: 0; transform: translate(-50%, -50%) scale(0.9); } to { opacity: 1; transform: translate(-50%, -50%) scale(1); } }`; document.head.appendChild(style); document.body.appendChild(tip)
    setTimeout(() => { tip.style.animation = 'fadeIn 0.3s ease reverse'; setTimeout(() => { document.body.removeChild(tip); document.head.removeChild(style) }, 300) }, 2000)
}
</script>

<style>
/* 全局样式：防止图片在夜间模式下被二次反转成底片 */
.is-dark-mode-global img,
.is-dark-mode-global video,
.is-dark-mode-global iframe {
    filter: invert(1) hue-rotate(180deg);
}

.app-nav-chino {
    display: grid;
    justify-content: center;
    grid-template-columns: 3fr 3fr 0.5fr 0.2fr;
    align-items: center;
    width: 82%;
    margin: 0 auto;
    /* 确保导航栏在最上层 */
    position: relative;
    z-index: 100;
}

.app-nav-title-chino {
    margin: 0;
    padding: 0;
    font-size: 20px;
    font-weight: bold;
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 8px;
}

.app-nav-search-chino {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 8px;
}

.app-nav-menu-chino {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    align-items: center;
    gap: 8px;
    justify-self: end;
    padding: 0 20px;
    text-align: center;
}

/* 桌面端 Social Icon 区域，现在包含 Theme 切换按钮 */
.app-nav-social-chino {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
    padding: 0 20px;
}

.app-nav-social-chino::before {
    content: '';
    width: 1px;
    height: 20px;
    background-color: #4671bb;
    margin-right: 12px;
}

.app-nav-social-chino::after {
    content: '';
    width: 1px;
    height: 20px;
    background-color: #4671bb;
    margin-left: 12px;
}

.app-nav-social-chino a,
.desktop-theme-btn-chino {
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s ease;
}

.desktop-theme-btn-chino:hover {
    transform: rotate(15deg);
}

/* 默认隐藏移动端元素 */
.mobile-only-chino {
    display: none;
}

/* --- 全局胶囊切换开关样式 (桌面端 & 移动端共用) --- */
.app-nav-theme-switch-chino {
    width: 50px;
    height: 26px;
    background-color: #fff;
    border: 1px solid #4671bb;
    border-radius: 13px;
    position: relative;
    cursor: pointer;
    transition: all 0.3s;
    /* 确保桌面端垂直居中 */
    display: flex;
    align-items: center;
    flex-shrink: 0;
}

.app-nav-theme-switch-chino.app-nav-is-dark-chino {
    background-color: #4671bb;
}

.app-nav-theme-handle-chino {
    width: 22px;
    height: 22px;
    background-color: #fff;
    /* 始终是白色圆点 */
    border-radius: 50%;
    position: absolute;
    top: 1px;
    left: 1px;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

/* 当夜间模式激活时，圆点移动到右边 */
.app-nav-theme-switch-chino.app-nav-is-dark-chino .app-nav-theme-handle-chino {
    left: 25px;
}

/* 竖屏移动端适配 @media (max-aspect-ratio: 1/1) */
@media (max-aspect-ratio: 1/1) {
    .app-nav-chino {
        width: 100%;
        padding: 0 10px;
        /* 调整Grid：Logo - Search(Hidden/Small) - MenuToggle */
        grid-template-columns: 3fr 0.5fr;
    }

    .app-nav-title-chino {
        margin: 0 20px;
    }

    /* 隐藏桌面端元素 */
    .desktop-only-chino {
        display: none !important;
    }

    /* 显示移动端元素 */
    .mobile-only-chino {
        display: block;
    }

    .app-nav-mobile-toggle-chino {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 20px;
        cursor: pointer;
    }

    /* --- 遮罩层修改：避开顶部64px，并使用 Grid 布局 --- 
       将整个菜单系统作为一个全屏容器 (Top 64px) */
    .app-nav-mobile-layout-chino {
        position: fixed;
        top: 64px;
        /* 避开顶部导航 */
        left: 0;
        width: 100vw;
        height: calc(100vh - 64px);
        /* 填满剩余 */
        z-index: 998;
        display: grid;
        grid-template-rows: max-content 1fr;
        /* 核心：上部分自适应，下部分占满剩余 */
    }

    /* 上部分：半透明菜单面板 */
    .app-nav-mobile-menu-panel-chino {
        background: rgba(255, 255, 255, 0.8) !important;
        /* 0.2 透明度 */
        backdrop-filter: blur(1px) !important;
        -webkit-backdrop-filter: blur(1px) !important;
        /* border-bottom-left-radius: 24px;
        border-bottom-right-radius: 24px; */
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        overflow-y: auto;
        max-height: 80vh;
        /* 限制最大高度 */
    }

    /* 下部分：遮罩区域 (点击关闭) */
    /* 因为使用了 Grid，这个 div 会自然占据剩下的空间，不会与上面的菜单重叠 */
    .app-nav-mobile-mask-rest-chino {
        background: rgba(0, 0, 0, 0.2);
        /* 半透明黑 */
        backdrop-filter: blur(2px);
        width: 100%;
        height: 100%;
        /* 占满 grid 的 1fr */
    }

    .mobile-menu-list-chino {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .app-mobile-menu-item-chino {
        padding: 15px 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        font-size: 16px;
        color: #333;
        text-decoration: none;
        display: block;
    }

    .app-mobile-menu-item-chino:last-child {
        border-bottom: none;
    }

    /* Appearance / Night Mode Section */
    .mobile-appearance-section-chino {
        margin-top: 30px;
        width: 100%;
    }

    .appearance-box-chino {
        background-color: rgba(238, 247, 255, 0.8);
        border-radius: 12px;
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #555;
        font-size: 15px;
        font-weight: 500;
    }

    /* 移动端社交图标区 - 底部居中 */
    .mobile-social-icons-chino {
        margin-top: 30px;
        padding-bottom: 10px;
        display: flex;
        justify-content: center;
        gap: 30px;
    }

    .mobile-social-icons-chino a {
        color: #666;
        display: flex;
        align-items: center;
    }
}

/* 菜单淡入淡出动画 */
.slide-down-enter-active,
.slide-down-leave-active,
.fade-enter-active,
.fade-leave-active {
    transition: all 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
    opacity: 0;
    transform: translateY(-10px);
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

/* Share Modal Styles (Unchanged) */
.app-nav-share-modal-chino {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(75, 66, 76, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(4px);
}

.app-nav-share-container-chino {
    background: #f3f2f4;
    border-radius: 16px;
    width: 320px;
    max-height: 400px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(75, 66, 76, 0.15);
}

.app-nav-share-header-chino {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 20px;
    border-bottom: 1px solid #dedef0;
    background: #4671bb;
}

.app-nav-share-header-chino h3 {
    margin: 0;
    padding: 0;
    font-size: 18px;
    color: #f3f2f4;
    font-weight: 500;
}

.app-nav-share-close-chino {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #f3f2f4;
    padding: 0;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: all 0.3s ease;
}

.app-nav-share-content-chino {
    padding: 20px;
}

.app-nav-share-grid-chino {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}

.app-nav-share-item-chino {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
    padding: 8px;
    border-radius: 12px;
}

.app-nav-share-icon-chino {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 8px;
    background: #f3f2f4;
    transition: all 0.3s ease;
}

.app-nav-share-qq-chino svg {
    fill: #4671bb;
}

.app-nav-share-qzone-chino svg {
    fill: #b8b3bc;
}

.app-nav-share-weibo-chino svg {
    fill: #4671bb;
}

.app-nav-share-wechat-chino svg,
.app-nav-share-moments-chino svg {
    fill: #4b424c;
}

.app-nav-share-link-chino svg {
    fill: #4b424c;
}

.app-nav-share-item-chino span {
    font-size: 12px;
    color: #4b424c;
    font-weight: 500;
    transition: color 0.3s ease;
}

.app-nav-share-item-chino:hover span {
    color: #2a4d8a;
}

@media (max-width: 480px) {
    .app-nav-share-container-chino {
        width: 280px;
    }

    .app-nav-share-header-chino {
        padding: 12px 16px;
    }

    .app-nav-share-header-chino h3 {
        font-size: 16px;
    }

    .app-nav-share-content-chino {
        padding: 16px;
    }

    .app-nav-share-grid-chino {
        gap: 12px;
    }

    .app-nav-share-icon-chino {
        width: 44px;
        height: 44px;
    }

    .app-nav-share-icon-chino svg {
        width: 24px;
        height: 24px;
    }

    .app-nav-share-item-chino span {
        font-size: 11px;
    }
}
</style>