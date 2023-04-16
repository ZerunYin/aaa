`ifndef {{AGENT_FILENAME}}
`define {{AGENT_FILENAME}}

class {{agent_name}} extends uvm_sequencer;
  `uvm_component_utils({{agent_name}})

  extern function new(string name = "{{agent_name}}", uvm_component parent = null);

endclass : {{agent_name}}


function {{agent_name}}::new(string name = "{{agent_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction

`ednif // {{AGENT_FILENAME}}