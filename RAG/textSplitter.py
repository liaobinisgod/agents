## 文档切分 1加载文档  切分块
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = UnstructuredWordDocumentLoader(
    file_path='assets/sample.docx',
    mode="single"
).load()

chunks =  RecursiveCharacterTextSplitter(
          separators=["\n\n", "\n", "。", "！", "？", "……", "，", ""], # 递归分割
          chunk_size=400, # 切分块大小
          chunk_overlap= 50, # 每个重叠块的长度
          length_function=len,## 可选：计算文本长度的函数，默认为字符串长度，可自定义函数来实现按token数切分
        add_start_index=True,#可选：块的元数据中添加此块起始索引
).split_documents(docs)
print(chunks)
