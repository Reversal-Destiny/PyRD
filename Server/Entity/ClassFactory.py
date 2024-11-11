import mod.server.extraServerApi as serverApi


# 实体管理类工厂
class EntityManagerClassFactory:
    def __init__(self):
        self.entity_manager_mapping = {}

    def add_entity_manager_mapping(self, entity_identify, entity_class):
        # 添加实体identify和类的映射
        self.entity_manager_mapping[entity_identify] = entity_class

    def assign_entity_manager_class(self, entity_str):
        # 使用传入字符串获取实体的identify
        engine_type = serverApi.GetEngineCompFactory().CreateEngineType(entity_str)
        entity_identify = engine_type.GetEngineTypeStr()

        # 查询映射中是否存在对应类
        if entity_identify in self.entity_manager_mapping:
            return self.entity_manager_mapping[entity_identify](entity_str)
        else:
            return None
