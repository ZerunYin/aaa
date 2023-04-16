`ifndef {{AGENT_CONFIG_FILENAME}}
`define {{AGENT_CONFIG_FILENAME}}

class {{agent_config_name}} extends uvm_object;
  `uvm_object_utils({{agent_config_name}})

  extern function new(string name = "{{agent_config_name}}");

endclass : {{agent_config_name}}


function {{AGENT_CONFIG_NAME}}::new(string name = "{{agent_config_name}}");
  super.new(name, parent);
endfunction

`ednif // {{AGENT_CONFIG_FILENAME}}