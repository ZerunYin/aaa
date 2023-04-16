import os

from django.template import Context
from ctx import tb_ctx
from ctx import agent_ctx
from user_config import engine


def build_tb_pkg(sc: dict, hc: dict, out: str) -> None:
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


def build_agent_pkg(agent_name: str, sc: dict, hc: dict, out: str, env_name: str = "") -> None:
    dst_dir = f"{out}/{agent_name}_pkg" if env_name == "" else f"{out}/{env_name}_env/{agent_name}_pkg"

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    ctx = agent_ctx(agent_name, sc, hc)
    tpl_ctx = Context(ctx)
    for i in sc.keys():
        suffix = sc[i]
        tpl = engine.get_template(f"agent_pkg/{i}.tpl")
        with open(f"{dst_dir}/{agent_name}_{suffix}.sv", "w") as fh:
            fh.write(tpl.render(tpl_ctx))


def build_env(sc: dict, hc: dict, out: str) -> None:
    env_cnt = len(hc["envs"])
    if env_cnt == 1:
        agent_names = hc["envs"]["agents"]
        for agent_name in agent_names:
            build_agent_pkg(agent_name, sc, hc, out)
    elif env_cnt > 1:
        for env_name, agent_names in hc["envs"].items():
            for agent_name in agent_names:
                build_agent_pkg(agent_name, sc, hc, out, env_name)


def generate_tb(sc, hc, out):
    if not os.path.exists(out):
        os.mkdir(out)
    build_tb_pkg(sc, hc, out)
    build_env(sc, hc, out)


if __name__ == '__main__':
    from user_config import suffix_config, hier_config

    # build_tb_pkg(sc=suffix_config, hc=hier_config, out=".")
    # build_agent_pkg("cmd", sc=suffix_config, hc=hier_config, out=".")
    # build_env(sc=suffix_config, hc=hier_config, out=".")

    # build_env(suffix_config, hier_config, ".")

    generate_tb(sc=suffix_config, hc=hier_config, out="./demo")
