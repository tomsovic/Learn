class MyRouter(object):
    def db_for_read(self, model, **hints):
        print("read model._meta.app_label:{}, model._meta.model_name:{}".format(
            model._meta.app_label,  model._meta.model_name))
        return 'slave'

    def db_for_write(self, model, **hints):
        print("write model._meta.app_label:{}, model._meta.model_name:{}".format(
            model._meta.app_label,  model._meta.model_name))
        return 'default'

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     允许使用相同数据库的应用程序之间存在任何关系。
    #     Allow any relation between apps that use the same database."""
    #     print("=========================", obj1, obj2, **hints)
    #     db_obj1 = obj1._meta.app_label
    #     db_obj2 = obj2._meta.app_label
    #     if db_obj1 and db_obj2:
    #         if db_obj1 == db_obj2:
    #             print(db_obj1, db_obj2)
    #             return True
    #         else:
    #             return False
    #     return None