import os

from django.template import Context
from ctx import tb_ctx
from ctx import agent_ctx
from user_config import engine


def build_tb_pkg(sc, hc, out):
    tb_name = hc["tb_name"]
    dst_dir = f"{out}/{tb_name}_pkg"

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    ctx = tb_ctx(sc, hc)
    tpl_ctx = Context(ctx)
    for i in ["sequence_item", "sequence", "package"]:
        suffix = sc[i]
        tpl = engine.get_template(f"tb_pkg/{i}.tpl")
        with open(f"{dst_dir}/{tb_name}_{suffix}.sv", "w") as fh:
            fh.write(tpl.render(tpl_ctx))


def build_agent_pkg(agent_name, sc, hc, out):
    dst_dir = f"{out}/{agent_name}_pkg"

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    ctx = agent_ctx(agent_name, sc, hc)
    tpl_ctx = Context(ctx)

    for i in suffix_config.keys():
        suffix = sc[i]
        tpl = engine.get_template(f"agent_pkg/{i}.tpl")
        with open(f"{dst_dir}/{agent_name}_{suffix}.sv", "w") as fh:
            fh.write(tpl.render(tpl_ctx))


def build_env(sc, hc, out):
    env_cnt = len(hc["envs"])
    print(env_cnt)
    if env_cnt == 1:
        agents = hc["envs"]["agents"]
    elif env_cnt > 1:
        pass


if __name__ == '__main__':
    from user_config import suffix_config, hier_config

    # build_tb_pkg(sc=suffix_config, hc=hier_config, out=".")
    # build_agent_pkg("cmd", sc=suffix_config, hc=hier_config, out=".")

    build_env(suffix_config, hier_config, ".")
