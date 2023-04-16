`ifndef {{SEQUENCER_FILENAME}}
`define {{SEQUENCER_FILENAME}}

class {{sequencer_name}} extends uvm_sequencer;
  `uvm_component_utils({{sequencer_name}})

  extern function new(string name = "{{sequencer_name}}", uvm_component parent = null);

endclass : {{sequencer_name}}

function {{sequencer_name}}::new(string name = "{{sequencer_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction

`endif // {{SEQUENCER_FILENAME}}