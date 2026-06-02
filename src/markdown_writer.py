from datetime import datetime


def build_paper_note(title: str, abstract: str) -> str:
    """
    根据论文标题和摘要，生成 Markdown 格式的论文笔记。
    """
    today = datetime.now().strftime("%Y-%m-%d")

    note = f"""# {title}

## 阅读日期

{today}

## 摘要原文

{abstract}

## AI 总结

暂未生成。

## 关键词

暂未生成。

## 研究问题

暂未生成。

## 我的理解

这里后续自己填写。

"""
    return note