`ifndef {{SEQUENCE_NAME}}
`define {{SEQUENCE_NAME}}

class {{sequence_name}} extends {{sequence_basename}};
  `uvm_object_utils_begin({{sequence_name}})
  `uvm_object_utils_end

  extern function new(string name = "{{sequence_name}}");

endclass : {{sequence_name}}


function {{sequence_name}}::new(string name = "{{sequence_name}}");
  super.new(name);
endfunction

`endif // {{SEQUENCE_NAME}}