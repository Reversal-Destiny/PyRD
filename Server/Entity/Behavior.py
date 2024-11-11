import random
class Behavior:
    def __init__(self, entityId, name, weight):
        self.entityId = entityId
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        # 检测行为是否相同
        return self.entityId == other.entityId and self.name == other.name

    def can_use(self):
        # 当前行为是否可用
        return True

    def activate(self):
        # 启用行为时调用的函数
        pass

    def deactivate(self):
        # 退出行为时调用的函数
        pass



class BehaviorSelector:
    def __init__(self, entityId, current_behavior=None, behaviors=[]):
        self.entityId = entityId
        self.behaviors = behaviors
        self.current_behavior = current_behavior

    def select_behavior(self):
        # 过滤出可用的行为
        available_behaviors = [behavior for behavior in self.behaviors if behavior.can_use()]

        if not available_behaviors:
            print("No available behaviors.")
            return

        # 根据权重选择行为
        total_weight = sum(behavior.weight for behavior in available_behaviors)
        rand_value = random.uniform(0, total_weight)

        cumulative_weight = 0
        selected_behavior = None
        for behavior in available_behaviors:
            cumulative_weight += behavior.weight
            if rand_value <= cumulative_weight:
                selected_behavior = behavior
                break

        # 激活选中的行为并停用之前的行为
        if selected_behavior:
            if self.current_behavior and self.current_behavior != selected_behavior:
                self.current_behavior.deactivate()

            self.current_behavior = selected_behavior
            self.current_behavior.activate()