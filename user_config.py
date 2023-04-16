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
    # if there is one env in the testbench, user should add agent names in the 'agents'
    # if there are more than one env in the testbench, user should delete the 'agents' and add custom envs
    "envs": {
        "agents": ["cmd", "msg"]
    },
}
