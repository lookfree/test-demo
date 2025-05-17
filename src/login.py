#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
登录功能模块
"""

import hashlib
import jwt
import datetime
from typing import Dict, Optional, Union


class LoginManager:
    """用户登录管理类"""
    
    def __init__(self, secret_key: str, token_expire_minutes: int = 60):
        """
        初始化登录管理器
        
        Args:
            secret_key: JWT签名密钥
            token_expire_minutes: 令牌过期时间（分钟）
        """
        self.secret_key = secret_key
        self.token_expire_minutes = token_expire_minutes
        self.users_db = {}  # 示例中使用内存存储，实际应用中应替换为数据库
        
    def hash_password(self, password: str) -> str:
        """
        密码哈希函数
        
        Args:
            password: 明文密码
            
        Returns:
            哈希后的密码
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username: str, password: str, email: str) -> bool:
        """
        注册新用户
        
        Args:
            username: 用户名
            password: 密码
            email: 电子邮件
            
        Returns:
            注册是否成功
        """
        if username in self.users_db:
            return False
            
        self.users_db[username] = {
            "password_hash": self.hash_password(password),
            "email": email,
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        return True
        
    def authenticate(self, username: str, password: str) -> bool:
        """
        验证用户凭据
        
        Args:
            username: 用户名
            password: 密码
            
        Returns:
            验证是否成功
        """
        if username not in self.users_db:
            return False
            
        stored_hash = self.users_db[username]["password_hash"]
        return stored_hash == self.hash_password(password)
        
    def create_token(self, username: str) -> str:
        """
        为已验证用户创建JWT令牌
        
        Args:
            username: 用户名
            
        Returns:
            JWT令牌
        """
        payload = {
            "sub": username,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=self.token_expire_minutes)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")
        
    def verify_token(self, token: str) -> Optional[str]:
        """
        验证JWT令牌
        
        Args:
            token: JWT令牌
            
        Returns:
            成功则返回用户名，失败则返回None
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload["sub"]
        except jwt.PyJWTError:
            return None
            
    def get_user_info(self, username: str) -> Optional[Dict]:
        """
        获取用户信息
        
        Args:
            username: 用户名
            
        Returns:
            用户信息字典
        """
        if username not in self.users_db:
            return None
            
        user_info = self.users_db[username].copy()
        user_info.pop("password_hash", None)  # 移除密码哈希
        return user_info


# 示例用法
if __name__ == "__main__":
    login_manager = LoginManager(secret_key="your-secret-key")
    
    # 注册用户
    login_manager.register_user("testuser", "password123", "test@example.com")
    
    # 验证用户
    is_valid = login_manager.authenticate("testuser", "password123")
    print(f"Authentication: {'成功' if is_valid else '失败'}")
    
    # 创建令牌
    if is_valid:
        token = login_manager.create_token("testuser")
        print(f"Token: {token}")
        
        # 验证令牌
        username = login_manager.verify_token(token)
        print(f"Token verification: {'成功' if username else '失败'}")