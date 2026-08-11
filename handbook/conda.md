### 环境管理
1. conda环境导入
conda export | grep -v '^prefix' > environment.yml
2. 引用环境
conda env create -f environment.yml
3. 激活环境
conda activate env_name
4. 列出环境
conda env list
5. 删除环境
conda env remove -n env_name
6. 克隆
conda create -n new_env --clone old_env
7. 更新
conda env update -f environment.yml --prune (删除yaml没有的包)

### 包管理
1. 当前环境中安装包
    - conda install name
    - conda install name=1.2.3 指定版本
        - 常见渠道 defaults,conda-forge,bioconda,pytorch
    - conda install -c conda-forge name 指定渠道
2. 卸载包
conda remove name
3. 更新包
conda update name
4. 更新环境所有包
conda update --all
5. 列出环境已安装包
conda list
6. 搜索包
conda search name
7. 查看依赖
conda info name