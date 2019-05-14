# Python

[TOC]

## Shebangs and encoding

```
#!/usr/bin/env python
# coding=utf-8
```

## Try / Except

Whenever you want to break a **try/except** command in a running script using `cmd + D`, the following scructure must be used, in order to catch the *KeyboardInterrupt*, *SystemExit* errors.

```
try:
    title_success = self.updateTitle(shopify_id, title)
    body_success = self.updateBody(shopify_id, body)

    if not all([title_success, body_success]):
        _id_to_remove.append(row['product_id'])

except (KeyboardInterrupt, SystemExit):
    raise ValueError('Script stopped manually!')

except:
    # self.notifyPriceStockIssue(row, 6)
    _id_to_remove.append(row['product_id'])
```

