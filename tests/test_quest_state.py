import pytest
from game import quest_state as mod

CASES = [
    ("state_upper", "m.state_id('active') == 'ACTIVE'"),
    ("state_strip", "m.state_id(' fail ') == 'FAIL'"),
    ("branch_a", "m.branch_progress('a', {'a': 3, 'b': 1}) == 3"),
    ("branch_missing", "m.branch_progress('c', {'a': 3}) == 0"),
    ("rollback_order", "m.rollback_effects(['a', 'b']) == ['b', 'a']"),
    ("rollback_empty", "m.rollback_effects([]) == []"),
    ("grant_new", "m.grant_once('sword', set()) is True"),
    ("grant_old", "m.grant_once('sword', {'sword'}) is False"),
    ("order_by_priority", "m.ordered_conditions([{'id': 'a', 'priority': 2}, {'id': 'b', 'priority': 1}])[0]['id'] == 'b'"),
    ("accept_new", "m.accept_once('q1', set()) is True"),
    ("accept_old", "m.accept_once('q1', {'q1'}) is False"),
    ("retry_failed", "m.reset_retry('FAILED') == 'ACTIVE'"),
    ("retry_active", "m.reset_retry('ACTIVE') == 'ACTIVE'"),
    ("cycle_true", "m.has_cycle({'a': ['b'], 'b': ['a']}) is True"),
    ("cycle_false", "m.has_cycle({'a': ['b'], 'b': []}) is False")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
