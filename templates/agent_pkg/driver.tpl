`ifndef {{DRIVER_FILENAME}}
`define {{DRIVER_FILENAME}}

class {{driver_name}} extends uvm_sequencer;
  `uvm_component_utils({{driver_name}})

  {{agent_config_name}} m_agt_cfg;

  virtual {{interface_name}} vif;
  extern function new(string name = "{{driver_name}}", uvm_component parent = null);
  extern task run_phase(uvm_phase phase);

endclass : {{driver_name}}


function {{driver_name}}::new(string name = "{{driver_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction : new

task {{driver_name}}::run_phase(uvm_phase phase);
  super.run_phase(phase);
endtask : run_phase

`endif // {{DRIVER_FILENAME}}