**简体中文** | [English](README_en.md) | [日本語](README_ja.md)

# 声明

1.智乃博客样式设计灵感以及动力都来源于 [KUN's Blog](https://soft.moe/) ，但并未直接复制代码，都是凭我的感觉加上个人的一点审美丢给 AI 设计的。<br> 2.这是一个<font color="red">个人理解 + AI</font>产出的项目，乱七八糟的代码请谅解。也只是一个只花了两天半搓出来的半成品，并不好用。<br> 3.或许会有人喜欢所以我选择开源。<br> 4.若您处于任何原因不喜欢本项目请离开，喜欢的话可以给我个 STAR，也可以根据本文档后面部分自行部署使用。<br> 5.第一次写 Markdown 文档必然是不好看懂的。

#

[![image](https://img.cdn1.vip/i/691d8b2dbfdd8_1763543853.webp)](https://github.com/Chino1116/chino_blog)

# <font color="#4671bb">智乃的博客</font>

<center class="half">
<img src="https://img.cdn1.vip/i/691d8d539c502_1763544403.webp" width="580"/>
<img src="https://img.cdn1.vip/i/691d9a1a1785a_1763547674.webp" width="150"/>
</center>
<center class="half">
<img src="https://img.cdn1.vip/i/691d9b539fe20_1763547987.webp" width="150"/>
<img src="https://img.cdn1.vip/i/691d9b579106f_1763547991.webp" width="575"/>
</center>
<center class="half">
<img src="https://img.cdn1.vip/i/691d9b578c11e_1763547991.webp" width="580"/>
<img src="https://img.cdn1.vip/i/691d9b54177d7_1763547988.webp" width="150"/>
</center>

## 下面或许是废话

> Q:<font color="#4671bb">为什么想要做这个东西？</font><br>A:因为我个人不喜欢用别人的程序，总觉得用起来不顺手，改起来也不顺手（其实是我压根看不懂代码）。<br><br>
> Q:<font color="#4671bb">做这个的契机是什么？</font><br>A:一个最萌的 Galgame 网站于 2023 年诞生，而后我访问到了站长的博客 [KUN's Blog](https://soft.moe/) ，实在是太好看了太戳我的审美了，于是 2025 年 11 月 16 日我下定决心购买我心仪已久的.moe 域名，前缀从众多日本动漫角色中选择了《请问您今天要来点兔子吗？》中的香风智乃(かふう ちの)的名的罗马音（chino），最后 chino.moe 的域名就此诞生，当日晚开始了博客程序的制作，智乃的博客就在这样的背景下孕育了。<br><br>
> Q:<font color="#4671bb">技术栈 NUXT + Flask + SQLite</font><br>A:前端采用 NUXT4，因为考虑到不想写死前端内容，并且兼顾 SEO，又因为本人毫无技术，从众多前端框架中选择了 NUXT，我什么都不需要做，直接搞代码即可，后端偷懒采用我的一直使用的 Python 的 Flask 库 + SQLite 数据库，懒得配置设计任何东西，因为我不会。

### KUN's Blog 截图如下（超级神）

![image](https://img.cdn1.vip/i/691d8ce77f01f_1763544295.webp)

# <font color="#4671bb">部署教程</font>

## 前端部署

## 注意

<font color="red">前端构建前请先替换后端接口 API。</font>

### 前置条件

已安装 Node.js - 20.x 版本或更高。

### 1.前端构建

下载源码至本地后进入 frontend 文件夹，执行下面代码输出.output 文件夹。

```bash
npx nuxt build
```

### 2.前端部署至服务器

将.output 文件夹上传至服务器后使用下面命令启动，前端将会默认运行在 <font color="#4671bb">localhost:3000</font> 上，使用反向代理将域名绑定即可。

```bash
node .output/server/index.mjs
```

### 3.后台管理地址

访问 <font color="#4671bb">localhost:3000/chino</font> 进入管理后台，可以通过修改源码 pages/chino 文件夹名来修改后台地址，例如 pages/admin ，后台地址即为 <font color="#4671bb">localhost:3000/admin</font>。

## 后端部署

## 注意

在后端 route 文件夹下 admin.py 内的如下代码位置修改博客后台密码

```python
# 后台密钥（建议后续可从环境变量或配置文件读取）
ADMIN_KEY = "Chino_Secret_1116"
```

### 前置条件

下载并进入 backend 文件夹，运行下面命令安装 Python 依赖库。

```bash
pip install -r requirements.txt
```

### 后端部署至服务器

进入 backend 文件夹，运行下面命令，后端将运行在 <font color="#4671bb">localhost:8000</font>上，使用反向代理将域名绑定至后端 API 上。

执行下面命令运行即可。

```bash
python chino.py
```

或者

```bash
python3 chino.py
```

### 至此博客程序部署结束

## 都看到这里了想必你一定对本项目有兴趣，请点个免费的 Star 吧！

<!-- - Star 趋势  [![GitHub stars](https://img.shields.io/github/stars/mirai-mamori/Sakurairo?logo=github&style=social)](https://github.com/mirai-mamori/Sakurairo/stargazers)

[![Stargazers over time](https://starchart.cc/mirai-mamori/Sakurairo.svg)](https://github.com/mirai-mamori/Sakurairo/stargazers) -->
