`ifndef {{DRIVER_FILENAME}}
`define {{DRIVER_FILENAME}}

class {{driver_name}} extends uvm_sequencer;
  `uvm_component_utils({{driver_name}})

  extern function new(string name = "{{driver_name}}", uvm_component parent = null);

endclass : {{driver_name}}


function {{driver_name}}::new(string name = "{{driver_name}}", uvm_component parent = null);
  super.new(name, parent);
endfunction

`endif // {{DRIVER_FILENAME}}