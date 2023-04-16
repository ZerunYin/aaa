import os
import shutil

from django.template import Context
from ctx import tb_ctx
from ctx import agent_ctx
from user_config import engine


def build_tb_pkg(sc, hc, out):
    tb_name = hc["tb_name"]
    dst_dir = f"{out}/{tb_name}_pkg"

    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)

    ctx = tb_ctx(sc, hc)
    tpl_ctx = Context(ctx)
    for i in ["sequence_item", "sequence", "package"]:
        suffix = sc[i]
        tpl = engine.get_template(f"tb_pkg/{tb_name}_{suffix}.tpl")
        with open(f"{dst_dir}/{tb_name}_{suffix}.sv") as fh:
            fh.write(tpl.render(tpl_ctx))






def build_agent_pkg(agent_name, sc, hc, out):
    pass