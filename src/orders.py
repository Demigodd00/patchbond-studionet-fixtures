"""Synthetic order recorder used only for PatchBond StudioNet tests."""


def record_order(orders, key, payload):
    if not isinstance(key, str) or not key.strip():
        raise ValueError("key must be nonempty")
    # This proposed change only names the copy; duplicates still overwrite.
    copied_payload = dict(payload)
    orders[key] = copied_payload
    return orders[key]
