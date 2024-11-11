import mod.server.extraServerApi as serverApi


# 实体属性查询类
class EntityAttributeQuery:
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.comp = serverApi.GetEngineCompFactory().CreateAttr(entity_id)

    def get_health(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.HEALTH)

    def get_max_health(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.HEALTH)

    def get_attack_damage(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_DAMAGE)

    def get_max_attack_damage(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_DAMAGE)

    def get_armor(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.ARMOR)

    def get_max_armor(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ARMOR)

    def get_movement_speed(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.MOVEMENT_SPEED)

    def get_max_movement_speed(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.MOVEMENT_SPEED)

    def get_attack_speed(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_SPEED)

    def get_max_attack_speed(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_SPEED)

    def get_luck(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.LUCK)

    def get_max_luck(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.LUCK)

    def get_knockback_resistance(self):
        return self._get_attr_value(serverApi.GetMinecraftEnum().AttrType.KNOCKBACK_RESISTANCE)

    def get_max_knockback_resistance(self):
        return self._get_attr_max_value(serverApi.GetMinecraftEnum().AttrType.KNOCKBACK_RESISTANCE)

    # 通用的属性获取方法
    def _get_attr_value(self, attr_type):
        # 调用GetAttrValue接口获取当前属性值
        return self.comp.GetAttrValue(attr_type)

    def _get_attr_max_value(self, attr_type):
        # 调用GetAttrMaxValue接口获取属性最大值
        return self.comp.GetAttrMaxValue(attr_type)

class EntityAttributeSetter:
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.comp = serverApi.GetEngineCompFactory().CreateAttr(entity_id)

    def set_health(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.HEALTH, value)

    def set_max_health(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.HEALTH, value)

    def set_attack_damage(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_DAMAGE, value)

    def set_max_attack_damage(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_DAMAGE, value)

    def set_armor(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.ARMOR, value)

    def set_max_armor(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ARMOR, value)

    def set_movement_speed(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.MOVEMENT_SPEED, value)

    def set_max_movement_speed(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.MOVEMENT_SPEED, value)

    def set_attack_speed(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_SPEED, value)

    def set_max_attack_speed(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.ATTACK_SPEED, value)

    def set_luck(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.LUCK, value)

    def set_max_luck(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.LUCK, value)

    def set_knockback_resistance(self, value):
        self._set_attr_value(serverApi.GetMinecraftEnum().AttrType.KNOCKBACK_RESISTANCE, value)

    def set_max_knockback_resistance(self, value):
        self._set_attr_max_value(serverApi.GetMinecraftEnum().AttrType.KNOCKBACK_RESISTANCE, value)

    # 通用的属性设置方法
    def _set_attr_value(self, attr_type, value):
        # 调用SetAttrValue接口设置当前属性值
        self.comp.SetAttrValue(attr_type, value)

    def _set_attr_max_value(self, attr_type, value):
        # 调用SetAttrMaxValue接口设置属性最大值
        self.comp.SetAttrMaxValue(attr_type, value)
