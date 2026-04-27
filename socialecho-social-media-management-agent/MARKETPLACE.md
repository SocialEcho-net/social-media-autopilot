# 发布到 Dify Marketplace（开发者速查）

本文对应官方文档：  
[发布到 Dify Marketplace](https://docs.dify.ai/zh/develop-plugin/publishing/marketplace-listing/release-to-dify-marketplace)

## 1. 发布前自检（与文档一致）

1. 完成插件开发与自测，遵守 [贡献者行为准则](https://docs.dify.ai/zh/develop-plugin/publishing/standards/contributor-covenant-code-of-conduct)。  
2. 按 [隐私数据保护指南](https://docs.dify.ai/zh/develop-plugin/publishing/standards/privacy-protection-guidelines) 编写 **`PRIVACY.md`**。  
3. 在 `manifest.yaml` 中已声明 **`privacy: PRIVACY.md`**（本仓库已满足）。  
4. 元数据、工具描述、凭据帮助文案清晰可读（建议含 **en_US** 与 **zh_Hans**；见 [通用规范](https://docs.dify.ai/zh/develop-plugin/features-and-specs/plugin-types/general-specifications)）。  
5. 本地打 **`*.difypkg` 包**（见下）。

## 2. 打包

在**插件根目录的上一级**执行（需已安装 Dify 插件 CLI，`dify version` 有输出）：

```bash
cd "path/to/parent"
dify plugin package ./socialecho-social-media-management-agent
```

会生成与插件元数据同版本号的 **`*.difypkg` 文件**。

## 3. 提交到官方仓库（给「别人在 Marketplace 里装」用）

1. **Fork** [langgenius/dify-plugins](https://github.com/langgenius/dify-plugins)。  
2. 在 fork 中**于你的个人或组织「文件夹」**下，上传新的 **`.difypkg`**。  
3. 按该仓库的 **PR Template** 开 **Pull Request** 到官方仓库。  
4. **审核**：通常 **1 周内**开始处理；**14 天**无响应可能被标为过期、**30 天**未处理可能被关闭（可重新开 PR 或新 PR，以仓库规则为准）。  
5. 合并后，插件会出现在 [Dify Marketplace](https://marketplace.dify.ai/)。

公测/迭代阶段**尽量避免对用户产生破坏性变更**；重大 API 变更时同步迁移说明。

## 4. 维护

- 响应 Issue/评论；对 SocialEcho 接口变更时同步发新版 `.difypkg` 并再次走 Marketplace PR 流程。  
- 本插件源码与版本号维护建议与 Git 仓库 [SocialEcho-net/social-media-autopilot](https://github.com/SocialEcho-net/social-media-autopilot) 中 `socialecho-social-media-management-agent` 目录一致。

## 5. 与「仅本地上传安装」的区别

- **本地上传 / 内部分发**：只需把 `.difypkg` 在**你自己的 Dify 工作区**中安装即可（见 [打包为本地文件并分享](https://docs.dify.ai/zh/develop-plugin/publishing/marketplace-listing/release-by-file)），**不经过**上一步 PR。  
- **本文件描述的是对全体用户的 Marketplace 上架流程。**
