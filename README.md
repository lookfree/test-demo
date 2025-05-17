# test-demo
test-demo is an open source project that provides a self-hostable sandbox for Agents to execute commands, read/write files, browse the web, operate iOS/Android. The sandbox can be used as a computer/phone/pad for agent. See "Features" section for details.

This project is based on the technology behind gru.ai. It has been tested over 100000 Agent jobs.

For advanced scenarios, we also kept the ability to run sandboxes in k8s cluster locally or remotely.

As MCP is getting more and more popular, we also implemented a MCP server to make it easy to be directly integrated into MCP client such as Claude Desktop/Cursor.

## 安装说明

### 系统要求
- Linux/macOS/Windows(WSL2)
- Docker 20.10+
- Python 3.8+
- 至少4GB RAM和10GB磁盘空间

### 基本安装
```bash
# 克隆仓库
git clone https://github.com/lookfree/test-demo.git
cd test-demo

# 安装依赖
pip install -r requirements.txt

# 启动服务
python setup.py install
python -m test_demo start
```

### Docker 安装
```bash
# 使用Docker运行
docker pull lookfree/test-demo:latest
docker run -p 8080:8080 lookfree/test-demo
```

### 高级部署
对于Kubernetes部署，请参考[部署文档](docs/deployment.md)。

## Features
### Terminal
- Execute any linux command
- Execute python scripts directly
- Share session across invokes [under-development]

### File
- Mount host machine folders into sandbox
- Access sandbox files through http links
- Read file content in multi-modal
- Write/re-write files
- Edit files [under-development]
- Search files [under-development]

### Browser
- Open any url, return content in multi-modal
- Download from any url [under-development]
- Operate browser by instructions [under-development]
- Human take over [under-development]

### HTTP Server
- Start http service on any folder on demand [under-development]

### SDKs
- Python SDK: Install using pip install pygbox. See PyPI for details.
- Typescript SDK

### MCP
- Standard MCP support
- Integrate Claude Desktop & Cursor