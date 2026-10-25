# 小圆 · Xiaoyuan

一只长发、黑框眼镜、白色上衣的二次元 Q 版桌宠。提供透明动画图集、九组动作、十六个看向方向、源图和离线预览。

![小圆挥手](previews/waving.gif)

## 快速预览

下载并解压后，双击 `preview.html`，在浏览器里选择动作或查看转头动画。无需安装，也不需要联网。

- [完整动作 GIF](previews/all-states.gif)
- [完整动作视频](previews/all-states.mp4)
- [动作总览](previews/contact-sheet.png)
- [方向总览](previews/directions.png)

## 仓库内容

| 路径 | 内容 |
| --- | --- |
| `assets/xiaoyuan-spritesheet.png` | 最终透明 PNG 图集，1536 × 2288 |
| `sprite.json` | 图集布局、帧数、时长和方向 |
| `preview.html` | 离线交互动画预览 |
| `previews/` | GIF、MP4、动作与方向总览 |
| `source-art/character.png` | 二次元基础角色 |
| `source-art/strips/` | 经过选定的各组生成源图，保留品红背景 |
| `docs/` | 接入说明、制作记录、提示词说明 |
| `reports/quality-summary.json` | 发布图集的检查摘要 |
| `tools/check_atlas.py` | 图集结构检查工具 |

## 使用方式

这是图像素材项目。你可以将图集接入自己的桌宠或动画播放器；它已在创作者的 ChatGPT 宠物库中验证并使用。

仓库本身不包含 ChatGPT 客户端或独立 Windows 桌宠程序。是否能在你的 ChatGPT 账户中导入自定义图集，取决于客户端所提供的入口；仓库文件不会自动安装宠物。

技术接入请看 [图集说明](docs/SPRITESHEET.md)。制作方法见 [制作记录](docs/CREATION.md)。

## 许可证与署名

- **图像素材、动画、源图和文档：CC BY 4.0**，允许分享、修改与商业使用，请保留署名、许可证链接并注明改动。
- **预览页面和检查工具：MIT**。

建议署名：`小圆 / Xiaoyuan — Xiaoyuan contributors，CC BY 4.0；如有修改请注明。`

详见 [LICENSE](LICENSE)、[素材许可证](licenses/CC-BY-4.0.txt) 和 [代码许可证](licenses/MIT.txt)。素材授权不代表人物为使用者或产品背书。

## 关于创作

本项目使用 AI 辅助生成角色及动作，再进行透明背景处理、尺寸对齐、图集拼装和检查。公开包中不包含参考照片、账户宠物编号、本机路径或上传会话信息。

这是个人创作项目，与 OpenAI 无隶属、赞助或官方合作关系。

## 在 GitHub 发布

新建空仓库，将本文件夹内的全部内容上传到仓库根目录即可。推荐仓库名：`xiaoyuan-desktop-pet`。仓库描述可使用：`小圆：二次元黑框眼镜桌宠，包含九组动作与十六方向透明动画素材。`

详见 [发布步骤](docs/PUBLISH.md)。
