"""Synthetic order recorder used only for PatchBond StudioNet tests."""


def record_order(orders, key, payload):
    if not isinstance(key, str) or not key.strip():
        raise ValueError("key must be nonempty")
    if key not in orders:
        orders[key] = dict(payload)
    return orders[key]
