### AI Translation

[简体中文](README.md) | **English** | [日本語](README_ja.md)

# Statement

0. This project is strictly prohibited for commercial use (probably no one will use it, but I still have to say it).
1. The design inspiration and motivation for Chino Blog's style come from [KUN's Blog](https://soft.moe/), but no code was directly copied. Everything was designed by my own feeling and a bit of personal aesthetics, then handed over to AI for implementation.
2. This is a project produced by <font color="red">personal understanding + AI</font>, so please forgive the messy code. It was made in just two and a half days and is only a semi-finished product, not very user-friendly.
3. I chose to open source it because someone might like it.
4. If for any reason you dislike this project, please leave. If you like it, please give me a STAR, and you can deploy and use it yourself according to the instructions below.
5. This is my first time writing a Markdown document, so it may not be easy to understand.

#

[![image](https://img.cdn1.vip/i/691d8b2dbfdd8_1763543853.webp)](https://github.com/Chino1116/chino_blog)

# <font color="#4671bb">Chino's Blog</font>

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

## Maybe Some Nonsense Below

> Q: <font color="#4671bb">Why did you want to make this?</font><br>A: Because I personally don't like using other people's programs, they never feel right, and modifying them is also a pain (actually, I can't understand the code at all).<br><br>
> Q: <font color="#4671bb">What was the trigger for making this?</font><br>A: The cutest Galgame website was born in 2023, and then I visited the blog of the site owner [KUN's Blog](https://soft.moe/). It was so beautiful and exactly my taste, so on November 16, 2025, I decided to buy my long-desired .moe domain. For the prefix, I chose "chino" from the Romanized name of Chino Kafuu (かふう ちの) from "Is the Order a Rabbit?". Thus, chino.moe was born, and that night I started making the blog program. Chino's Blog was born in this context.<br><br>
> Q: <font color="#4671bb">Tech Stack: NUXT + Flask + SQLite</font><br>A: The frontend uses NUXT4 because I didn't want to hardcode the frontend content and wanted SEO. Since I have no technical skills, I chose NUXT from many frameworks. I just need to write code. The backend uses Python's Flask library + SQLite database for convenience, as I don't want to configure anything (because I can't).

### Screenshot of KUN's Blog (Super God)

![image](https://img.cdn1.vip/i/691d8ce77f01f_1763544295.webp)

# <font color="#4671bb">Deployment Tutorial</font>

## Frontend Deployment

## Note

<font color="red">Please replace the backend API before building the frontend.</font>

### Prerequisites

Node.js version 20.x or higher is installed.

### 1. Frontend Build

Download the source code locally, enter the frontend folder, and run the following command to output the .output folder.

```bash
npx nuxt build
```

### 2. Deploy Frontend to Server

Upload the .output folder to the server and use the following command to start. The frontend will run on <font color="#4671bb">localhost:3000</font> by default. Use reverse proxy to bind your domain.

```bash
node .output/server/index.mjs
```

### 3. Admin Panel Address

Visit <font color="#4671bb">localhost:3000/chino</font> to enter the admin panel. You can change the admin address by renaming the pages/chino folder in the source code, e.g., to pages/admin, then the admin address will be <font color="#4671bb">localhost:3000/admin</font>.

## Backend Deployment

## Note

Modify the blog admin password in the following code in backend/route/admin.py.

```python
# Admin key (recommended to read from environment variable or config file)
ADMIN_KEY = "Chino_Secret_1116"
```

### Prerequisites

Download and enter the backend folder, then run the following command to install Python dependencies.

```bash
pip install -r requirements.txt
```

### Deploy Backend to Server

Enter the backend folder and run the following command. The backend will run on <font color="#4671bb">localhost:8000</font>. Use reverse proxy to bind your domain to the backend API.

Run the following command to start:

```bash
python chino.py
```

or

```bash
python3 chino.py
```

### Blog Deployment Complete

## If you've read this far, you must be interested in this project. Please give a free Star!

### Star Trend

[![Star History Chart](https://api.star-history.com/svg?repos=Chino1116/chino_blog&type=date&legend=top-left)](https://www.star-history.com/#Chino1116/chino_blog&type=date&legend=top-left)
