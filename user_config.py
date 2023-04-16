from django.template import Engine

engine = Engine(dirs=["templates"])

suffix_config = {
    "interface": "if",
    "sequence_item": "item",
    "sequence": "seq",
    "sequencer": "sqr",
    "driver": "drv",
    "monitor": "mon",
    "agent_config": "agt_cfg",
    "agent": "agt",
    "package": "pkg",
}

dut_name = "icache"
hier_config = {
    "dut_name": f"{dut_name}",
    "tb_name": f"tb_{dut_name}",
    "agents": ["cmd", "msg"]
}
