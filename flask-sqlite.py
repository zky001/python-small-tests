# -*- coding: utf-8 -*-


import sqlite3
from flask import current_app
from flask import _app_ctx_stack as stack


class SQLite3(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """ 典型的 Flask 扩展的初始化方式""
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        """ 连接到 sqlite 数据库"""
        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])

    def teardown(self, exception):
        """ 关闭 sqlite 链接"
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        """ 单例模式在这里：使用 flask._app_ctx_stack 存放 sqlite 链接,
        每次获取数据库链接时都通过 connection 获取"""
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db
