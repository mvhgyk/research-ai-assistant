# Research AI Assistant

科研文献 AI 助手。

## 项目目标

本项目计划实现一个面向科研论文阅读的 AI 助手，后续支持：

- PDF 论文解析
- 大模型摘要生成
- Markdown 笔记导出
- RAG 文献问答
- 简单 Agent 工具调用

## 当前进度

- [x] 项目结构初始化
- [ ] Python 文件处理
- [ ] Markdown 笔记生成
- [ ] LLM API 调用
- [ ] PDF 解析
- [ ] RAG 问答系统

## 技术栈

- Python
- Git
- Markdown
- 后续计划：FastAPI, FAISS, RAG, Tool Calling

## 项目结构

```text
research-ai-assistant/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── data/
│   ├── papers/
│   └── outputs/
├── logs/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── file_utils.py
│   └── markdown_writer.py
└── notes/
```
