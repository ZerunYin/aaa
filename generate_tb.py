import os

from build_pkg import build_tb_pkg
from build_pkg import build_agent_pkg


def generate_tb(sc, hc, out):
    if not os.path.exists(out):
        os.mkdir(out)
    build_tb_pkg(sc, hc, out)

