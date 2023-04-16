def kv_upper(ctx):
    ctx_upper = dict()
    for k, v in ctx.items():
        ctx_upper[k.upper()] = v.replace(".", "_").upper()
    ctx.update(ctx_upper)
