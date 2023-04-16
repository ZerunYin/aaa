`ifndef {{AGENT_CONFIG_FILENAME}}
`define {{AGENT_CONFIG_FILENAME}}

class {{agent_config_name}} extends uvm_object;
  `uvm_object_utils_begin({{agent_config_name}})
  `uvm_object_utils_end

  extern function new(string name = "{{agent_config_name}}");

endclass : {{agent_config_name}}


function {{agent_config_name}}::new(string name = "{{agent_config_name}}");
  super.new(name);
endfunction

`endif // {{AGENT_CONFIG_FILENAME}}