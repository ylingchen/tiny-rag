from huggingface_hub import snapshot_download  

  
# 指定模型的仓库ID  

repo_id = "Qwen/Qwen2-7B-Instruct"  

# 指定下载到的本地目录  

local_dir = "./models/Qwen2-7B-Instruct"  

  

# 使用snapshot_download下载模型  

snapshot_download(  

    repo_id=repo_id,  

    local_dir=local_dir,  

    resume_download=True  # 如果下载中断，可以恢复下载  

)  
# from modelscope.hub.snapshot_download import snapshot_download

# model_dir = snapshot_download('iic/nlp_bert_document-segmentation_chinese-base', cache_dir='./models/nlp_bert_document-segmentation_chinese-base')
