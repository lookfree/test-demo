# test-demo
test-demo is an open source project that provides a self-hostable sandbox for Agents to execute commands, read/write files, browse the web, operate iOS/Android. The sandbox can be used as a computer/phone/pad for agent. See "Features" section for details.

This project is based on the technology behind gru.ai. It has been tested over 100000 Agent jobs.

For advanced scenarios, we also kept the ability to run sandboxes in k8s cluster locally or remotely.

As MCP is getting more and more popular, we also implemented a MCP server to make it easy to be directly integrated into MCP client such as Claude Desktop/Cursor.

Features
Terminal
Execute any linux command
Execute python scripts directly
Share session across invokes [under-development]
File
Mount host machine folders into sandbox
Access sandbox files through http links
Read file content in multi-modal
Write/re-write files
Edit files [under-development]
Search files [under-development]
Browser
Open any url, return content in multi-modal
Download from any url [under-development]
Operate browser by instructions [under-development]
Human take over [under-development]
HTTP Server
Start http service on any folder on demand [under-development]
SDKs
Python SDK: Install using pip install pygbox. See PyPI for details.
Typescript SDK
MCP
Standard MCP support
Integrate Claude Desktop & Cursor
