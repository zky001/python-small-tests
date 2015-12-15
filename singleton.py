class Singleton(object):
    """
    单例模式
    """
    class _A(object):
        """
       真正干活的类, 对外隐藏
        """
        def __init__(self):
            """
            完成相关数据的加载与检测
            """
            pass

        def display(self):
            """ 返回当前实例的 ID，是全局唯一的"""
            return id(self)

    # 类变量，用于存储 _A 的实例
    _instance = None

    def __init__(self):
        """ 先判断类变量中是否已经保存了 _A 的实例，如果没有则创建一个后返回"""
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, attr):
        """ 所有的属性都应该直接从 Singleton._instance 获取"""
        return getattr(self._instance, attr)


if __name__ == '__main__':
    # 创建两个实例
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), s1.display())
    print(id(s2), s2.display())
