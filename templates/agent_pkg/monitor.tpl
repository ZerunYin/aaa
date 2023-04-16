`ifndef {{MONITOR_FILENAME}}
`define {{MONITOR_FILENAME}}

class {{monitor_name}} extends uvm_sequencer;
  `uvm_component_utils({{monitor_name}})

  extern function new(string name = "{{monitor_name}}", uvm_component parent = null);

endclass : {{monitor_name}}


function {{monitor_name}}::new(string name = "{{monitor_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction

`endif // {{MONITOR_FILENAME}}