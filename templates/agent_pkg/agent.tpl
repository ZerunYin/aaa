`ifndef {{AGENT_FILENAME}}
`define {{AGENT_FILENAME}}

class {{agent_name}} extends uvm_sequencer;
  `uvm_component_utils({{agent_name}})

  {{agent_config_name}} m_agt_cfg;
  {{sequencer_name}} m_sqr;
  {{driver_name}} m_drv;
  {{monitor_name}} m_mon;

  extern function new(string name = "{{agent_name}}", uvm_component parent = null);

  extern function void build_phase(uvm_phase phase);

endclass : {{agent_name}}


function {{agent_name}}::new(string name = "{{agent_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction : new

function void {{agent_name}}::build_phase(uvm_phase phase);
  if(uvm_config_db#get({{agent_config_name}})::get(this, "", "m_agt_cfg", m_agt_cfg))
    `uvm_fatal(get_type_name(), $sformatf("%s fail to get config", get_name()))

  is_active = m_agt_cfg.is_active;

  m_mon = {{monitor_name}}::type_id::create("m_mon", this);
  m_mon.m_agt_cfg = m_agt_cfg;
  if(get_is_active()) begin
    m_drv = {{driver_name}}::type_id::create("m_drv", this);
    m_drv.m_agt_cfg = m_agt_cfg;
    m_sqr = {{sequencer_name}}::type_id::create("m_sqr", this);
    m_sqr.m_agt_cfg = m_agt_cfg;
  end
endfunction : build_phase

`endif // {{AGENT_FILENAME}}