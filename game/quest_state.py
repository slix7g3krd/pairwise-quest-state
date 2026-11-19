"""第 52 批：任务链在分支、共享进度、跨场景时错乱：状态机用字..."""


def state_id(value):
    """返回规范化的任务状态枚举值。"""
    return str(value).strip().upper()


def branch_progress(branch, counts):
    """返回指定分支的独立进度。"""
    return counts.get(branch, 0)


def rollback_effects(effects):
    """按逆序撤销任务副作用。"""
    return list(reversed(effects))


def grant_once(key, granted):
    """判断奖励是否尚未发放。"""
    return key not in granted


def ordered_conditions(conditions):
    """按优先级排序任务条件。"""
    return sorted(conditions, key=lambda c: c["priority"])


def accept_once(quest_id, accepted):
    """判断任务是否可以幂等接取。"""
    return quest_id not in accepted


def reset_retry(state):
    """把失败重试的任务状态复位。"""
    if state_id(state) == "FAILED":
        return "ACTIVE"
    return state_id(state)


def has_cycle(graph):
    """检测任务链是否存在循环。"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def visit(node):
        color[node] = GRAY
        for nxt in graph.get(node, []):
            if color.get(nxt, WHITE) == GRAY:
                return True
            if color.get(nxt, WHITE) == WHITE and visit(nxt):
                return True
        color[node] = BLACK
        return False

    return any(color[node] == WHITE and visit(node) for node in graph)
