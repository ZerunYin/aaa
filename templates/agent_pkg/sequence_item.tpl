`ifndef {{SEQUENCE_ITEM_NAME}}
`define {{SEQUENCE_ITEM_NAME}}

class {{sequence_item_name}} extennds {{sequence_item_basename}};
  `uvm_object_utils_begin({{sequence_item_name}})
  `uvm_object_utils_end
  extern function new(string name = "{{sequence_item_name}}");

endclass : {{sequence_item_name}}


function {{sequence_item_name}}::new(string name = "{{sequence_item_name}}");
  super.new(name);
endfunction

`ednif // {{SEQUENCE_ITEM_NAME}}
