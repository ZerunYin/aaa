from utils import kv_upper


def interface_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["interface"]
    return {
        "interface_name": f"{agent_name}_{suffix}",
        "interface_filename": f"{agent_name}_{suffix}.sv",
    }


def sequence_item_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["sequence_item"]
    tb_name = hc["tb_name"]
    return {
        "sequence_item_name": f"{agent_name}_{suffix}",
        "sequence_item_basename": f"{tb_name}_base_{suffix}",
        "sequence_item_filename": f"{agent_name}_{suffix}.sv",
    }


def sequence_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["sequence"]
    dut_name = hc["dut_name"]
    tb_name = hc["tb_name"]
    return {
        "sequence_name": f"{agent_name}_{suffix}",
        "sequence_basename": f"{tb_name}_base_{suffix}",
        "sequence_filename": f"{agent_name}_{suffix}.sv",
    }


def sequencer_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["sequencer"]
    return {
        "sequencer_name": f"{agent_name}_{suffix}",
        "sequencer_filename": f"{agent_name}_{suffix}.sv",
    }


def driver_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["driver"]
    return {
        "driver_name": f"{agent_name}_{suffix}",
        "driver_filename": f"{agent_name}_{suffix}.sv",
    }


def monitor_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["monitor"]
    return {
        "monitor_name": f"{agent_name}_{suffix}",
        "monitor_filename": f"{agent_name}_{suffix}.sv",
    }


def agent_config_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["agent_config"]
    return {
        "agent_config_name": f"{agent_name}_{suffix}",
        "agent_config_filename": f"{agent_name}_{suffix}.sv",
    }


def agent_ctx(agent_name: str, sc: dict, hc: dict):
    ctx = dict()
    suffix = sc["agent"]
    ctx.update({
        "agent_name": f"{agent_name}_{suffix}",
        "agent_filename": f"{agent_name}_{suffix}.sv",
    })

    ctx.update(tb_ctx(sc, hc))

    ctx.update(interface_ctx(agent_name, sc, hc))
    ctx.update(sequence_item_ctx(agent_name, sc, hc))
    ctx.update(sequence_ctx(agent_name, sc, hc))
    ctx.update(sequencer_ctx(agent_name, sc, hc))
    ctx.update(driver_ctx(agent_name, sc, hc))
    ctx.update(monitor_ctx(agent_name, sc, hc))
    ctx.update(agent_config_ctx(agent_name, sc, hc))
    ctx.update(package_ctx(agent_name, sc, hc))

    kv_upper(ctx)

    return ctx


def package_ctx(agent_name: str, sc: dict, hc: dict):
    suffix = sc["package"]
    return {
        "package_name": f"{agent_name}_{suffix}",
        "package_filename": f"{agent_name}_{suffix}.sv",
    }


def tb_ctx(sc: dict, hc: dict):
    dut_name = hc["dut_name"]
    tb_name = hc["tb_name"]
    ctx = {
        "tb_name": tb_name,  # e.g. tb_icache
        "tb_filename": f"{tb_name}.sv",
        "tb_base_package_name": f"{tb_name}_base_{sc['package']}",  # e.g. tb_icache_pkg
        "tb_base_package_filename": f"{tb_name}_base_{sc['package']}.sv",
        "tb_base_sequence_item_name": f"{tb_name}_base_{sc['sequence_item']}",
        "tb_base_sequence_item_basename": "uvm_sequence_item",
        "tb_base_sequence_item_filename": f"{tb_name}_base_{sc['sequence_item']}.sv",
        "tb_base_sequence_name": f"{tb_name}_base_{sc['sequence']}",
        "tb_base_sequence_basename": "uvm_sequence",
        "tb_base_sequence_filename": f"{tb_name}_base_{sc['sequence']}.sv",
    }
    kv_upper(ctx)
    return ctx
